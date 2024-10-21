from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from PIL import Image
from io import BytesIO
from datetime import datetime 

# Create your models here.
class Board(models.Model):
    name =  models.CharField(max_length=50)
    description = models.TextField(max_length=50000) 

    def __str__(self):
        return self.name

    def count_posts(self):
        return Post.objects.filter(board=self.id).count()

def compress(image):    
    im = Image.open(image)   
    im_io = BytesIO()     
    im.save(im_io, "JPEG", quality=60)     
    new_image = File(im_io, name=f"{datetime.now()}.jpeg")    
    return new_image

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Judul",help_text="Maksimal 50 karakter")
    content = models.TextField(max_length=50000,verbose_name="Isi")
    date_created = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
    attachment = models.ImageField(upload_to="attachment",null=True,help_text="maksimal gambar berukuran 500kb",blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        if self.attachment:
            self.attachment = compress(self.attachment)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-date_created"]

class Comment(models.Model):
    comment = models.TextField(max_length=50000,verbose_name="Komentar")
    date_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_created"]

class Announcement(models.Model):
    title = models.CharField(max_length=200,verbose_name="Judul",help_text="Maksimal 50 karakter")
    content = models.TextField(max_length=50000,verbose_name="Isi")
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
