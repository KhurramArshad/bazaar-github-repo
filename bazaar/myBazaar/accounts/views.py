from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignupForm
# Create your views here.
def logout_thanks_view(request):
    return render(request, 'registration/thanks.html')

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # OR
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/thanks')
    return render(request, 'registration/signup.html', {'form':form})
