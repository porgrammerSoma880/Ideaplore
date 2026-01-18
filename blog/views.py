from django.shortcuts import render

# Create your views here.




# import essentials
from .models import Post  # to use its data in our views




def homepage_view(req):
    """
    function for the homepage view
    """

    # get every blog post object from the model by using the all() QuerySet
    blog_posts = Post.objects.all()


    # now render the HTTP Response, along with the HTML Template;
    # and the extracted model data as the context variable, as follows
    return render(req, "homepage.html", {"posts": blog_posts})







