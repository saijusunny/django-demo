from django import views
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('about/', views.about, name='about'),
    path('students', views.student, name='student'),
    path('add_student/', views.add_student, name="add_student"),
    path('course1', views.course1, name='course1'),
    path('courses', views.courses, name='courses'),
    path('student1', views.student1, name='student1'),
    path('add_course', views.add_course, name='add_course'),
    path('show', views.show, name='show'),
    # path('edit', views.edit, name='edit'),
    # path('delete_product/<int:pk>', views.delete_product, name='delete_product'),
    # path('edit_details/<int:pk>', views.edit_details, name='edit_details'),
    
    #login Section
    path('usercreate/', views.usercreate, name='usercreate'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),

    
]