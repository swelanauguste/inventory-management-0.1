from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, UpdateView

from .forms import ProfileUpdateForm
from .models import Profile, User


@login_required
def profile_redirect(request):
    return redirect("profile", slug=request.user.profile.slug)


# class HomeView(LoginRequiredMixin, TemplateView):
#     template_name = "home.html"


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    success_message = "Updated"