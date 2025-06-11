import joblib

# Model load karo
model = joblib.load("spam_classifier.pkl")

# Test karo specific message pe
msg = [" You've got a Memory to look back on"]
prediction = model.predict(msg)

print("Prediction (1=Spam, 0=Not Spam):", prediction[0])
