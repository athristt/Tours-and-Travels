from django.contrib import admin
from .models import Packages # importing Packages from models
from.models import Form
from .models import Guide
from .models import Post
from .models import Comment
from .models import Reviews


# Register your models here.

#registering the model Packages

admin.site.register(Packages)
admin.site.register(Form)
admin.site.register(Guide)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reviews)