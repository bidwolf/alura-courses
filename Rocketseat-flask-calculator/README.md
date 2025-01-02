# Rocketseat Flask Calculator 🇺🇸

This project aims to create a simple calculator using Flask, a lightweight Python web framework.
The calculator project has 3 challenges that will be solved in their respective routes.
We use the Blueprint feature from Flask to organize the routes, and the main objective of this course is actually to learn Design Patterns and how to apply them in any project using Flask and Python.

## Blueprint

Blueprints help us to organize the actual code by separating the routes into different files.
Each blueprint should be registered in the main application file, and just like the main application, each one can register another blueprint.

While creating a blueprint, we need to pass the name of the blueprint and the name of the file that will be used to import the blueprint (you can do that by passing the `__name__` variable).

Each blueprint can have their own route prefix, and can also have their own error handlers.

to create a route from the blueprint we need to use the `@name_of_blueprint.route` decorator. It's like the normal `@app.route` decorator.

Blueprints are not a entire application, they need to be registered in the main application file, and when we have to change anything in the blueprint, we need to restart the entire application.

Blueprints can have their own static files or templates, by passing the `static_folder` and `template_folder` parameters when creating the blueprint.

If the blueprint does not have a `url_prefix`, the static folder will be the same as the main application static folder.

You can access the static folder in the flask application or in any template by using the `url_for` function, passing the name of the blueprint and the name of the file.

```python
url_for('name_of_blueprint.static',filename='css/style.css')
```
About templates, you can use the `render_template` function, passing the name of the blueprint and the name of the file.

>[!WARNING]
> If you have a template with the same name in the main application and in the blueprint, the main application template has priority. To use the blueprint template, Flask recommends using the following pattern to the folder structure:
> ```
> yourpackage/
>└── blueprints/
>    └── your_blueprint_name/
>        ├── templates/
>        │   └── your_blueprint_name/
>        │       └── index.html
>        └── __init__.py
> ```
> In the blueprint file, you can use:
> ```python
> render_template('your_blueprint_name/index.html')
>```

## Factory Pattern

The Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. In Python, this pattern can be implemented by defining a method in the base class that creates objects, and allowing subclasses to override this method to change the type of objects created.

Example:
```python
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteProduct1:
    def operation(self):
        return "{Result of the ConcreteProduct1}"

creator = ConcreteCreator1()
print(creator.some_operation())
```

## Facade Pattern

The Facade Pattern is a structural design pattern that provides a simplified interface to a complex subsystem. It hides the complexities of the system and provides an easy-to-use interface for the client. In Python, this pattern can be implemented by creating a facade class that wraps the subsystem classes and provides a simplified interface to the client.

Example:
```python
class Subsystem1:
    def operation1(self):
        return "Subsystem1: Ready!"

    def operation_n(self):
        return "Subsystem1: Go!"

class Subsystem2:
    def operation1(self):
        return "Subsystem2: Get ready!"

    def operation_z(self):
        return "Subsystem2: Fire!"

class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2):
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self):
        results = []
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)

subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
facade = Facade(subsystem1, subsystem2)
print(facade.operation())
```
