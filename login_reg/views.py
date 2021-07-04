from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import collage
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "incorect pass word or username",
                           extra_tags="inco")
            return redirect('login')
    else:
        return render(request, 'login.html')


def reg(request):
    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        Collage = request.POST['collage']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 != pass2:
            messages.error(request, "Incorrect password", extra_tags="pass")
        elif User.objects.filter(username=user).exists():
            messages.error(request, "user exiest", extra_tags="user")
        else:
            c_user = User.objects.create_user(
                username=user, email=email, password=pass1)
            c_user.save()
            coll = collage(
                user_name=c_user, coll_type=Collage)
            coll.save()
            messages.success(request, "account created", extra_tags="succ")
            auth.login(request, c_user)
            return redirect('/', karan=True)
    return render(request, 'reg.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
