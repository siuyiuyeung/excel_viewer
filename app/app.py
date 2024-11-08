from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from pathlib import Path

app = Flask(__name__)

# Global dictionary to store DataFrames
excel_data = {}

def load_excel_files(directory="excel_files"):
    """Load all Excel files from the specified directory"""
    Path(directory).mkdir(exist_ok=True)
    excel_data.clear()

    for file in os.listdir(directory):
        if file.endswith(('.xlsx', '.xls')):
            file_path = os.path.join(directory, file)
            try:
                # Read all sheets into a dictionary
                excel_file = pd.read_excel(file_path, sheet_name=None)
                excel_data[file] = excel_file
            except Exception as e:
                print(f"Error loading {file}: {str(e)}")

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html', files=list(excel_data.keys()))

@app.route('/search')
def search():
    """Search across all Excel files and sheets with multiple keywords"""
    queries = request.args.getlist('query')  # Get all query parameters
    if not queries:
        return jsonify([])

    results = []

    for file_name, file_data in excel_data.items():
        for sheet_name, df in file_data.items():
            # Convert all columns to string for searching
            df_str = df.astype(str)

            # Create a mask for each keyword
            matches = None
            for query in queries:
                query = query.lower()
                current_matches = df_str.apply(lambda x: x.str.contains(query, case=False, na=False))
                current_matches = current_matches.any(axis=1)

                if matches is None:
                    matches = current_matches
                else:
                    # Combine with AND operation
                    matches = matches & current_matches

            if matches is not None and matches.any():
                # Get matching rows
                matching_rows = df[matches]

                # Convert matching rows to dict and add metadata
                for idx, row in matching_rows.iterrows():
                    result = {
                        'file': file_name,
                        'sheet': sheet_name,
                        'data': row.where(pd.notnull(row), None).to_dict()  # Replace NaT with None
                    }
                    results.append(result)

    return jsonify(results)


@app.route('/refresh')
def refresh_files():
    """Reload all Excel files"""
    load_excel_files()
    return jsonify({'status': 'success', 'files': list(excel_data.keys())})

if __name__ == '__main__':
    # Load initial Excel files
    load_excel_files()
    # Run on all interfaces
    app.run(host='0.0.0.0', debug=True)
