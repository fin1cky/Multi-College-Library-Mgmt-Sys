from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.forms import ValidationError
from library.models import College,Books
from .form import Student_Form, update_profile
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import User, Student,issue
from django.forms import forms

def register(request):
    return render(request, '../templates/register.html')

#class customer_register(CreateView):
    #model = User
    #form_class = Student_Form
    #template_name = '../templates/customer_register.html'

    #def form_valid(self, form):

        #user = form.save()

        #login(self.request, user)
        #return redirect('/')
def student_regview(request):
    context = {}
    if(request.POST):
        form = Student_Form(request.POST)

        if(form.is_valid()):


            user = form.save_data()
            login(request,user)
            return redirect('/student_home')
    else:
        form = Student_Form()

    return render(request,'../templates/customer_register.html',{'form':form})
def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                if(user.is_student):
                    return redirect('/accounts/student_home')
                else:
                    return redirect('/accounts/admin_home')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})
@login_required
def student_homeView(request):
    user = request.user
    books1 = issue.objects.filter(user=user)
    l = books1.values_list('book_id',flat=True)
    books = Books.objects.filter(Book_id__in=l)
    context = {
        'books': books

    }
    return render(request,'../templates/student_home.html',context)
def logout_view(request):
   logout(request)
   return redirect('/accounts/login')
def contact_us(request):
    return redirect('/accounts/contact')
def contact_view(request):
    return render(request,'../templates/contact.html')
def profile_btn(request):
    return redirect('/accounts/profile')
def profile(request):
    user = request.user
    student = Student.objects.get(user=user)
    context = {
        'user': user,
        'student': student
    }
    return render(request,'../templates/profile.html',context)
def edit(request):
    return redirect('/accounts/edit_profile')
def edit_view(request):
    if(request.POST):
        form = update_profile(request.POST)
        if(form.is_valid()):
            user = request.user
            student = Student.objects.get(user=user)
            if(form.cleaned_data.get('first_name')!=''):
                first_name = form.cleaned_data.get('first_name')
                student.first_name = first_name
            if(form.cleaned_data.get('last_name')!=''):
                last_name = form.cleaned_data.get('last_name')
                student.last_name = last_name
            if(form.cleaned_data.get('gender')!=None):
                gender = form.cleaned_data.get('gender')
                student.gender = gender
            if(form.cleaned_data.get('age')!=None):
                age = form.cleaned_data.get('age')
                student.age = age
            if(form.cleaned_data.get('phone_no')!=None):
                phone = form.cleaned_data.get('phone_no')
                student.phone_no = phone
            if(form.cleaned_data.get('email')!=''):

                email = form.cleaned_data.get('email')
                student.email = email

            if(form.cleaned_data.get('branch')!=''):
                branch = form.cleaned_data.get('branch')
                student.branch = branch
            student.save()
            return redirect('/accounts/profile')


    return render(request,'../templates/edit_view.html',{'form':update_profile()})
def return_book(request):
    return redirect('/accounts/return_book_page')
def return_book_page(request):
    user = request.user
    books1 = issue.objects.filter(user=user)
    l = books1.values_list('book_id', flat=True)
    books = Books.objects.filter(Book_id__in=l)
    context = {
        'books': books
    }
    if(request.POST):
        book_id = request.POST.get('optradio')
        book = Books.objects.get(Book_id=book_id)
        issue.objects.get(user=request.user,book=book).delete()
        return redirect('/accounts/student_home')
    return render(request,'../templates/return_book.html',context)
def add_book(request):
    return redirect('/accounts/add_book_page');