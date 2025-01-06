# Intelnetus

Copyright &copy; 2025 Georgios Milonas. All rights reserved.

## Overview
Intelnetus is a web application that is directed to help science network
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

## Set Up
Intelnetus uses `pybliometrics` Python package (developed and founded by Michael E.Rose and John Kitchin) for accessing, searching and retrieving data from Scopus &copy; database, developed by Elsevier &copy;.
For the sufficient use of `pybliometrics` APIs, the creation of a **config.ini** file is neccessary.
Usually, the file is included in **.pybliometrics** folder which is automatically generated by the package itself and it has the following form:
```
[Directories]
AbstractRetrieval = path\to\.pybliometrics\Scopus\abstract_retrieval
AffiliationRetrieval = path\to\.pybliometrics\Scopus\affiliation_retrieval
AffiliationSearch = path\to\.pybliometrics\Scopus\affiliation_search
AuthorRetrieval = path\to\.pybliometrics\Scopus\author_retrieval
AuthorSearch = path\to\.pybliometrics\Scopus\author_search
CitationOverview = path\to\.pybliometrics\Scopus\citation_overview
ScopusSearch = path\to\.pybliometrics\Scopus\scopus_search
SerialSearch = path\to\.pybliometrics\Scopus\serial_search
SerialTitle = path\to\.pybliometrics\Scopus\serial_title
PlumXMetrics = path\to\.pybliometrics\Scopus\plumx
SubjectClassifications = path\to\.pybliometrics\Scopus\subject_classification

[Authentication]
APIKey = YOUR_SCOPUS_API_KEYS

[Requests]
Timeout = 20
Retries = 5
```

In this file, several options regarding package's functionality can be set, like installed classes paths, requests policy and
**Scopus API keys**.

In case the file is not created by default, you can run the following Python command to do this manually:
```
import pybliometrics.scopus.utils as utils

utils.create_config("path\for\config\file")
```

>**NOTE**: Documentation about API keys generation, management and code integration can be found in [Elsevier Developer Portal](https://dev.elsevier.com/scopus.html).
>In addition, a detailed guide about `pybliometrics` integration in Python code can be found in [pybliometrics readthedocs](https://pybliometrics.readthedocs.io/en/stable/).

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

## Communication
For any queries or feedback regarding this repository, you can reach me out through the contact information attached in my [profile page](https://github.com/Gemyl/profile)😊.
