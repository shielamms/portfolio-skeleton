# Django Portfolio App Skeleton

Skeleton app for building a portfolio site in Django

## Dev Setup

```
python -m venv venv
source venv/bin/activate

pip install Django
```

## To run the app

In the project root:
```
python manage.py runserver
```

## To add a DB model

Modify the `models.py` in any of the apps.
Then run `python manage.py makemigrations <app_name>/` to make a migration file.
For example:
```
python manage.py makemigrations projects
```

To run the migration:
``` 
python manage.py migrate projects
```
