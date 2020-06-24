# Django notes

- [Django notes](#django-notes)
  - [day 1: environment and a simple project](#day-1-environment-and-a-simple-project)
    - [environment](#environment)
    - [simple project](#simple-project)
  - [day 2: more about HelloWorld](#day-2-more-about-helloworld)
    - [view and template](#view-and-template)
    - [model](#model)

## day 1: environment and a simple project

### environment

windows10, python3, vs code, MySQL8
steps:  

- install Django  
  pip install Django  

- install mysql8  
  go to MySQL community download [installer](https://dev.mysql.com/downloads/windows/installer/8.0.html)  
  download [DBeaver](https://dbeaver.io/files/dbeaver-ce-latest-x86_64-setup.exe), tool of database management

### simple project

- open cmd, and switch to expected directory. then run command:  
  django-admin.py startproject HelloWorld  
  create a Django project named HelloWorld. open folder HelloWorld, the tree of file and folder like this:  
  |-- HelloWorld  
  |&nbsp;&nbsp; |-- `__init__`.py  
  |&nbsp;&nbsp; |-- asgi.py  
  |&nbsp;&nbsp; |-- settings.py  
  |&nbsp;&nbsp; |-- urls.py  
  |&nbsp;&nbsp; `-- wsgi.py  

  `-- manage.py  

- then modify the setting.json
  add configuration for Django project. like this:

  ```json
        {
            "name":"Python: Django",
            "type":"python",
            "request":"launch",
            "program":"${file}",
            // "program":"${file}\\..\\manage.py",
            "console":"integratedTerminal",
            "args":[
                "runserver",
                "0.0.0.0:8080",
            ],
            "django":true
        },
  ```

  to launch Django project, open the manage.py, then open debug panel, select python:Django interpreter.

  open 127.0.0.1:8080 in web browser.

## day 2: more about HelloWorld

### view and template

- create folders, views and templates  
  create folder views in HelloWorld/HelloWorld  
  create folder templates in HelloWorld  
  Django use the model of  MTV(model, template, view), similar to MVC(model, view, controller).  
  the part of view in MTV is similar to controller of MVC.  
  all views will be put in folder views.(out of personal habit).

  modify the setting.py in HelloWorld/HelloWorld:

```python
# some code
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates",],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# some code
```

- create hello.html and runoob.html in HelloWorld/templates  
  hello.html:  

  ```html
  <!DOCTYPE html>
  <html>
      <head>
          <title>Hello</title>
      </head>
      <body>
          Hello Django
      </body>
  </html>
  ```

  runoob.html:

    ```html
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Test</title>
        </head>
        <body>
            <div>
                <h1>{{hello}}</h1>
                <p>{{name}}</p><br>
                <p>name:  {{person.name}}</p>
                <p>sex:  {{person.sex}}</p>
                <p>{% if person.sex|stringformat:"s" == "male" %} age:  {{person.age}} {% endif %}</p>
            </div>
            <div>{% include "hello.html" %}</div>
            <div>{{runoob|safe}}</div>
        </body>
    </html>
    ```

- create hello.py in HelloWorld/HelloWorld/views
  hello.py:  

  ```python
  from django.http import HttpResponse
  from django.shortcuts import render


  def hello(request):
      return HttpResponse("Hello world ! ")

  def runoob(request):
      context = {}
      context['hello'] = 'Hello World ! '
      context['name'] = 'RUNOOB'
      context['person'] = {"name":"MY", "sex":"female", "age":"21"}
      context['runoob'] = "<a href='https://www.runoob.com/'>点击跳转</a>"
      return render(request, 'runoob.html', context)
  ```

  HttpResponse("Hello World ! ") will show Hello World ! in browser. equal a html file just have content of "Hello World ! "
  render(request, 'runoob.html', context) will render runoob.html will data from context. and the detail of how to render the html can be found in the Django office website.

- modify urls.py.  
  modify urls.py, to create the link between the URLs and the views.
  urls.py:

    ```python
    from django.contrib import admin
    from django.urls import path

    from .views import hello, testdb

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('hello/', hello.hello),
        path('runoob/', hello.runoob),
    ]
    ```

  launch project, and visit 127.0.0.1:8080/hello and 127.0.0.1:8080/runoob.

### model

- model  
  to connect database, APP is required. use command:  
  django-admin.py startapp App_TestModel  
  this will create an app named App_TestModel. the folder in HelloWorld  

- create database runoob  
  install mysqlclient via: pip install mysqlclient
  
- modify setting.py in HelloWorld/HelloWorld
  setting.py

    ```python
    # some code
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'App_TestModel',
    ]
    # some code
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'runoob',  # database used
            'HOST': '127.0.0.1',  # server address
            'PORT': serverport,
            'USER': 'username',
            'PASSWORD': 'password',
            'OPTIONS': {
                'autocommit': True,
            }
        }
    }
    # some code
    ```

- modify models.py in HelloWorld/App_TestModel
  models.py:

    ```python
    from django.db import models

    # Create your models here.

    class Test(models.Model):  # table name in server is Test
        name = models.CharField(max_length=20)
        # name is the files in table. data type is CharField(like varchar),  
        # max_length is the limitation of length.

    ```

- run commands
  
  1. python manage.py migrate   # create tables struct
  2. python manage.py makemigrations App_TestModel  # tell Django models has changed.
  3. python manage.py migrate App_TestModel   # create tables struct from App_TestModel

  when error occurred, check the log and modify.

- test connection
  add four records to runoob.app_testmodel_test.
  
  1. create testdb.py in HelloWorld/HelloWorld/views
  2. modify urls.py
  3. look 127.0.0.1:8080/testdb

    ```python
    # testdb.py:
    def testdb(request):
    response = ""
    response1 = ""

    result_all = Test.objects.all()  # return datatype QuerySet
    response += "<p>1.Test.objects.all()</p>"
    for var in result_all:
        response += "<p>"+var.name+"</p><br/>"

    response2 = Test.objects.filter(id=1)  # return datatype QuerySet
    response += "<p>2.Test.objects.filter(id=1)</p>"
    for var in response2:
        response += "<p>"+var.name+"</p><br/>"

    response3 = Test.objects.get(id=1)  # return a data
    response += "<p>3.Test.objects.get(id=1)</p>"
    response += "<p>"+response3.name+"</p><br/>"

    response4 = Test.objects.order_by("id")  # return QuerySet
    response += "<p>4.Test.objects.order_by('id')</p>"
    for var in response4:
        response += "<p>"+var.name+"</p><br/>"

    response5 = Test.objects.order_by('name')[0:2]  # return QuerySet
    response += "<p>5.Test.objects.order_by('name')[0:2]</p>"
    for var in response5:
        response += "<p>"+var.name+"</p><br/>"

    response6 = Test.objects.filter(name="runoob").order_by('id')  # return QuerySet
    response += "<p>6.Test.objects.filter(name='runoob').order_by('id')</p>"
    for var in response6:
        response += "<p>"+var.name+"</p><br/>"

    responseu = Test.objects.get(id=2)  # return a data
    response += "<p>before update</p>"
    response += "<p>"+responseu.name+"</p><br/>"
    responseu.name = "Baidu"
    responseu.save()
    testu = Test.objects.get(id=2)  # return a data
    response += "<p>after update</p>"
    response += "<p>"+testu.name+"</p><br/>"

    return HttpResponse(response)
    ```

    ```python
    # urls.py:
    from django.contrib import admin
    from django.urls import path

    from .views import hello, testdb

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('hello/', hello.hello),
        path('runoob/', hello.runoob),
        path('testdb/', testdb.testdb)
        # re_path(r'\w*hello\w*', views.hello),
    ]
    ```
