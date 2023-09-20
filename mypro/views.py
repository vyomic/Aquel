from django.shortcuts import render

def my_view(request):
    # ... your view logic ...
    return render(request, 'index.html')
def about_us(request):
    # ... your view logic ...
    return render(request, 'about_us.html')
def resume(request):
    # ... your view logic ...
    return render(request, 'resume.html')
def skills(request):
    # ... your view logic ...
    return render(request, 'skills.html')