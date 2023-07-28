[![Python Continuous Integration](https://github.com/architkaila/Text-To-Image-MircoService/actions/workflows/main_text-to-image-microservice.yml/badge.svg)](https://github.com/architkaila/Text-To-Image-MircoService/actions/workflows/main_text-to-image-microservice.yml)

# Text To Image MircoService
> #### _Archit, Shen, Shrey | Summer '23 | Duke AIPI 561 MLOps Final Project_

## Project Description
This project is a microservice that takes a text prompt and generates an image based on the text. The microservice is hosted on Azure App Service along with a CI/CD pipeline setup such that any changes to the code are automatically deployed to the App Service. The microservice is built using FastAPI. The model deployed for this microservice is [StabilityAI's Stable Diffusion 2.1](https://huggingface.co/stabilityai/stable-diffusion-2-1).

## Setting up the project
**1. The project can be run using the following command:**  
```
make install
```
This upgrades pip, installs the requirements and sets up the environment.

**2. To run the formatting on the code:**  
```
make format
```
**3. To run linting on the code:**  
```
make lint
```
**4. To run all the tests:**
```
make test
```
**5. To run all the steps including setup, code formating using black and linting:**  
```
make all
```

## Usage
**1. To start the FastAPI service on port 8080:**  
```
uvicorn main:app --port 8080 --reload
```
**2. To make calls to the API using CURL (prompt: photo of an astronaut riding a horse on mars):**  
```
curl -X 'GET' 'http://text-to-image-microservice.azurewebsites.net/vector_image/?prompt=photo%20of%20an%20astronaut%20riding%20a%20horse%20on%20mars' -H 'accept: application/json' -o "photo.png"
```

## Project Structure
The project data and code files are arranged in the following manner:
```
├── .github                           <- directory for github actions 
├── tests                             <- directory for tests
    ├── test_main.py                  <- tests for the API
├── .gitignore                        <- git ignore file
├── LICENSE                           <- license file
├── main.py                           <- main file for the API
├── Makefile                          <- makefile to run the setup, formatting and linting
├── README.md                         <- description of project and how to set up and run it
├── requirements.txt                  <- requirements file to document dependencies
```
