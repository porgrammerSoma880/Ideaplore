from django.shortcuts import render

# Create your views here.




# import essentials
from .models import Post  # to use its data in our views
from django.views.generic import ListView, DetailView





class HomepageView(ListView):
    """
    class for the Homepage View Listing all the
    blog posts
    """

    # specify the model
    model = Post

    # specify the template name
    template_name = "homepage.html"






class PostDetailView(DetailView):
    """
    class for the Individual
    Blog Post Pages
    """

    # specify the model
    model = Post

    # specify the template name
    template_name = "post_detail.html"


