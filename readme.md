### Flask MVC Template

A Flask mvc template to start quickly a new Flask project with reusability of its components in mind

# Structure:

```
/Your_application
    |-- run.py
    |-- config.py
    |__ /env             
    |__ /app           
         |-- __init__.py
         |-- /module_1
             |-- __init__.py
             |-- controllers.py
             |-- models.py                
             |-- script.py
         |-- /module_2
             |-- __init__.py
             |-- controllers.py
             |-- models.py
             |-- better_script.py                
         |-- /module_X
             |-- __init__.py
             |-- controllers.py
             |-- models.py
         |-- /etc...
         |__ /templates
             |__ /module_1
                 |-- index.html
             |__ /module_2
                 |-- page.html
             |__ /module_X
                 |-- X.html
         |__ /static
         |__ ..
         |__ .
    |__ ..
    |__ .
```