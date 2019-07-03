from django import forms
from .models import BlogPost
class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget= forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "content"]

        def clean_title(self, *args, **kwargs):
            title = self.cleaned_data.get("title")
            qs = BlogPost.objects.filter(title_iexact= title)
            if qs.exists():
                raise forms.ValidationError("Title is already exists!")
            return  title
