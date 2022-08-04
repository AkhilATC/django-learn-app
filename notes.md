## Activating models
To include the app in our project, 
we need to add a reference to its configuration class in the INSTALLED_APPS setting.
The __EndgameConfig__ class is in the endgame/apps.py file, 
so its dotted path is 'endgame.apps.EndgameConfig'.
Edit the wakanda/settings.py file and add that dotted path to the INSTALLED_APPS setting.

Now Django knows to include the endgame app. Let’s run another command:

```commandline
python manage.py makemigrations endgame
```
By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration
Now, run migrate again to create those model tables in your database:
```commandline
python manage.py migrate
```

The migrate command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them 
against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

In short if any change w.r.t models do following steps:
- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.

## Creating an admin user

```commandline
python manage.py createsuperuser
```
register __Avengers__ model in endgame/admin.py
```python
from django.contrib import admin
from .models import Avengers
# Register your models here.

admin.site.register(Avengers)
```
