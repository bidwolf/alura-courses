# Flask course
This course aims to create a simple web application league of legends based on Flask framework in python to create a real app with a database and a web interface.

## About Flask

Flask is a micro web framework written in Python, that means it is simple and easy to use, since it don't have any dependencies to external libraries. It was created by Armin Ronacher in 2010 and it is based on the Werkzeug toolkit and Jinja2 template engine.

### Setup the environment

First you have to install python in your machine. You can download it from the official website [here](https://www.python.org/downloads/).

Also, you have to install pip, the python package manager. You can download it from the official website [here](https://pip.pypa.io/en/stable/installing/).


And to setup the environment, you must have venv installed. You can install it by running the following command:

```bash
pip install venv
```
#### Creating the virtual environment
After that, you can create a virtual environment by running the following command:

```bash

python3 -m venv .venv # this will create a virtual environment in the .venv folder (for linux users)

```

In order to activate the virtual environment, you have to run the following command:

```bash

source .venv/bin/activate # this will activate the python virtual environment (for linux users)

```
>[!TIP]
> If you are using visual studio code as your code editor, you can activate the virtual environment by press `command + shift + p` and type "Python: Select Interpreter" and select the .venv folder.

### Installing the dependencies

Finally you can install the dependencies by running:
```bash

pip install -r requirements.txt  # this will install all the dependencies in the requirements.txt file

```

>[!TIP] 
>In order to generate the requirements.txt file, you must run the command:
> ```bash
> pip freeze > requirements.txt
> ```

## Creating the web application

This course will use render_template to render the html files. The render_template function will look for the html files in the templates folder.