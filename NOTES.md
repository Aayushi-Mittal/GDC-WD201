# DJANGO
Django is a web application framework written in Python programming language. It is based on MVT (Model View Template) design pattern. The Django is very demanding due to its rapid development feature. It takes less time to build application after collecting client requirement.

This framework uses a famous tag line: **The web framework for perfectionists with deadlines**.

By using Django, we can build web applications in very less time. Django is designed in such a manner that it handles much of configure things automatically, so we can focus on application development only.

Django is widely accepted and used by various well-known sites such as: Instagram, Mozilla, Disqus, Pinterest, Bitbucket, etc.

## Features of Django
- Rapid Development
- Secure
- Scalable
- Fully loaded
- Versatile
- Open Source
- Vast and Supported Community

## Setting up a virtual environment
1. ```$ apt-get install python3-venv```
2. ```$ mkdir djangoenv```
3. ```$ python3 -m venv djangoenv```
4. ```$ source djangoenv/bin/activate```

### Install Django
```$ pip install django```

### Setup Project
```$ django-admin startproject projectname```

A Django project contains the following packages and files. The outer directory is just a container for the application. We can rename it further.

- **manage.py**: It is a command-line utility which allows us to interact with the project in various ways and also used to manage an application. A directory (djangpapp) located inside, is the actual application package name. Its name is the Python package name which we'll need to use to import module inside the application.
- ```__init__.py```: It is an empty file that tells to the Python that this directory should be considered as a Python package.
- **settings.py**: This file is used to configure application settings such as database connection, static files linking etc.
- **urls.py**: This file contains the listed URLs of the application. In this file, we can mention the URLs and corresponding actions to perform the task and display the view.
- **wsgi.py**: It is an entry-point for WSGI-compatible web servers to serve Django project.

Initially, this project is a default draft which contains all the required files and folders.

## Django Admin Interface
Django provides a built-in admin module which can be used to perform CRUD operations on the models. It reads metadata from the model to provide a quick interface where the user can manage the content of the application.

This is a built-in module and designed to perform admin related tasks to the user.

## Django App

Django application consists of project and app, it also generates an automatic base directory for the app, so we can focus on writing code (business logic) rather than creating app directories.

The difference between a project and app is, a project is a collection of configuration files and apps whereas the app is a web application which is written to perform business logic.

##  Django - MVT or MVC framework?

The MVT (Model View Template) is a software design pattern. It is a collection of three important components Model View and Template. 
- The Model helps to handle database. It is a data access layer which handles the data.
- The Template is a presentation layer which handles User Interface part completely. 
- The View is used to execute the business logic and interact with a model to carry data and renders a template.

Although Django follows MVC pattern but maintains it's own conventions. So, control is handled by the framework itself.

There is no separate controller and complete application is based on Model View and Template. That's why it is called MVT application. Here, a user requests for a resource to the Django, Django works as a controller and check to the available resource in URL. If URL maps, a view is called that interact with model and template, it renders a template. Django responds back to the user and sends a template as a response.
