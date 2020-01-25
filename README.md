# Notes-WebApp

A simple web app that allows you to take notes on the go

## About this project

My second attempt at making a web app using flask. Tried my best to implement all the best practices of Flask.
Enjoy.

## Notes

This website was created using Flask. Flask is a lightweight `WSGI`_ web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around `Werkzeug`_
and `Jinja`_ and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.


Installing
----------

Installing required packages using `pip`_:

    pip install -r requirements.txt
    
Or, running in virtualenv:

    cd <path to the app directory>
    source env/bin/activate
    
Running the website:

    cd <path to the Notes-WebApp directory>
    python run.py [development | production]

## Features

* WTForms for robust form validations
* SQLAlchemy for robust Object Relational Mapper to database

* Home page which displays: word of the day, news articles, as well as notes of 
other people that are either public or shared with you
* Starring function to save a particular note
* Folders to organize notes for easier access

