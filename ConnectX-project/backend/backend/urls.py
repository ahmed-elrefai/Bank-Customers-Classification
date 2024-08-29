from django.contrib import admin
from django.urls import path, include  # Added `include`
from pages.views import home_page, form_page, ai_results_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('form/', form_page),
    path('form/result/', ai_results_page), 
]
