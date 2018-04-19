from django.db import models

# Create your models here.
class register(models.Model):
      uname=models.CharField(max_length=100,unique=True)
      name=models.CharField(max_length=100)
      pwd=models.CharField(max_length=100)
      mobile=models.CharField(max_length=100)
      email=models.EmailField(max_length=100)
      question=models.CharField(max_length=100,default="")
      answer=models.CharField(max_length=100,default="")

      def __unicode__(self):
            return self.uname

class blog_post1(models.Model):
      bname = models.CharField(max_length=100)
      blog = models.TextField(default="")
      author = models.CharField(max_length=100, default="")
      username = models.CharField(max_length=100, default="")


      def __unicode__(self):
            return self.bname

class comment(models.Model):
      blog=models.ForeignKey(blog_post1,on_delete=models.CASCADE)
      comment=models.CharField(max_length=100)


