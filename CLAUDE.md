# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a web-based Excel file viewer and search application built with Flask that allows users to search across multiple Excel files using multiple keywords with AND logic.

## Key Commands

### Development and Running

Start the application:
```bash
docker compose up -d --build
```

Stop the application:
```bash
docker compose down
```

The application runs on port 5000 inside the container and is exposed on port 80 on the host.

### Adding Excel Files

Place Excel files (.xlsx or .xls) in the `excel_files` directory. The application will load them on startup or when the refresh button is clicked.

## Architecture

### Core Components

1. **app/app.py** - Flask application with three main routes:
   - `/` - Main page serving the HTML interface
   - `/search` - API endpoint accepting multiple `query` parameters for AND-based search
   - `/refresh` - Reloads all Excel files from the directory

2. **app/templates/index.html** - Single-page web interface with:
   - Dynamic keyword input fields (add/remove functionality)
   - Search results displayed in a table format grouped by file and sheet
   - Refresh button to reload Excel files

### Data Flow

1. On startup, the application loads all Excel files from `excel_files/` into memory as pandas DataFrames
2. Each file's sheets are stored in a nested dictionary structure: `excel_data[filename][sheetname]`
3. Search converts all data to strings and applies AND logic across multiple keywords
4. Results include file name, sheet name, and matching row data

### Key Technical Details

- Uses pandas for Excel file reading and data manipulation
- All Excel data is loaded into memory on startup for fast searching
- Search is case-insensitive and works across all columns
- The application mounts `./excel_files` as a volume for persistence across container restarts
- Flask runs in debug mode with auto-reload enabled

## Common Tasks

When modifying search functionality, the logic is in `app.py:search()` function. The current implementation:
- Uses AND logic for multiple keywords
- Converts all data to strings for universal searching
- Returns results as JSON with file/sheet metadata

When updating the UI, all frontend code is in `templates/index.html` including:
- JavaScript for dynamic keyword management
- Result rendering logic
- CSS for responsive design