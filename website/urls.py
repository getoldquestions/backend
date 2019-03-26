from django.urls import path
from . import views
from .views import message, FileCreate, FilesView,FilesDetailView,FileDelete

urlpatterns = [
    path('',views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('message/', message.as_view(), name="message"),
    path('file/add', FileCreate.as_view(), name='add-file'),
    path('files/', FilesView.as_view(), name="files-view"),
    path('files/<int:pk>/',FilesDetailView.as_view(), name='detail'),   
    path('files/<int:pk>/delete',FileDelete.as_view(), name='delete-file'),

]