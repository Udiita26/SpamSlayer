from fetch_emails import get_email_data
from gmail_auth import get_service
import joblib

# Load trained model
model = joblib.load("spam_classifier.pkl")

# Connect to Gmail API
service = get_service()

# Fetch emails (you can increase max_results if needed)
emails = get_email_data(service, max_results=10)

# Classify each email
for i, email in enumerate(emails):
    text = email['subject'] + " " + email['body']
    prediction = model.predict([text])[0]
    label = "📬 Not Spam" if prediction == 0 else "🚫 Spam"
    
    print(f"\nEmail {i+1}: {label}")
    print(f"Subject: {email['subject']}")
    print(f"Body: {email['body'][:150]}...")
