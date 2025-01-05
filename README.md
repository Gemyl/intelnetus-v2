# Intelnetus

Copyright &copy; 2025 Georgios Milonas. All rights reserved.

## Overview
Intelnteus is a web applications that is directed to help science network
researchers to perform statistical analysis with greater accuracy and ease.

Key features:
- **Search** in a large dataset of scientific publications metadata based on your criteria (keywords, time period, fields etc.)
- **Manage** your search's results by viewing, filtering and exporting
- **Duplicates** detection for removing identical records
- **Insights** of metadata retrieved through a variety of charts and diagrams
- **Network Visualization** dashboard with network indices available

## Installation
Source code of Intelnetus is organized in two base directories: **intelnetus-api** and **intelnetus-ui** which they host the back-end and front-end accordingly.

Intelnetus back-end is developed in Python (v3.12.8) with Flask (v3.0.0) framework. To install all dependecies run via `pip` the following command within **intelnetus-api** directory:
```
pip install -r requirements.txt
```

>**NOTE**: The creation of a Python Virtual Environment is strongly recommended. To create one, run inside **intelnetus-api** directory:
>```
>python -m venv .your_env

Intelnetus frontend is developed in Angular (v17). To install all necessary packages run via `npm` the following command inside **intelnetus-ui** directory:
```
npm i --save
```

## Project Start Up
### Flask Server
Navigate in  **intelnetus-api** directory and run:
```
python app.py --dev
```

>**NOTE**: The `--dev` argument indicates that Flask server is running within a DEVELOPMENT environment. Remove this argument to run server within a PRODUCTION environment.

### Angular Project
Navigate in **intelnetus-ui** directory and run:
```
ng serve 
```
