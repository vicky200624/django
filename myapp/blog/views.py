from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls.base import reverse
import logging
from .models import Post
from django.core.paginator import Paginator
from .forms import ContactForm
# Create your views here.
# posts = [
#         {"id": 1, "title": "First Post", "content": "This is the first post."},
#         {"id": 2, "title": "Second Post", "content": "This is the second post."},
#     ]
def index(request):
    blog_title = "Latest Blog Posts" #varialbe interpolation
    #getting all the posts from the database by post model
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 5) # Show 5 posts per page
    page_number = request.GET.get("page")
    post_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"blog_title": blog_title, "post_obj": post_obj})

def detail(request, blog_id):
    #static data
    #post = next((item for item in posts if item["id"] == blog_id), None)
    #getting the post with the given id from the database
    #post = Post.objects.get(pk=blog_id) #getting the post with the given id from the database
    # logger = logging.getLogger("TESTING")
    # logger.debug(f"Retrieved post: {post}")   Log the retrieved post for debugging
    post = get_object_or_404(Post, slug=blog_id)
    related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)  # Get related posts based on category, excluding the current post
    if not post:
        return render(request, "404.html", status=404)
    return render(request, "detail.html", {"post": post, "related_posts": related_posts})

def old_url_redirect(request):
    return redirect(reverse("blog:new_url"))

def new_url_view(request):
    return HttpResponse("This is the new URL view.")
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            # Here you can handle the form data, such as saving it to the database or sending an email
            print(f"Received contact form submission: Name={name}, Email={email}, Message={message}")
            return HttpResponse("Thank you for contacting us!")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
    

def about(request):
    return render(request, "about.html")