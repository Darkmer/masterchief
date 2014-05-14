![CourseBuilder Logo](/CourseBuilder/static/images/logo.png) 
# CourseBuilder

**A modern course builder for a modern teacher**

CourseBuilder is a webapplication which allows teachers to dynamically and fluidly create Courses, Lessons, and Slides. Imagine a college professor putting their course on CourseBuilder. Each lecture would be a Lesson and each of those Lessons would contain the slides the professor went through in lecture.

Having all of this information online and easily accessible allows the students to catchup and easily review material. The professor can build courses as the year progresses since CourseBuilder is dynamic.

## Technologies
      
### Django 
Django is an extremly popular web framework written in python. It is based on the MVC design pattern and separates the views, models, and controllers in an intuitive and easy to use way. Django has a lot of documentation and makes for extremly powerful webapplications. We are using Django v 1.6.2 
[Check it out!](https://www.djangoproject.com/)
    
### MySQL
MySQL is one of many databases that Django supports. We went with MySQL because of its support and its power. One of the strongest modern database systems, MySQL fulfills all of our requirements and everyone here is familiar with its use. 
[Check it out!](http://www.mysql.com/)
    
### JavaScript    
JavaScript allows for a lot of the usability of the website. The dynamic in page slide show, the ability to update courses, lessons, and slides, and a lot of the other cool features are powered by the JavaScript. 
[Check it out!](http://www.w3schools.com/js/DEFAULT.asp)
    
## Development Specifics

### Waterfall Approach
The team selected waterfall due to the small size of the project, the fact that the requirements will not change much, and that the project does not have too much parallel work. Each section needs to be completed fully before development of the enxt section can begin. Waterfall just meshes well with the team.

### Version Control
The team has obviously chosen to use Github. If you are here I do not need to tell you why Github is so amazing. The team had a lot of experience in Github so the decision was unanimous. 

### Issue Tracking and Wiki
The team decided to use Github's tools for issue tracking and documentation. The issue tracker is just very easy to use and simple. It also allows for assigning issues, tagging issues, and attaching those issues to milestones. Such a convient system that is attached to the repository is too good to pass up. Feel free to go explore that section to get an idea of how useful this Github issue tracker is.

## Installing

### LINUX INSTALL INSTRUCTIONS

* Python comes installed on most current linux distributions. If it is not installed on your distribution (try “python” in the temrinal and see if the command is recognized) then go to https://www.python.org/download/ and find the correct release for your distribution

* Install PIP, an extremely easy to use and popular python manager:

```
sudo apt-get install python-pip
```

* Install Django, the web server python library we will be using:

```
sudo pip install django
```

* Navigate to the home directory, clone our repository and then navigate into the repository:

```
cd ~
git clone https://github.com/Darkmer/masterchief.git
cd masterchief/
```

* We are almost there. This folder contains everything we will need to run the server. First we need to fix any inconsistencies with the local database and the database we expect to have up and running. Let’s sync the database:

```
python manage.py syncdb
```

* With the database synced we can now start the Django Server:

```
python manage.py runserver
```

* The server will tell you that it is up and running. Leave it running in the terminal and go to your favorite browser. Point the browser at localhost:8000/ and you will see the web application up and running. Feel free to start playing around with this wonderful application.


