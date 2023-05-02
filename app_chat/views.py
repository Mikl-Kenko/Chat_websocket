from django.shortcuts import render
 
 
def chat_views(request, *args, **kwargs):
    return render(request, "chat.html")
