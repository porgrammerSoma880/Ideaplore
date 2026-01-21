from django.db import models

# Create your models here.

from django.urls import reverse




class Post(models.Model):
    """
    class for the Blog Posts Model
    """

    # field for the post title, with a maximum character length of 200 chars
    title = models.CharField(max_length=200)
 
    # an author field for the blog post, refering as the foreign key of the default auth.User model
    # thus, every user in the database can be the author of blog posts
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
                                            # in case the user object is deleted, 
                                            # then the blog posts related to it, in the database,
                                            # will be also deleted as well


    # field for the blog post contents with an unlimited character limit
    body = models.TextField()





    def __str__(self):
        """
        additional method to display
        the object in a human-readable format;
        as best practices
        """

        # return the first 50 Chars of the Blog Post title, ending with three-dots;
        # following a standard approach

        return f"{self.title[:50]}..."




    def get_absolute_url(self):
        """
        method for getting the primary key for individual
        blog post pages 
        """

        return reverse('post_detail_page', kwargs={"pk":self.pk})



