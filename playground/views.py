from django.shortcuts import render
from django.http import HttpResponse

# Demo "products" for the storefront UI (no DB yet)
FEATURED_ITEMS = [
    {"name": "Quick start", "description": "Get your store running in minutes.", "url_name": "playground_hello"},
    {"name": "Admin", "description": "Manage content and users from the admin panel.", "url_name": None, "path": "/admin/"},
    {"name": "About", "description": "Learn more about this project.", "url_name": "about"},
]


def home(request):
    """Landing page with links to main sections."""
    return render(request, "home.html", {"featured": FEATURED_ITEMS})


def say_hello(request):
    """Greeting page – keeps your name in context."""
    return render(request, "hello.html", {"name": "Thiha"})


def about(request):
    """Simple about page for the project."""
    return render(request, "about.html")
