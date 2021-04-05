from django.urls import path
from .import views
from accounts.views import (
     student_regview,
)
urlpatterns=[
     path('register/',views.register, name='register'),
     #path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('customer_register/',student_regview,name='customer_register'),
     path('login/',views.login_request, name='login'),
     path('student_home/',views.student_homeView,name ='student_home'),
     path('logout',views.logout_view,name='logout'),
     path('contact_us',views.contact_us,name='contact us'),
     path('contact/',views.contact_view,name='contact'),
     path('profile_btn',views.profile_btn,name='profile_btn'),
     path('profile/',views.profile,name='profile'),
     path('edit',views.edit,name='edit'),
     path('edit_profile/',views.edit_view,name='edit_profile'),
     path('return_book',views.return_book,name='return_book'),
     path('return_book_page/',views.return_book_page,name='return_book_page')
     ]