from django.http.response import HttpResponse

def home(request, username = 'user'):
    return HttpResponse(f"Welcome, {username}. You have successfully hit home!")