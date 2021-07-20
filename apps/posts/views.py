from django.shortcuts import render, redirect
from apps.posts.forms.new_post import PostForm
from apps.posts.models import Post

# Create your views here.


def dashboard(request):
    if request.method == 'POST':
        new_post_form = PostForm(request.POST)
        if new_post_form.is_valid():
            new_post_form.save()
            return redirect('dashboard')
       
    new_post_form = PostForm()
    context = {
        'new_post_form' : new_post_form,
        'post' : Post.objects.all()
    }


    
    return render(request, 'dashboard.html', context)