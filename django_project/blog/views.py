from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import forms
import random
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

def surprise(request):
    template = "blog/surprise_problem.html"
    surprise_id=random.randint(10,40)
    post=Post.objects.filter(id=surprise_id)
    context={
        'posts':post
    }
    return render(request,template,context)


def  search(request):
    template = "blog/post_list.html"
    query = request.GET.get('q')
    results = Post.objects.filter(Q(title__icontains=query)|Q(content__icontains=query))
    context = {
        'posts' : results
    }
    
    return render(request, template, context)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def feedback(request):
    return render(request,'blog/feedback.html')

def submit(request):
    
    issue=request.GET.get('issue')
    suggestion=request.GET.get('suggestion')
    current_user = request.user
    send_mail(
        issue,
        suggestion,
        current_user.email,
        ["varunsai.nadipelly@gmail.com"],
        fail_silently=False
    )
    
    return render(request,'blog/thanks.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostHintView(DetailView):
    model = Post
    template_name = 'blog/post_hint.html' 
    
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    hint = forms.TextInput()
    fields = ['title', 'content', 'hint']
    l=[]
    i=""
    for i in User.objects.all():
        l.append(i.email)

    def form_valid(self, form):
        username=self.request.user
        form.instance.author = self.request.user
        l=[]
        i=""
        for i in User.objects.all():
            l.append(i.email)
        send_mail(
            '[New Problem Statement!!!!]Hello from Coding club!!!',
            f'A new problem statement has been uploaded by {username}. Go and check it now!!!',
            'varunsai.nadipelly@gmail.com',
            l,
            fail_silently=False
        )
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    hint = forms.TextInput()
    fields = ['title', 'content', 'hint']
    l=[]
    i=""
    for i in User.objects.all():
        l.append(i.email)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        l=[]
        i=""
        for i in User.objects.all():
            l.append(i.email)
        if self.request.user == post.author:
            uname=self.request.user
            send_mail(
                '[Problem Statement Updated!!!!]Hello from Coding club!!!',
                f'A new problem statement has been updated by {uname}. Go and check the updated version!!!',
                'varunsai.nadipelly@gmail.com',
                l,
            fail_silently=False
            )
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    description="VCE Coding Community helps students share the coding problem statements and thus increases their coding and problem skills!!!"
    return render(request, 'blog/about.html', {'title': 'VCE Coding Community','description' : description})

