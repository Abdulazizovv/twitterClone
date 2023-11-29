from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
from .forms import TweetForm, Tweet, EditProfileForm
from .models import UserProfile
from better_profanity import profanity


@login_required(login_url='login')
def user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'profile': user_profile})


def profile_view(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user)
    print(profile)
    if profile:
        return render(request, 'profile_view.html', {'profile': profile})
    print("error: No profile")


# @login_required(login_url='login')
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.cleaned_data['content'] = profanity.censor(form.cleaned_data['content'])
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            print(form.cleaned_data)
            return redirect('home')  
    else:
        form = TweetForm()
    all_tweets = Tweet.objects.all().order_by('-created_at')
    userprofile = None
    if request.user:
        try:
            userprofile = UserProfile.objects.get(user=request.user)
        except Exception as err:
            print(err)
    today = datetime.datetime.today()
    context = {
        'user_profile': userprofile,
        'today': today,
        'tweets': all_tweets,
    }


    return render(request, 'home.html', {'form': form, 'context': context})




@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})


def delete_tweet(request, pk):
    tweet = Tweet.objects.get(id=pk)
    if tweet.user == request.user:
        tweet.delete()
    else:
        print("you are not allowed to delete")
    return redirect('home')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            print("Error")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("not found")  
    return render(request, 'auth/login.html')


def signupPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                if not User.objects.filter(username=username).exists():
                    User.objects.create_user(username=username, password=password1, email=email)
                    return redirect('home')
            except Exception as err:
                print(err)
    return render(request, 'auth/signup.html')

def logoutPage(request):
    logout(request)
    return redirect('home')