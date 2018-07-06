from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # Homepage(/music/)
    path('', views.IndexView.as_view(), name='index'),
    # Register User
    path('register/', views.UserFormView.as_view(), name='register'),
    # Id Find(/music/album_id/)
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # Create View
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    # Update View
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),
    # Delete View
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]
