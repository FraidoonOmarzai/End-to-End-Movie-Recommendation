<h1 align=center> End-to-End-Movie-Recommendation</h1>

* In this project I am using content based recommendation system to recommend movies.

```bash
## MLOps Lifecycle:

    1. Problem Definition and Requirement Gathering
    2. EDA
    3. Feature Engineering
    4. Feature Selection
    5. Model Creation
    6. Model Hyper-parameter Tunning
    7. Model Deployment
    8. Retraining Approaches
```

```bash
## Workflows
1. Update config.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
9. Update the dvc.yaml
```


## Steps

* get clone the repository
* define template.py
* define setup.py
* create a new environment
```bash
conda create -n recom-env python=3.9 -y
conda activate recom-env
```
* create requirements.txt and install the required dependencies
* define logger
* define utils

* **Data Ingestion**

* **Data Validation**

* **EDA&Training.ipynb** 

* **Data Transformation**

* **Model Training**

* using **streamlit** to create a web page for our project

* **Docker**
    * adding code to docker file
    * bulid the docker image
    ```bash
    docker build -t streamlit-app .
    docker ps
    docker images
    ```
    * running our app using docker
    ```bash
    docker run -p 8080:8080 streamlit-app
    ```
    * open the browser and run
    ```bash
    htpp://localhost:8080
    ```