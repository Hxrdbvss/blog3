from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Category, Post, Comment, Page
from .forms import RegistrationForm, ProfileForm, CommentForm, PostForm, PageForm
from django.contrib.auth.models import User

def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def post_detail(request, id):
    post = get_object_or_404(Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ), id=id)
    comments = post.comments.all().order_by('created_at')
    form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments, 'form': form})

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/category.html', {
        'category': category,
        'page_obj': page_obj
    })

def profile(request, username):
    profile = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(
        author=profile,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'profile': profile,
        'page_obj': page_obj,
    }
    return render(request, 'blog/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile', username=request.user.username)
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/edit_profile.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Добавляем request.FILES для изображений
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:index')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {'post': post, 'form': form})

@login_required
def edit_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)
    if comment.author != request.user:
        return redirect('blog:post_detail', id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', id=post_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment.html', {'post': comment.post, 'form': form, 'comment': comment})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Проверяем, что текущий пользователь — автор поста
    if post.author != request.user:
        return redirect('blog:post_detail', id=post.id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect('blog:post_detail', id=post.id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('blog:index')  # Перенаправление на главную после удаления
    else:
        form = PostForm(instance=post)  # Форма нужна для отображения данных в шаблоне
    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)
    if comment.author != request.user:
        return redirect('blog:post_detail', id=post_id)
    
    if request.method == 'POST':
        comment.delete()
        return redirect('blog:post_detail', id=post_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment.html', {'post': comment.post, 'form': form, 'comment': comment})

# Новые CBV для статичных страниц
class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/page_detail.html'
    context_object_name = 'page'

    def get_queryset(self):
        return Page.objects.filter(is_published=True)

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'blog/page_form.html'

    def get_queryset(self):
        return Page.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('blog:page_detail', kwargs={'slug': self.object.slug})