import joblib
from sklearn.preprocessing import LabelEncoder

# Load the model from the file
model = joblib.load('model.sav')

# Sample input data
sample_data = {
    'age': 30,                         # Sample age
    'job': 'engineer',                 # Sample job
    'marital': 'married',              # Marital status
    'education': 'bachelor',           # Education level
    'default': 'no',                   # Credit in default
    'housing': 'yes',                  # Has housing loan
    'loan': 'no',                      # Has personal loan
    'contact': 'cellular'              # Contact communication type
    # Assuming month and day_of_year were not used in training
}

# Encode categorical variables
label_encoders = {
    'job': LabelEncoder(),
    'marital': LabelEncoder(),
    'education': LabelEncoder(),
    'default': LabelEncoder(),
    'housing': LabelEncoder(),
    'loan': LabelEncoder(),
    'contact': LabelEncoder()
}

# Example: fitting encoders (normally done during training)
label_encoders['job'].fit(['engineer', 'teacher', 'doctor', 'etc.'])  # Add all categories used in training
label_encoders['marital'].fit(['married', 'single'])
label_encoders['education'].fit(['primary', 'secondary', 'bachelor'])
label_encoders['default'].fit(['yes', 'no', 'unknown'])
label_encoders['housing'].fit(['yes', 'no', 'unknown'])
label_encoders['loan'].fit(['yes', 'no', 'unknown'])
label_encoders['contact'].fit(['telephone', 'cellular'])

# Transform sample data using the fitted encoders
encoded_data = [
    sample_data['age'],
    label_encoders['job'].transform([sample_data['job']])[0],
    label_encoders['marital'].transform([sample_data['marital']])[0],
    label_encoders['education'].transform([sample_data['education']])[0],
    label_encoders['default'].transform([sample_data['default']])[0],
    label_encoders['housing'].transform([sample_data['housing']])[0],
    label_encoders['loan'].transform([sample_data['loan']])[0],
    label_encoders['contact'].transform([sample_data['contact']])[0]
]

# Make predictions using the model
predictions = model.predict([encoded_data])

print(predictions)
