from django.shortcuts import render


def chat_box(request, chat_box_name):
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})

# Create your views here.
