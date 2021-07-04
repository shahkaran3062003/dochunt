from django.shortcuts import redirect, render
from .models import update
from random import choice
# Create your views here.


def home(request):
    data = update.objects.all()
    sent = ['There is no elevator to success. You have to take the stairs.', 'Success is the sum of small efforts, repeated day-in and day-out.', 'Success consists of going from failure to failure without loss of enthusiasm.',
            'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.', 'Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.', 'There are far, far better things ahead than any we leave behind.']
    pass_sent = choice(sent)
    return render(request, "update_img.html", {'data': data, 'sent_pass': pass_sent})
