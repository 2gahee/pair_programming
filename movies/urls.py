from django.urls import path
from . import views
# from .views import movie_search

urlpatterns = [
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/<int:actor_pk>/', views.actor_detail, name='actor_detail'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('movies/<int:movie_pk>/reviews/', views.create_review, name='create_review'),
    path('movies/search/', views.movie_search, name='movie_search'),
]