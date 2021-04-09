from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render,get_object_or_404
from .models import Category, Cat_items
from .forms import CommentForm

# Create your views here.


def home(request):
    cat_list = Category.objects.all()
    paginator = Paginator(cat_list, 4)
    page_number = request.GET.get('page')
    try:
        cat_list = paginator.page(page_number)
    except PageNotAnInteger:
        cat_list = paginator.page(1)
    except EmptyPage:
        cat_list = paginator.page(paginator.num_pages)
    return render(request, 'home/index.html', {'cat_list': cat_list})

def cat_items(request,item,id):
    cat = Category.objects.get(id=id)
    items = Cat_items.objects.filter(category=id,status='published')
    paginator = Paginator(items,4)
    page_number = request.GET.get('page')
    try:
        items = paginator.page(page_number)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'home/catitems.html', {'cat':cat, 'items': items})

@login_required
def cat_items_detail(request,item):
    item = get_object_or_404(Cat_items,slug=item,status='published')
    user = User.objects.get(id=request.user.id)
    comments = item.comments.filter(active=True) # here 'comments' in the middle is related_name
    form = CommentForm()
    csubmit = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_Comment = form.save(commit=False)
            new_Comment.item = item
            new_Comment.user = user
            new_Comment.save()
            csubmit = True
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'home/itemdetails.html', {'item': item, 'form': form, 'csubmit': csubmit, 'comments': comments})


