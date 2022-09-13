## README

$ django-admin startproject mysite .

$ python manage.py startapp polls

To see the SQLs generated

$ python manage.py sqlmigrate polls 0001

Whenever you change your model.py

'''
python manage.py makemigrations

python manage.py migrate
'''

$ python manage.py createsuperuser

1. Create an App named 'Blog'

2. Add 'Blog' to your Django Project

3. Create a Model named Article.

4. Run Migrations.

5. Create a ModelForm for Article

6. Create `article_list.html` & `article_detail.html` Template

7. Add Article Model to the Admin.

8. Save a new Article object in the Admin.

Confused? Start here: https://kirr.co/9ypik6