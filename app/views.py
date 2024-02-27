from django.shortcuts import render
from django.http import JsonResponse
from .models import PhotoSubmission
from PIL import Image
from io import BytesIO
import base64
import os
from django.conf import settings

def submit_photo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        image_data = request.POST.get('image_data')

        if image_data is not None:
            try:
                # Decode base64 data
                image_data = image_data.split('base64,')[1]
                image = Image.open(BytesIO(base64.b64decode(image_data)))
                
                # Save image to MEDIA_ROOT directory
                image_path = os.path.join(settings.MEDIA_ROOT, 'photos', 'temp.jpg')
                image.save(image_path, format='JPEG')
                
                # Create PhotoSubmission instance and save
                submission = PhotoSubmission.objects.create(
                    name=name,
                    date=date,
                    time=time,
                    location=location,
                    photo='photos/temp.jpg'  # Save relative path to the image
                )
                submission.save()
                
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
        else:
            return JsonResponse({'success': False, 'error': 'Image data is missing.'})

    return render(request, 'submit_photo.html')
