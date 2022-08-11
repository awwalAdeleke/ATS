from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import EditSettingForm, SignUpForm, PasswordChangingForm, ProfilePageForm
from theblog.models import Profile, Post

# Create your views here.

class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_profile_page.html"
    # success_url = reverse_lazy('show_profile_page')
    # fields = "__all__"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        posts = Post.objects.all()
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        context['posts'] = posts
        return context



class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
    # fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']




class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditSettingForm
    template_name = 'registration/edit_setting.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request,'registration/password_success.html',{})