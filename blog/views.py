from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Film, Entry
from .forms import MessageForm

def index(request):
    context = {'message_form': MessageForm()}
    return render(request, 'blog/cover.html', context)

def message(request):
    """posting the message"""
    if request.method == 'POST':
        # process the form data
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to the home page
            messages.add_message(request, messages.SUCCESS, 'Message sent successfully!')
            return HttpResponseRedirect(reverse("blog:index"))

def reviews(request):
    """show all the films."""
    reviews = Entry.objects.all().order_by('date_added')
    context = {'reviews':reviews}
    return render(request, 'blog/reviews.html', context)
