from django.views.generic import TemplateView, FormView
from django.http import JsonResponse
from django.core.mail import send_mail
from blog_app.models import Post
from .forms import ContactForm

class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexTemplateView, self).get_context_data(**kwargs)
        ctx['private_posts'] = Post.objects.all()[:4]
        ctx['public_posts'] = Post.objects.filter(is_private=False)[:4]
        return ctx

class WatershedMapTemplateView(TemplateView):
    template_name = 'watersheds.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        if self.request.is_ajax():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            send_mail('Website Query from ' + name, message + "\n\nReply to " + name + " at " + email, 'queries@waterresourcestt.com', ['kevanleelum@gmail.com',],
                fail_silently=False,
            )
            return JsonResponse({"message": "Your message has bean sent. Returning to the home page now..."})
        return super().form_valid(form)
