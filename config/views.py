from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Charul API is running",
        "status": "success"
    })