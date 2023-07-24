from django.urls import path,include 
from userstorygeneration import views



urlpatterns=[
    path('api/features',views.feature_post),
    path('api/story',views.story_post)
]