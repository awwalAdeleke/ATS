from django.http.response import HttpResponse

def home(request, username = 'User'):
    return HttpResponse(f"Welcome,{username} You have successfully hit home!")