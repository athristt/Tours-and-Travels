from django.db import models

# Create your models here.
# Each model maps to a single table in a database

# declaring a STATUS tuple to manage the availability of a tour package
STATUS = (
    (0, "UnPublish"),
    (1, "Publish")
)

class Packages(models.Model): 
    # define different fields/columns for package
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    days = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "images/")
    price = models.CharField(max_length=50)
    trip_diff = models.CharField(max_length=50)
    trip_style = models.CharField(max_length=50)
    transport = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    accommodation = models.CharField(max_length=50)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0) #Default= 0 means that the package is unavailable

    def __str__(self):
        return self.title



# model for contact form

class Form(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField(blank=True,unique=True)
    ephone = models.IntegerField(blank=True,unique=True)
    package = models.CharField(max_length=20)
    pickupdetails = models.TextField(max_length=30)

    def __str__(self):
        return self.fname


# model for guides

class Guide(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to = "images/")
    title1 = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    skills = models.CharField(max_length=250)

class  Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)



# by default it will order by id but now we update by the recent date automatically
    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
    



# review form model
class Reviews(models.Model):
    fname = models.CharField(max_length=30, null=True)
    lname = models.CharField(max_length=20,null=True)
    email = models.EmailField()
    package = models.CharField(max_length=50,null=True)
    review_title = models.CharField(max_length=100,null=True)
    #auto adds date when user writes a review
    date = models.DateTimeField(auto_now_add=True)
    reviewdetails = models.TextField(max_length=900,null=True)

    def __str__(self):
        return self.review_title  
