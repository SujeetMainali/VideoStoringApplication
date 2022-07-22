from numpy import size

from django.shortcuts import redirect, render
from webapp.forms import VideoDetailsForm, VideoForm
from webapp.models import Video
from django.http import HttpResponse


# Create your views here.
def index(request):
    form = VideoForm(request.POST or None, request.FILES)
    # if request.method == 'POST':
    if form.is_valid():
        form.save()
        return redirect('home')
    # form = VideoForm()
    context = {'form': form}
    return render(request, 'index.html', context)

def uploadedvideos(request):
    videos = Video.objects.all()
    return render(request, 'uploadedvideos.html', {'videos': videos})

def charges(request):
    return render(request, 'charges.html')

def price(request):
    # return render(request, 'price.html')
    size = request.GET.get('video_size')
    duration = request.GET.get('video_duration')
    type = request.GET.get('video_type')
    if size < '500':
        price = 5
        params = {'size': size, 'duration': duration, 'type': type, 'price': price}
        return render(request, 'price.html', params)
    if size > '500':
        price = 12.2
        params = {'size': size, 'duration': duration, 'type': type, 'price': price}
        return render(request, 'price.html', params)
    if(size < '500' and duration < '6.33'):
        price = price + 12.5
        params = {'size': size, 'duration': duration, 'type': type, 'price': price}
        return render(request, 'price.html', params)
    if(size > '500' and duration > '6.33'):
        price = price + 12.5
        params = {'size': size, 'duration': duration, 'type': type, 'price': price}
        return render(request, 'price.html', params)

    return HttpResponse('Error')


   