from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog_app/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(is_private=False)
        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super(PostDetailView, self).get_context_data(**kwargs)
        ctx['posts'] = Post.objects.all()[:5][::-1]
        return ctx

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_app/blog_form.html'
