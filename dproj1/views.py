from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from .models import Persondetails 
from django.http import HttpResponse, JsonResponse
from .models import Persondetails 
from django.urls import reverse
import re
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import Persondetails 
from django.http import HttpResponse
import re
import random
from django.core.mail import send_mail
from django.conf import settings
#from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from .models import Persondetails

class loginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('home1')  
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html') 
    
def generate_otp():
    return get_random_string(length=6, allowed_chars='0123456789')


class forgot_passwordView(View):
    def get(self, request):
        return render(request, 'forgot_password.html')

    def post(self, request):
        email = request.POST.get("email")
        try:
            user = Persondetails.objects.get(email=email)  
            otp = random.randint(100000, 999999)
            user.otp = otp
            user.save()
            send_mail(
                'Your OTP for Password Reset',
                f'Yah! Your OTP for resetting the password is: {otp}',
                settings.DEFAULT_FROM_EMAIL, 
                [email],
                fail_silently=False,
            )
            messages.success(request, "OTP has been sent to your email.")
            return redirect('reset_password')  
        except Persondetails.DoesNotExist:
            messages.error(request, "Email does not exist.")
            return render(request, 'forgot_password.html')
class reset_passwordView(View):
    def get(self, request):
        return render(request, 'reset_password.html')

    def post(self, request):
        email = request.session.get('email')
        entered_otp = request.POST.get("otp")
        new_password = request.POST.get("new_password")
        
        if entered_otp == request.session.get('otp'):
            try:
                user = Persondetails.objects.get(email=email)
                user.password = make_password(new_password)  
                user.save()
                messages.success(request, "Password reset successfully!")
                return redirect('login')  
            except Persondetails.DoesNotExist:
                messages.error(request, "User not found.")
        else:
            messages.error(request, "Invalid OTP. Please try again.")
        return render(request, 'reset_password.html')
class registerprocessView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if 'otp' in request.POST:  
            entered_otp = request.POST.get('otp')
            stored_otp = request.session.get('otp')
            
            if entered_otp != str(stored_otp):
                return render(request, 'register.html', {
                    'otp_error': "Invalid OTP. Please try again.",
                    'username': request.session.get('username', ''),
                    'email': request.session.get('email', ''),
                    'otp_sent': True, 
                })
            
            request.session['otp_verified'] = True
            return render(request, 'register.html', {
                'otp_verified': True,
                'otp_sent': True,  
                'username': request.session.get('username', ''),
                'email': request.session.get('email', ''),
            })

        elif 'password' in request.POST:  
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                return render(request, 'register.html', {
                    'otp_verified': True,
                    'otp_sent': True,
                    'username': request.session.get('username', ''),
                    'email': request.session.get('email', ''),
                    'error': 'Passwords do not match.',
                })
            new_user = Persondetails(
                username=request.session.get('username', ''),  
                email=request.session.get('email', ''),
                password=make_password(password),
            )
            new_user.save()

            messages.success(request, "Registration successful!")
            return redirect('login') 

        else:  
            username = request.POST.get('username', '').strip()  
            email = request.POST.get('email', '').strip() 
            errors = {
                'username_error': None,
                'email_error': None,
            }
            
            if username and not username.isalpha():
                errors['username_error'] = "Username should only contain letters."
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                errors['email_error'] = "Email must be a valid address."
            if username and Persondetails.objects.filter(username=username).exists():
                errors['username_error'] = "Username already exists."
            if Persondetails.objects.filter(email=email).exists():
                errors['email_error'] = "Email already exists."
            
            if any(errors.values()):
                return render(request, 'register.html', {
                    'errors': errors,
                    'username': username,
                    'email': email,
                })
            otp = random.randint(100000, 999999)
            send_mail(
                'Request to Login',
                f'Yah! User, we received a request to login and your OTP Code is {otp}.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            request.session['username'] = username if username else ''
            request.session['email'] = email
            request.session['otp'] = otp
            request.session['otp_sent'] = True

            return render(request, 'register.html', {
                'otp_sent': True,
                'username': username,
                'email': email,
            })
class home1View(LoginRequiredMixin, View):
    login_url = 'login' 
    redirect_field_name = 'redirect_to'

    def get(self, request):
        username = request.user.username
        profile_image = request.user.profile_image.url if request.user.profile_image else None
        return render(request, 'home1.html', {'username': username, 'profile_image': profile_image})


class changepasswordView(LoginRequiredMixin, View):
    login_url = '/login/' 

    def get(self, request):
        email = request.session.get('email') 
        return render(request, 'changepassword.html', {'email': email})

    def post(self, request):
        email = request.session.get('email') 
        old_password = request.POST.get('old-password')
        new_password = request.POST.get('new-password')
        confirm_password = request.POST.get('confirm-new-password')
        
        try:
            user = Persondetails.objects.get(email=email)
            if not check_password(old_password, user.password):
                messages.error(request, "Old password is incorrect.")
                return render(request, 'changepassword.html', {'email': email})
            if new_password != confirm_password:
                messages.error(request, "New password and confirm password do not match.")
                return render(request, 'changepassword.html', {'email': email})

            user.password = make_password(new_password)
            user.save()
            messages.success(request, "Password changed successfully!")
            return redirect('home1')  
        except Persondetails.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('login')
class profileView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            user_details = Persondetails.objects.get(email=request.user.email)
            return render(request, 'profile.html', {
                'user_profile': user_details,
                'username': request.user.username,
                'email': request.user.email,
            })
        except Persondetails.DoesNotExist:
            return JsonResponse({"status": False, "error": "User details not found."})

class editprofileView(LoginRequiredMixin, View):
    login_url = '/login/' 

    def get(self, request):
        try:
            user_details = Persondetails.objects.get(email=request.user.email)
            return render(request, 'editprofile.html', {
                'user_profile': user_details,
            })
        except Persondetails.DoesNotExist:
            return JsonResponse({"status": False, "error": "User details not found."})

    def post(self, request):
        try:
            user_details = Persondetails.objects.get(email=request.user.email)
            user_details.username = request.POST.get('username', '')  
            user_details.address = request.POST.get('address', '')
            user_details.city = request.POST.get('city', '')
            user_details.state = request.POST.get('state', '')
            user_details.postal_code = request.POST.get('postal_code', '')

            if 'profile_image' in request.FILES:
                user_details.profile_image = request.FILES['profile_image']

            user_details.save()
            return redirect('profile') 
        except Persondetails.DoesNotExist:
            return JsonResponse({"status": False, "error": "User details not found."})
        except Exception as e:
            return JsonResponse({"status": False, "error": str(e)})



class logoutView(View):
    def get(self, request):
        request.session.flush()  
        messages.success(request, "You have been logged out.")  
        return redirect('login') 

class aboutusView(View):
    def get(self, request):
        return render(request, 'aboutus.html')

class productView(View):
    def get(self,request):
        return render(request,'product.html')

class productsView(View):
    def get(self,request):
        return render(request,'products.html')

    
  

       

