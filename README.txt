HackBright Project
_________________________________________________________________________________________

This repository represents my final project at HackBright Academy. This project is a project I created 
from an API called ShopCollective ( https://www.shopstylecollective.com/api/overview). My project has 
a search function that searches for clothing items and returns suggestions for your future purchases. 

_________________________________________________________________________________________

Here is an explanation of the files and what you need to do if you want to duplicate my efforts:

1. model.py: You want to run this first. With SQLAlchemy it models the database and creates the necessary 
relationships between tables

1. seed.py : You want to run this second. This file calls the API gathers the necessary records and seeds my databse

2. server.py: Run this file to start your server. It also contains all the routes and rendres the appropriate html files.

3. the static folder contains main.js and my stylesheet, style.css. Main.js contains all the Ajax for rendering information
from the databse.

4. The templates folder contains all of the html pages




