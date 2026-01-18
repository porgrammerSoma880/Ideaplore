

"""
The URL Configuration file
for the app-level directory
"""

# import essentials
from django.urls import path      # to dispatch the URL Patterns
from .views import homepage_view  # to patch-up its URL Pattern







# now dispatch the URL Patterns as follows
urlpatterns = [

              path("", homepage_view, name="homepage")  # path for the Homepage View


              ]



