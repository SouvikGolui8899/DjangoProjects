## README

## Django Commands

```
pip3 install Django==4.1

django-admin startproject <project_name> .

python manage.py startapp <app_name>

ptyhon manage.py runserver 8000
```

```
python manage.py shell

>>> from blog.models import Post
>>> from django.contrib.auth.models import User

>>> user = User.objects.create_user('sgolui', 'sgolui@gmail.com', 'password')
>>> user.save()
>>> User.objects.all()
<QuerySet [<User: sgolui>]>
>>> User.objects.all().first()
<User: sgolui>
>>> post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
>>> post_1.save()
>>> post_2 = Post(title='Blog 2', content='Second Post Content!', author=user)
>>> post_2.save()

>>> user.post_set.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
```