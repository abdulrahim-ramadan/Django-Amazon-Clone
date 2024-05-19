from django.shortcuts import render , redirect

# Create your views here.
from products.models import Product , Brand , Review
from orders.models import Order
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .models import Profile
from .forms import SignupForm

from django.conf import settings


def dashboard(request):

    products = Product.objects.all().count() #-----> dasboard data
    brands = Brand.objects.all().count()
    users = User.objects.all().count()
    orders = Order.objects.all().count()
    review = Review.objects.all().count()


    new_products = Product.objects.filter(flag='New').count()
    feature_products = Product.objects.filter(flag='Feature').count()
    sale_products = Product.objects.filter(flag='Sale').count()

    return render(request,'accounts/dashboard.html',{
        'products':products,
        'brands':brands,
        'users':users,
        'orders':orders,    #-----> dasboard data
        'review':review,
        'new_products': new_products,
        'feature_products': feature_products,
        'sale_products': sale_products
        
    })

def signup(request):
    
    # create new user 
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid() :
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            
            # make user un active 
            user = form.save(commit=False)
            user.is_active = False
            
            form.save()  # create new user 
            
            # send user email 
            profile = Profile.objects.get(user__username=username)
            code = profile.code 

            send_mail(
                "Activate Your Account",
                f"Welcome {username}\nUse this code {code} to acitvate your account .",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            
            # redirect : activate 
            return redirect(f'/accounts/{username}/activate')
        
    else:
        form = SignupForm() 
    return render(request,'registration/signup.html',{'form':form})     


def user_activate(request,username):
    profile = Profile.objects.get(user__username=username)
    
    if request.method == 'POST':
        code = request.POST['code']
        if code == profile.code :
            profile.code = ''
            profile.save()
            
            # activate user 
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()
            
            return redirect('/accounts/login')
    return render(request,'registration/activate.html',{})
