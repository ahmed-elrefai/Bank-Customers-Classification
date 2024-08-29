from django.http import JsonResponse
import joblib
import numpy as np
# Create your views here.

loaded_model = None

def load_model():
    global loaded_model
    loaded_model = joblib.load('/home/ahmed-elrefai/Desktop/ConnectX-project/backend/static/models/model.sav')


def predict(request):
    try:
        # Get data from the form
        data = {
            'loan': request.POST.get('age'),
            'week-day': request.POST.get('week-day'),
            'housing': request.POST.get('housing'),
            'month': request.POST.get('month'),
            'default': request.POST.get('default'),
            'education': request.POST.get('education'),
            'job': request.POST.get('job'),
            'contact': request.POST.get('contact')
        }
        
        # Preprocess the data (if needed)
        # Assuming no additional preprocessing needed here

        # Convert form data to an array to feed to the model
        data_array = [data['job'], data['education'],data['loan'], data['week-day'], data['housing'], data['month'], data['default'], data['contact']]
        data_array = [float(x) if x.isdigit() else x for x in data_array]  # Ensure data types are appropriate for your model
        
        # Reshaping the data
        data_array = np.array(data_array).reshape(1, -1)

        # Use the model to predict the input that came from the form
        probabilities = loaded_model.predict_proba(data_array)

        percentage = probabilities[0][1] * 100

        # Return the percentage as JSON
        return percentage
    
    except Exception as e:
        return JsonResponse({'error': str(e)})