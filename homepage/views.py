from django.contrib import auth
from login_reg.models import collage
from django.shortcuts import render
from django.contrib.auth import get_user
from updates_with_img.models import update
from random import choice
# Create your views here.


def home(request):
    data = update.objects.all()
    u = get_user(request)
    pass1 = ""
    sent = ['There is no elevator to success. You have to take the stairs.', 'Success is the sum of small efforts, repeated day-in and day-out.', 'Success consists of going from failure to failure without loss of enthusiasm.',
            'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.', 'Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.', 'There are far, far better things ahead than any we leave behind.']
    sent_pass = choice(sent)
    if request.user.is_authenticated:
        d_join = str(u.date_joined).split('.')[0].split(' ')
        l_login = str(u.last_login).split('.')[0].split(' ')
        c = collage.objects.filter(user_name=u)
        if str(c) != '<QuerySet []>':
            if str(c[0].coll_type) == "DN":
                pass1 = "DN"
            elif str(c[0].coll_type) == "MB":
                pass1 = "MB"
        if (d_join[0] == l_login[0]) and ((int(d_join[1].split(':')[1])) == (int(l_login[1].split(':')[1]))):
            into = True
        else:
            into = False
        auth.login(request, u)
        print(into)
        return render(request, 'index.html', {'data': data, "pass": pass1, 'sentense': sent_pass, 'intor': into})

    else:
        return render(request, 'index.html', {'data': data, "pass": pass1, 'sentense': sent_pass})
