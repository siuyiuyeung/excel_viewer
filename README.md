# EXCEL VIEWER
## Description
Dynamic searching within multiple Excel files with password authentication and 24-hour session timeout
## Dependencies
- Docker
- Python
- Flask
- Pandas
- Openpyxl
- Numpy
## Folder structure
```
├───excel_files
│   └───*.xlsx
├───app
│   ├───app.py
│   └───templates
│       └───index.html
├───dock-compose.yml
├───Dockerfile
```
## Setup
1. Copy Excel files to excel_files folder
2. Set password by editing EXCEL_VIEWER_PASSWORD in docker-compose.yml (default: excel_viewer_2024)

## Start
```shell
docker compose up -d --build
```
## Stop
```shell
docker compose down
```

## Features
- Password authentication required to access the application
- 24-hour session timeout for security
- Search across multiple Excel files with AND logic for multiple keywords
- Dynamic file refresh without restarting the application
- Responsive web interface