from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# Create your views here.
from user.forms import *


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, "registration.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            print("succes")
            return redirect("sign-in")


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = LogInForm()
        return render(request, "signin.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LogInForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(request, username=u_name, password=pwd)
            if user.is_superuser:
                login(request, user)
                return redirect("admin-home")
            else:
                login(request, user)
                return redirect("user-home")
        else:
            return redirect("sign-up")


class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('sign-in')


class UserIndexView(ListView):
    model = UserRequest
    template_name = "user-index.html"
    context_object_name = "data"

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class AdminIndexView(ListView):
    model = UserRequest
    template_name = "admin-index.html"
    context_object_name = "data"


class CreateUserProfileView(View):
    def get(self, request, *args, **kwargs):
        form = UserProfileForm()
        return render(request, "add-profile.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            return redirect('user-home')
        else:
            return render(request, "add-profile.html", {"form": form})


class UserProfileView(DetailView):
    template_name = "view-profile.html"
    context_object_name = "data"
    model = UserProfile


class UpdateUserProfileView(UpdateView):
    form_class = UserProfileForm
    template_name = "update-profile.html"
    model = UserProfile

    def get_success_url(self):
        return reverse_lazy('profile-view', kwargs={'pk': self.request.user.profile.id})


class DeleteUserProfileView(SuccessMessageMixin, DeleteView):
    model = UserProfile
    success_url = reverse_lazy("user-home")
    template_name = "delete-profile.html"
    success_message = "Profile successfully deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class NewRequestView(View):
    def get(self, request, *args, **kwargs):
        form = RequestForm()
        return render(request, "new-request.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect('user-home')
        else:
            return render(request, "new-request.html", {"form": form})


class DetailRequestView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = UserRequest.objects.get(id=id)
        return render(request, "view-request.html", {"data": qs})


class DetailRequestView(DetailView):
    template_name = "view-request.html"
    context_object_name = "data"
    model = UserRequest


class DeleteRequestView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        UserRequest.objects.get(id=id).delete()
        return redirect('user-home')


class UpdateRequestView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = UserRequest.objects.get(id=id)
        form = RequestForm(instance=qs)
        return render(request, "edit-request.html", {"form": form, "data": qs})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = UserRequest.objects.get(id=id)
        form = RequestForm(request.POST, request.FILES, instance=qs)
        if form.is_valid():
            form.save()
            return redirect('view-request', pk=qs.pk)
        else:
            return render(request, "edit-request.html", {"form": form})


class UserListView(ListView):
    model = UserProfile
    template_name = "list-user.html"
    context_object_name = "data"


class UserDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        User.objects.get(id=id).delete()
        return redirect("admin-home")


class AdminUpdateRequestView(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        value = request.POST.get("status")
        UserRequest.objects.filter(id=id).update(status=value)
        return redirect ('admin-home')

class AdminDetailRequestView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = UserRequest.objects.get(id=id)
        return render(request, "admin-edit.html", {"data": qs})