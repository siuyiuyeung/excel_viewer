# EXCEL VIEWER
## Description
Dynamic searching within multiple Excel files
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
copy concerned files to excel_files folder

## Start
```shell
docker compose up -d --build
```
## Stop
```shell
docker compose down
```