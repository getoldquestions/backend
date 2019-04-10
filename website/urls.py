from django.urls import path
from . import views
from .views import message, FileCreate, FilesView,FilesDetailView,FileDelete,questionsView, semesterView, semdetailView

urlpatterns = [
    path('',views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('message/', message.as_view(), name="message"),
    path('file/add', FileCreate.as_view(), name='add-file'),
    path('files/', FilesView.as_view(), name="files-view"),
    path('files/<int:pk>/',FilesDetailView.as_view(), name='detail'),   
    path('files/<int:pk>/delete',FileDelete.as_view(), name='delete-file'),
    path('plus2', views.plus2, name="plus-2"),
    path('questions+2/', questionsView.as_view(), name="questions+2"),
    path('semester', semesterView.as_view(), name="semester"),
    path('detail/',views.semdetailView, name='sem-detail'), 

]