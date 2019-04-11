from django.urls import path
from . import views
from .views import (message, FileCreate, FilesView,FilesDetailView,FileDelete,questionsView,
                    semesterView, semdetailView, SubjectCreateView, QuestionsCreateView,
                     Science11q, Science12q, Commerce11q, Commerce12q,
                    Csit1q, Csit2q, Csit3q, Csit4q, Csit5q, Csit6q, Csit7q, Csit8q )

urlpatterns = [
    path('',views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('message/', message.as_view(), name="message"),

    path('file/add', FileCreate.as_view(), name='add-file'),
    path('file/add-sub', SubjectCreateView.as_view(), name='add-sub'),
    path('file/add-ques', QuestionsCreateView.as_view(), name='add-ques'),


    path('files/', FilesView.as_view(), name="files-view"),
    path('files/<int:pk>/',FilesDetailView.as_view(), name='detail'),   
    path('files/<int:pk>/delete',FileDelete.as_view(), name='delete-file'),
    path('plus2', views.plus2, name="plus-2"),
    path('questions+2/', questionsView.as_view(), name="questions+2"),
    path('semester', semesterView.as_view(), name="semester"),
    path('detail/',views.semdetailView, name='sem-detail'), 

    #url routes for +2 Science
    path('science-11/', Science11q.as_view(), name="science-11"),
    path('science-12/', Science12q.as_view(), name="science-12"),
    path('Commerce-11/', Commerce11q.as_view(), name="Commerce-11"),
    path('Commerce-12/', Commerce12q.as_view(), name="Commerce-12"),
    #url routes for CSIT
    path('csit-1/', Csit1q.as_view(), name="csit-1"),
    path('csit-2/', Csit2q.as_view(), name="csit-2"),
    path('csit-3/', Csit3q.as_view(), name="csit-3"),
    path('csit-4/', Csit4q.as_view(), name="csit-4"),
    path('csit-5/', Csit5q.as_view(), name="csit-5"),
    path('csit-6/', Csit6q.as_view(), name="csit-6"),
    path('csit-7/', Csit7q.as_view(), name="csit-7"),
    path('csit-8/', Csit8q.as_view(), name="csit-8"),

]