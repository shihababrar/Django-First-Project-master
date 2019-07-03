from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def home_page(request):
    title = "Home Page"
    template= "home.html"
    return render(request,template, {"title": title})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form
                }
    return render(request,"form.html", context)

def about_page(request):
    return render(request, "hello_world.html", {"title": "About Us"})