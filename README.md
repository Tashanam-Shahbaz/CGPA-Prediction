

<img src="./img.jpeg" />

## 🚀 About Project 
------------
In this project, we will experiment with a real world dataset of grades with CGPA, and to explore how
machine learning algorithms can be used to find the patterns in data.

 We have a dataset of 42 features of different courses. In corresponding to these we are
required to predict CGPA. We can solve this problem using **SUPERVISED LEARNING** algorithms.


## 📂 Project Organization
------------
├── src
│   ├── controller
│   │   ├── **/*.css
│   ├── views
│   ├── model
│   ├── index.js
├── public
│   ├── css
│   │   ├── **/*.css
│   ├── images
│   ├── js
│   ├── index.html
├── dist (or build
├── node_modules
├── package.json
├── package-lock.json 
└── .gitignore

## 🔮 User Interface
------------
- The UI of the project is built using Flask. HTML and CSS.
- https://cgpa-prediction-3.herokuapp.com/

## 🏡 Developer Setup Guide
------------

#### ⏮️ Prerequisites
- Account on <a href="https://signup.heroku.com/">Heroku</a>
- Heroku CLI
- <a href="https://docs.docker.com/get-started/">Docker</a> 
- Docker Desktop

    `cd Deployment_Folder`

    `python venv -m my-venv`

    `.\my-venv\Scipts\activate`

    `pip install requirements.txt`
     
 Run Flask app locally:
 
     `python app.py'
 
 Build the docker image
 
      `docker build -t docker_application_name . '
 
 Run the docker container and test it locally  
 
       `docker images'
       `docker run --name flask1 -dit -p 5000:5000 docker_application_name'
       `docker ps'
       
Login to heroku container registry
       
       `heroku container:login'

Create an heroku app

       `heroku create heroku_app_name'
       
Build the image and push the image to heroku registry.

       `heroku container:push web -a heroku_app_name'
       
Creating the container on heroku host and hosting it publicly

       `heroku container:release web -a heroku_app_name'
       
To open the app in your default browser

       `heroku open -a heroku_app_name'
       
       
      
## ⚒️ Built Upon
------------

    - Python
    - Heroku
    - Docker
    
## 🔧 Tools Used
------------

    - Visual Studio Code
    - Google Colaboratory
    - Microsoft Excel

## 📋 License
------------

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the `LICENSE` file for details.


