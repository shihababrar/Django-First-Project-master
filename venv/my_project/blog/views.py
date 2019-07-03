
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm

def blog_post_detail_page(request):
    data = BlogPost.objects.all()
    template_name = "blog_post_detail.html"
    context = {
        "data": data
    }
    return render(request, template_name, context)

#@login_required()
@staff_member_required()
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
      #  obj = BlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit= False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = "form.html"
    context = {
        "form": form
    }
    return render(request,template_name,context)

def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    form = BlogPostModelForm(request.POST or None, instance = obj)
    template_name = "form.html"
    context = {
        "form": form,
        "title": f"Update {obj.title}"
    }
    return render(request, template_name, context)


