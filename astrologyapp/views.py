from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import math

@csrf_exempt  # Only use this if you understand the security implications
def index(request):
    # Your index view logic here
    return render(request, 'index.html')

@csrf_exempt  # Only use this if you understand the security implications
def run_script(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        year = int(data['year'])
        month = int(data['month'])
        day = int(data['day'])
        
        # Your calculation for height
        height04112023 = 815324
        if year == 2023:
            if month == 11:
                height = height04112023 + ((day - 4) * 150)
            else:
                height = height04112023 + ((19 + day) * 150)
        else:
            height = (height04112023 + (57 * 150) +
                      (((year - 2024) * 365.25 + ((month - 1) * 30.5 )+ (day - 1)) )*150)
        height=height/210000

        # Your calculation for price
        print(height)
        price = 30 * (height ** 5.5) * (10**((0.7**height) * math.sin((2 * math.pi * height) - 0.4)))

        # Return the price as JSON
        return JsonResponse({'result': price})

    # If the request is not POST, or there is some other error:
    return JsonResponse({'error': 'Invalid request'}, status=400)