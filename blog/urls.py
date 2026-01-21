

"""
The URL Configuration file
for the app-level directory
"""

# import essentials
from django.urls import path                      # to dispatch the URL Patterns
from .views import HomepageView, PostDetailView   # to patch-up its URL Pattern







# now dispatch the URL Patterns as follows
urlpatterns = [

              # path for the Homepage View
              path("", HomepageView.as_view(), name="homepage"),  

              # path for the individual Blog Post pages
              path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail_page")


              ]



