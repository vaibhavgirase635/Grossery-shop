from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
# Create your views here.

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(full_name=uname,email=email,password=pass1,confirm_password=pass2)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')



def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render (request,'login.html')

@login_required
def index(request):
    return render(request,'index.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request,'about.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def faqs(request):
    return render(request,'faqs.html')

def help(request):
    return render(request,'help.html')

def icons(request):
    return render(request,'icons.html')


def payment(request):
    return render(request,'payment.html')

def privacy(request):
    return render(request,'privacy.html')

def product(request):
    return render(request,'product.html')

def privacy(request):
    return render(request,'privacy.html')

def product2(request):
    return render(request,'product2.html')

def single(request):
    return render(request,'single.html')

def single2(request):
    return render(request,'single2.html')

def terms(request):
    return render(request,'terms.html')

def typography(request):
    return render(request,'typography.html')