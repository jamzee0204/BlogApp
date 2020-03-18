from django.db import models

# Create your models here.


# class User(models.Model):
#
#     """    This Model stores Info of Blog Application User    """
#
#     email = models.EmailField(max_length=50)
#     password = models.CharField(max_length=10)
#     created = models.DateTimeField(auto_now_add=True)


class BlogPost(models.Model):

    """    This model will store all diffrent Blog Posted by different Users    """

    # blogger = models.ForeignKey(User, related_name='blog_post', on_delete=models.CASCADE)
    blogger = models.ForeignKey('auth.User', related_name='blog_post', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)


class BlogComment(models.Model):

    """    This model will store Comments on Blog Post"""

    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
