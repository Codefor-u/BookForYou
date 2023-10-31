# accounts/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView,LogoutView
from django.urls import reverse_lazy
from .forms import SignupForm, LoginForm,UserUpdateForm,UserSearchForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from book.models import Book 



def index_view(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace with the URL to the user profile
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page or some other URL after login.
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    # Use Django's built-in LogoutView and set the next_page attribute
    return LogoutView.as_view(next_page=reverse_lazy('home'))(request)

# class CustomPasswordResetView(PasswordResetView):
#     template_name = 'registration/password_reset.html'
#     form_class = PasswordResetCustomForm
#     success_url = reverse_lazy('password_reset_done')

def user_profile(request, username):
    s_user = get_object_or_404(User, username=username)
    books = Book.objects.filter(user__username=username)  # Get the user's uploaded books
    return render(request, 'accounts/profile.html', {'s_user': s_user, 'books':books})

# def profile_view(request):
#     searched_user = None  # Initialize searched_user to None

#     if request.method == 'GET':
#         search_query = request.GET.get('query')  # Get the search query from the URL

#         # Perform the search query on your users and get the first result
#         if search_query:
#             searched_user = User.objects.filter(username__icontains=search_query)
#             print(searched_user)

#     return render(request, 'accounts/profile.html', {'searched_user': searched_user})

def user_search(request):
    form = UserSearchForm(request.GET)
    users = []

    if form.is_valid():
        query = form.cleaned_data['query']
        users = User.objects.filter(username__icontains=query)

    return render(request, 'accounts/user_search.html', {'form': form, 'users': users})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return redirect('home')  # Redirect to the profile edit page or another page

    else:
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'accounts/profile_edit.html', {'user_form': user_form})
