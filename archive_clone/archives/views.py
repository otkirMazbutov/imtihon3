from django.shortcuts import render
from .models import Archive

def archive_list(request):
    entries = Archive.objects.all().order_by('-published_date')
    return render(request, 'archive/archive_list.html', {'entries': entries})
