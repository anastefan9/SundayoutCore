"""
"""

from django.urls import re_path
from . import views

urlpatterns = [
   re_path('login', views.login),
   re_path('signup', views.signup),
   re_path('test_token', views.test_token),
   re_path('fetch_businesses_data', views.fetch_businesses_data)
]

# we want to map those views to certain routes with our urls

# now we have an api for login, signup, and test_token

# whenever we make a post request to any of the POST requests from the views, it will return us an empty response object