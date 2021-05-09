from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, UpdateProfileForm  # , AccountUpdateForm
from django.contrib.auth import views as auth_view
# Create your views here.
from account.models import Account

from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request,'account/home.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form

    else: #GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')



def login_view(request):
    context={}

    user=request.user
    # if user.is_authenticated:
    #     return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("index")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "account/login.html", context)

# def profile(request):
#     return render(request,'account/profile.html')

def forgetPass(request):
    email=None
    forget_pass_view=auth_view.PasswordResetView.as_view(
        template_name='account/password_reset.html',


        initial={
            # 'emai,
        }
    )
    if request.method=="POST":
        email = request.POST.get('email')
        print(email)
        try:
            Account.objects.get(email=email)
        except ObjectDoesNotExist:
            messages.warning(request,f"Sorry Your Account Doesn't exist please contact your class cr or admin")
            redirect('contact_us')

    return forget_pass_view(request)

@login_required
def updateProfile(request):
    context={
        'user':request.user
    }
    form=UpdateProfileForm()
    if request.POST:
        form=UpdateProfileForm(request.POST or None,request.FILES or None,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile is updated successfully")
            context['success_message'] = "Updated"
    else:
        form=UpdateProfileForm(
            initial={
                "username":request.user.username,
                "first_name":request.user.first_name,
                "last_name":request.user.last_name,
                "branch": request.user.branch,
                "year": request.user.year,

            }
        )
    context['form'] = form

    return render(request,'account/profile.html',context)
