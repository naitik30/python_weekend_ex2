from django.shortcuts import render
from .froms import BlogDataForm
from django.contrib import messages
from .models import BlogData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def Blog_list(request):
    form = BlogDataForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Blog  created")

    quearyset_list = BlogData.objects.all()
    paginator = Paginator(quearyset_list, 2)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        quearyset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        quearyset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        quearyset = paginator.page(paginator.num_pages)
    context = {
        "title": "BlogList",
        "object_list": quearyset,
        "form": form,
    }
    return render(request, "blog.html", context)
