
from urllib.request import Request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout # visable pages using django login session method
from  django.contrib.auth.decorators import login_required
from app1.models import course
from app1.models import student



def index(request):
    return render(request, 'index.html')

@login_required(login_url='adminlogin')
def students(request):
    return render(request,'student.html')


@login_required(login_url='adminlogin')
def courses(request):
    return render(request,'course.html')

def signup(request):
    return render(request, 'signup.html')

def loginpage(request):
    return render(request, 'login.html')

#this function is login visable pages using login session method
@login_required(login_url='adminlogin')
def about(request):
    return render(request, 'about.html')


#this function is login visable pages using session method
# def about(request):
#     if 'uid' in request.session:
#         return render(request, 'about.html')
#     return render(request, 'login.html')


# #this function is login visable pages using session method
# def about(request):
#     if 'uid' in request.session:
#         return render(request, 'about.html')
#     return render(request, 'login.html')

#this function is login visable pages using django login session method
# def about(request):
#     if request.user.is_authenticated:
#         return render(request, 'about.html')
#     return render(request, 'login.html')



#signup page
def usercreate(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpassword']
        email=request.POST['email']

        if password==cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This Username Is Already Exists!!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=username,
                    password=password,
                    email=email,
                )
                user.save()
        else:
            messages.info(request, 'Password doesnot match!!!!!')
            return redirect('signup')
        return redirect('adminlogin')
    else:
        return render(request, 'signup.html')

#login page
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # request.session['uid'] = user.id #visable pages using session method
        if user is not None:
            # login(request, user) #this function is login visable pages using django login session method
            auth.login(request, user)
            messages.info(request, f'Welcome {username}')#pass users name to welcome page
            return redirect('about')
        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')



# logoutpage
@login_required(login_url='adminlogin') #login  session method
def adminlogout(request):
    # if request.user.is_authenticated: # visable pages using django login session method
    #request.session['uid']= '' #visable pages using session method
    auth.logout(request)
    return redirect('index')

@login_required(login_url='adminlogin')
def add_course(request):
    if request.method== 'POST':
        cors=request.POST['course']
        cfee=request.POST['fees']
        crs=course()
        crs.course_name=cors
        crs.fee=cfee
        crs.save()
        return redirect('student1')
    
# add student functions
@login_required(login_url='adminlogin')
def add_student(request):
    if request.method== 'POST':
        name=request.POST['name']
        address=request.POST['addr']
        dob=request.POST['age']
        join=request.POST['date']
        sel1=request.POST['sel']
        course1= course.objects.get(id=sel1)
        std=student(
            std_name=name,
            std_address=address,
            std_age=dob,
            join_date=join,
            course=course1)
        std.save()
        return redirect('show')
    return render(request, 'student.html')


@login_required(login_url='adminlogin')
def course1(request):
    uid=User.objects.get(id=request.session['uid'])
    return render(Request, 'course.html', {'uid':uid})


@login_required(login_url='adminlogin')
def student1(request):
    courses=course.objects.all()
    context={'courses':courses}
    return render(request,'student.html', context)

@login_required(login_url='adminlogin') 
def show(request):
    result=student.objects.all()
    return render(request,'show_student.html', {'result':result})


# @login_required(login_url='adminlogin')
# def delete_product(request,pk):
#     products=student.objects.all(id=pk)
#     products.delete()
#     return redirect('show')
    
# @login_required(login_url='adminlogin')
# def edit_details(request,pk):
#     if request.method=='POST':
#         studs = student.objects.get(id=pk)
#         studs.std_name = request.POST.get('name')
#         studs.std_address = request.POST.get('addr')
#         studs.std_age = request.POST.get('age')
#         studs.join_date = request.POST.get('date')
#         studs.course = request.POST.get('sel')
#         studs.save()
#         return redirect('show')
#     return render(request, 'edit.html')

# @login_required(login_url='adminlogin')
# def edit(request,pk):
#     stud=student.objects.get(id=pk)
#     return render(request,'edit.html', {'stud':stud})
    