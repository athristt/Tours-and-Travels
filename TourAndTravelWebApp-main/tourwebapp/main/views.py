from django.shortcuts import render, redirect
from .models import Packages
from .models import Form
from .models import Guide
from .models import Post
from .models import Reviews
from .forms import CommentForm
from django.http import HttpResponseRedirect

# Create your views here.

# stores different views for the application HTTP requests


def index(request):                                                        
    packages = Packages.objects.all()[3:9] # show only 6 packages from the database as best selling tour packages
    reviews = Reviews.objects.all()
    return render(request, "main/home.html", {"packages":packages, "reviews":reviews})


def about(request):
    return render(request, "main/about.html" )

def FAQ(request):
    return render(request, "main/FAQ.html" )

def TermsandCondition(request):
    return render(request, "main/TermsandCondition.html" )

def blog(request):
    posts = Post.objects.all()
    return render(request, "main/blog.html", {"posts":posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':             #using if conditions to update the page if new commnets are submitted
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
            # return HttpResponseRedirect("/registered")
    else:
        form = CommentForm()



    return render(request, "main/post_detail.html", {'post':post, 'form': form,})


def package(request):
    packages = Packages.objects.all() 
    return render(request, "main/packages.html", {"packages":packages})

def guide(request):
    guide = Guide.objects.all() 
    return render(request, "main/guide.html", {"guide":guide})


#using the captured slug
def package_details(request,slug):
    package = Packages.objects.get(slug=slug) #using Django ORM to query database with .get(slug=slug) code
    return render(request, "main/package_detail.html",{"package":package})



#function base view for form

def form(request):
    packages = Packages.objects.all()
    if request.method=="POST":
        # create object for form
        form = Form()
        # first name attribute in the template is fname so .get(fname)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        ephone = request.POST.get('ephone')
        package = request.POST.get('package')
        pickupdetails = request.POST.get('pickupdetails')
        # save in form model
        form.fname= fname
        form.lname= lname
        form.email = email
        form.phone = phone
        form.ephone = ephone
        form.package = package
        form.pickupdetails = pickupdetails
        form.save()
        return HttpResponseRedirect("/registered")

    return render(request, "main/requestform.html",{"packages":packages} )


#after the booking form is filled a thankyou page is shown with the help of this view function
def thankyou(request):
    return render(request, "main/registered.html")



#function based view for review page
def review(request):
    #fetching the database object of packages
    packages = Packages.objects.all() 
    if request.method=="POST":
        # create object for review
        review = Reviews()
        # first name attribute in the template is fname so .get(fname)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        package = request.POST.get('package')
        review_title = request.POST.get('title')
        reviewdetails = request.POST.get('reviewdetails')
        # save in form model
        review.fname= fname
        review.lname= lname
        review.email = email
        review.package = package
        review.review_title = review_title
        review.reviewdetails = reviewdetails
        review.save()
        return HttpResponseRedirect("/reviewed")

    return render(request, "main/review.html",{"packages":packages} )


# for sucessful review post
def success(request):
    return render(request, "main/reviewsuccess.html")  