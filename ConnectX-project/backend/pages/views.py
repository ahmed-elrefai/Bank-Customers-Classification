from django.shortcuts import render
from ai_api.views import load_model,predict
# Create your views here.

def form_page(request):
    load_model()
    return render(request, 'form.html')

def home_page(request):
    return render(request, 'home.html')

def ai_results_page(request):
    percentage = predict(request)
    print(percentage)
    return render(request, 'ai_result.html', {'percentage': f'{percentage:.2f}'})