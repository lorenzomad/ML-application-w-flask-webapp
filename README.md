# Overview

In this project, I built a Github repository from scratch and performed Continuous Integration and Continuous Delivery. I used Github Actions along with a Makefile, requirements.txt and application code to perform lint, test, and install cycle. Then, I integrated this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Continuous Integration

Continuous integration is performed through the use of Github actions to run test and lint 
[![Python application test with Github Actions](https://github.com/lorenzomad/ML-application-w-flask-webapp/actions/workflows/main.yml/badge.svg)](https://github.com/lorenzomad/ML-application-w-flask-webapp/actions/workflows/main.yml)

# Project Plan

link to the spreadsheet that includes the final project plan (the effort foreseen for each task is reflected in the amount of weeks for the associated activity)
https://github.com/lorenzomad/ML-application-w-flask-webapp/blob/main/p_man/project_management.xlsx

link to the trello board for the project (if you have just been added to the project and need access to the board, request to the Project Management).
https://trello.com/b/vqoxq9oC/building-ml-application-with-flask


## Instructions

* Steps to run the project:

1. clone or fork this github repository 
2. check that the webapp is running at the link: https://lorenzo-flask-webapp.azurewebsites.net/
3. you can run the bash script make_predict_azure_app.sh to get a prediction
 
* Architectural Diagram>
here is an overview of the different parts of the project. 
The continuous integration is done through github actions and the continuous delivery is enabled through the azure pipelines
The project is running in an azure webapp at the following link: https://lorenzo-flask-webapp.azurewebsites.net/

<img width="615" alt="image" src="https://user-images.githubusercontent.com/106270843/192147371-dedd7409-ff73-4cd6-a130-c441561f8ca2.png">


* Project running on Azure App Service
<img width="611" alt="image" src="https://user-images.githubusercontent.com/106270843/192147393-a154bc7c-b22f-4472-a2c7-341f41cb11ea.png">


* Project cloned into Azure Cloud Shell
<img width="476" alt="image" src="https://user-images.githubusercontent.com/106270843/192108868-eb07d585-3cd3-4c18-a6e0-df83089d7147.png">


* Passing tests that are displayed after running the `make all` command from the `Makefile`
<img width="951" alt="image" src="https://user-images.githubusercontent.com/106270843/192108897-acd77863-7a1c-4e1d-82d0-91c865485fae.png">


* Output of a test run
<img width="619" alt="image" src="https://user-images.githubusercontent.com/106270843/192143787-db71b00a-05ff-48b0-b3ef-dfdba189fdf1.png">


* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment
<img width="957" alt="image" src="https://user-images.githubusercontent.com/106270843/192108906-95c78231-61ea-40bb-8470-75c22fcfe234.png">


* Successful prediction from deployed flask app in Azure Cloud Shell.  

<img width="619" alt="image" src="https://user-images.githubusercontent.com/106270843/192143787-db71b00a-05ff-48b0-b3ef-dfdba189fdf1.png">


* Output of streamed log files from deployed application
<img width="960" alt="image" src="https://user-images.githubusercontent.com/106270843/192143743-4db97822-af5f-4c75-937d-cd3716ba0dd1.png">


## Enhancements

enhancements for the future:
  1. create a GUI where the webapp can allow the user to input the input values and it will output the prediction
  2. extend the machine learning algorythm to provide predictions also for other areas. allow in the GUI the selection of the area for which the prediction should be run and load accordingly the correct model 
  3. include more specific tests for the CI pipeline
  4. make the webapp more appealing by improving the graphic

## Demo 

<TODO: Add link Screencast on YouTube>
