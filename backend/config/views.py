from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
from ticket.forms import TicketForm


@login_required(login_url="loginpage")
def indexPage(request):
    user_tickets = Ticket.objects.filter(user = request.user)
    ticketform = TicketForm()

    if request.method == 'POST':
        ticketform = TicketForm(request.POST)
        if ticketform.is_valid():
            ticket = Ticket()
            ticket.subject = ticketform.cleaned_data['subject']
            ticket.message = ticketform.cleaned_data['message']
            ticket.user = request.user
            ticket.status = 'new'
            ticket.save()

    return render(request, 'index.html', context={'tickets': user_tickets, 'ticketform': ticketform})

def logoutView(request):
    logout(request)
    return redirect('loginpage')

def loginPage(request):
    form = LoginForm()
    message = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message = 'Login nem sikerült'

    return render(request, 'login.html', context={'loginform': form, 'message': message})