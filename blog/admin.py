from django.contrib import admin

# Register your models here.


# import essentials
from .models import Post



class PostAdmin(admin.ModelAdmin):
    """
    class for the Customized Adminstration Page
    for our Post Model
    """

    # specify the model
    model = Post

    # specify the fields to display
    list_display = ("title",
                    "author",
                    "body")
    




# and finally register the Post model along with its Customized Admin Page on the 
# default Django Adminstration Page
admin.site.register(Post, PostAdmin)






