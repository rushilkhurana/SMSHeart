
#Documentation :
##Index:
    1.	Installation 
    3.	Project setup
    4.	Fill out the setting
    5.  Setup the views and Url link
    6.	Build the html



##Installation Django to your computer (Mac)
    1. Make sure you have Python 2.7 or latest version in your computer system, to check your python version from Terminal type <pre><code>python --version</code></pre>. It would be better to create a virtual environment, usually we use <code>virtaulenv</code> and <code>pip</code>(a python package setup tool.)
    2. Create your own virtual environment, you can using <code>[sudo] pip install virtualenv</code>, then type <code>virtualenv ENV</code> to create the environment inside 'ENV' folder. 
    3. Active your virtual environment you can go to 'ENV' folder <code>cd ENV</code>, and type 'bin/activate' from your Terminal.
    4. Install the latest version of Django <code>pip install django</code>

##Project Setup
    1. Setup the project from virtual environment, type 
    <code>django-admin.py startproject smsHeart</code>. So now we create a project, called 'smsHeart'
    2. Then type <code>ls</code>, you will found inside 'smsHeart' folder, there are 'manage.py' and another 'smsHeart' folder inside.This 'manage.py' is in the root of your Django project
    3. Run developement server to test everything is correct, type <code>python manage.py runserver</code> in your Django project root folder. Then go to your browser and type 'localhost:8000/' to test the development app. It should display 'It worked' inside the webpage. To stop the server, from Terminal press CTRL+C.
    4. Then we want to setup basic database, type 'python manage.py syncdb'. You will be asked to create the superuser, if you don't have one, create one (type 'yes'). Creat your username, email address and password. Then type <code>python manage.py syncdb</code> again to install the table.
    5. Now start server again <code>python manage.py runserver</code>, and go to the 'localhost:8000/admin', you will able to access the admin page by using the username and password your just created.
    6. Inside the admin page, you can add more user and groups. (This page is not for normal user, only for admin user)

##Fill out the setting
    1. Go to the 'smsHeart' folder inside the Django root folder. Edit the 'setting.py'. 
    2. First you want to make sure you are in the Debug mode, so inside 'setting.py' <code>DEBUG = True TEMPLATE_DEBUG = True</code>. Then you want to add your project name to the last nine of <code>INSTALLED_APPS =(...,smsHeart)</code> part.
    3. Database part, you can select different database system. In my example, I'm using 'sqlite3', I'm adding 
```
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         }
        }
```
    4. Setup the static file and directory. So the static files are linked with 
```
        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/1.7/howto/static-files/
        STATIC_URL = '/static/'
        # Template location
        TEMPLATE_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
        )
```
    5. Additonal setup about timezone, lanuage, etc
```
        # Internationalization
        # https://docs.djangoproject.com/en/1.7/topics/i18n/
        LANGUAGE_CODE = 'en-us'
        TIME_ZONE = 'EDT'
        USE_I18N = True
        USE_L10N = True
        USE_TZ = True
```

##Setup the views and URL link
    1. Inside 'smsHeart' app folder, there is a file called 'urls.py'. Now we need to edit this part in order to get the server link work.
    2. Now our app only have 1 sub-dir link, which is /admin and we want to add homepage view by adding
```
        from django.conf.urls import patterns, include, url
        from django.contrib import admin

        urlpatterns = patterns('',
        # Home page view Examples:
         url(r'^$', 'smsHeart.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),

        url(r'^admin/', include(admin.site.urls)),
        )
```
    So when you go to browser and type 'localhost:8080/home' it will direct you to the home page.
    3. Now you need to setup the view file, if the current folder(smsHeart/smsHeart) don't have one, create one called 'views.py'. And add following code:
```
        from django.shortcuts import render, render_to_response, RequestContext
        # Create your views here.
        # We create a 'PatientForm' by improt the 'forms' model from Django
        from .forms import PatientForm

        def home(request):
        # POST method
        form = PatientForm(request.POST or None)
        # Checking the form is valid or not
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save();
        # The page will render the info from 'patientInfo.html' page
        return render_to_response("patientInfo.html",
                                  locals(),
                                  context_instance=RequestContext(request))
```
    4. Since we are creating a form and taking the form entries from out app, so we need to create a 'forms.py' taking care the the form entries that coming from html part.
    5. Now we need to take those datafileds from html form entries to database. So inside 'model.py'(if it don't have, create one). Add the following code, will take the data entries
```
    #importing library and smart unicode encoding
    from django.db import models
    from django.utils.encoding import smart_unicode

    # Create your models here.
    # In this models, there are first name, last name, email address, entry timestamp and updated timestamp field.
    class smsHeart(models.Model):
      first_name = models.CharField(max_length=120, null=True, blank=True)
      last_name = models.CharField(max_length=120, null=True, blank=True)
      email = models.EmailField()
      timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
      updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __unicode__(self):
        return smart_unicode(self.email)
```

##Setup your html page
    1. In Django all html page can be put inside 'static/Template' folder. You can define your 'static/Template' folder root from 'setting.py' and then put your html file inside the Template folder. In our case, we have 'patientInfo.html'







