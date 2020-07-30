from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog_app/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(is_private=False).order_by('-date_updated')
        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super(PostDetailView, self).get_context_data(**kwargs)
        ctx['related_posts'] = Post.objects.filter(category=self.get_object().category).exclude(id=self.get_object().id).order_by('-date_updated')[:5][::-1]
        return ctx

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_app/blog_form.html'

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_app/blog_form.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/blog_delete.html'
    success_url = reverse_lazy('blog_app:list')
