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

## Templates 

1. create a __templates__ directory in endgame directory
2. Your project’s TEMPLATES setting describes how Django will load and render templates.
3. The default settings file configures a __DjangoTemplates__ backend 
whose __APP_DIRS__ option is set to True. 
4. By convention DjangoTemplates looks for a “templates” subdirectory in each of the INSTALLED_APPS.
5. need to import __from django.template import loader__
> You need to create "templates" directory in apps directory with its name as sub-directory.
in our project "endgame" is app so we create a "templates" directory and then we create 
> sub-directory "endgame" and save a index.html (endgame/templates/endgame/index.html)
```python
from django.template import loader
from django.http import HttpResponse

def temp_view(request):
    temp = loader.get_template("endgame/index.html")
    ctx = {'name': 'akhil'} # context object
    return HttpResponse(temp.render(ctx, request))
```
A shortcut: render()¶
It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template. 
Django provides a shortcut. Here’s the full index() view, rewritten:
```python
from django.shortcuts import render

def temp_view_advance(request):
    return render(request,'endgame/index.html',{})
```

