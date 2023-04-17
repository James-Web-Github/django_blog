from django.shortcuts import render
from .models import test_api1
from django.http import JsonResponse
# Create your views here.
def test_api(request):
    new_obj = test_api1()
    new_obj.api_name = "hohuou"
    new_obj.save()

    return JsonResponse(data={'msg':'add a obj success!'}, status=200)
def clear_test_api(request):
    all_obj = test_api1.objects.all()

    all_obj.delete()

    return JsonResponse(data={'msg':"delete success!"},status=200)
