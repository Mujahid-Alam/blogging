from statistics import mode
from django.db import models
from django.utils.html import format_html
# Create your models here.
# Category
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:50px; height:50px"; />'.format(self.image))
    
#POST
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()

    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Post/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:50px; height:50px"; />'.format(self.image))

# Comment
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    # post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    post = models.CharField(max_length=300)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)