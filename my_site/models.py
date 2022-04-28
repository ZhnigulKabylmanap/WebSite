from django.db import models


class Tourist(models.Model):
    First_name = models.CharField(max_length=200)
    Last_Name= models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ""+ self.last_name


class Sport (models.Model):
    title = models.CharField(max_length=200)
    athlete=models.CharField(max_length=200)
    content = models.TextField(max_length=200)

    def __str__(self):
     return self.title + ""+ self.athlete + ""+ self.content


class Art(models.Model):
    title = models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    content = models.TextField(max_length=200)



    def __str__(self):
     return self.title + ""+ self.author + ""+ self.content




class Book(models.Model):
    name = models.CharField(max_length = 50)
    actor = models.CharField(max_length = 100)
    describe = models.TextField(max_length = 200)
    def __str__(self):
        return self.name +""+ self.actor +self.describe


class Posts(models.Model):
    title = models.CharField(max_length = 50,verbose_name="title")
    is_published = models.BooleanField(default=True,verbose_name="lecture10")



class Lab4(models.Model):
    name = models.CharField(max_length=10)
    Surname = models.CharField(max_length=10)
    age = models.IntegerField(verbose_name="Age")
    Address=models.CharField(max_length=18)
    Email = models.CharField(max_length=20)
    Password = models.CharField(max_length=8)
    is_published = models.BooleanField(verbose_name="Remember Password")

class Test(models.Model):
    def get_number(self):
        return 15