from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name= 'dashboard' ),
    path('render_posts', views.render_posts, name= 'render_posts' ),
]