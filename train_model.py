from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
import pandas as pd

# Load dataset from URL
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep="\t", header=None, names=["label", "message"])
df['label'] = df['label'].map({'ham': 0, 'spam': 1})


# Add custom spam examples (Snapchat-style)
extra_data = [
     {"label": 1, "message": "You've got a Memory to look back on"},
    {"label": 1, "message": "You've got a Memory to look back on"},
    {"label": 1, "message": "Someone messaged you on Snapchat"},
    {"label": 1, "message": "View your recent snaps now"},
    {"label": 1, "message": "You've got a Memory to look back on"},
{"label": 1, "message": "You've got a Memory to look back on"},
{"label": 1, "message": "You've got a Memory to look back on"},
{"label": 1, "message": "You've got a Memory to look back on"},
{"label": 1, "message": "You've got a Memory to look back on"},
{"label": 1, "message": "You've got a Memory to look back on"},
{"label": 1, "message": "You've got a Memory to look back on"},
{"label": 1, "message": "You've got a Memory to look back on"},
{"label": 1, "message": "You've got a Memory to look back on"},
    {"label": 1, "message": "You have unread messages on Snapchat"},
    {"label": 1, "message": "New Snapchat memory available"},
    {"label": 1, "message": "Open Snapchat to see what you missed"},
    {"label": 1, "message": "Someone just sent you a snap"},
    {"label": 1, "message": "You received a new message on Snapchat"},
    {"label": 1, "message": "You've got a memory to look back on"},
    {"label": 1, "message": "View recent Snapchat memories now"},
    {"label": 1, "message": "You've got a memory to look back on"},
    {"label": 1, "message": "Check your Snapchat memories"},
    {"label": 1, "message": "New memory notification from Snapchat"},
    {"label": 1, "message": "Snapchat memory alert"},
    {"label": 1, "message": "View your snap memories now"}
]

ham_data = [
     {"label": 0, "message": "Security alert"},
     {"label": 0, "message": " Your Google Account was recovered successfully"},
    {"label": 0, "message": "Google Verification code"},
    {"label": 0, "message": "Your single-use code"},
    {"label": 0, "message": "Your single-use code is: 857421"},
    {"label": 0, "message": "Your account has been logged in from a new device"},
    {"label": 0, "message": "Password reset request received"},
    {"label": 0, "message": "Your bill for June is ready"},
    {"label": 0, "message": "Meeting scheduled for tomorrow at 10 AM"},
    {"label": 0, "message": "Reminder: Your appointment is on 5th June"},
    {"label": 0, "message": "Thank you for your payment"},
    {"label": 0, "message": "Your order has been shipped"},
    {"label": 0, "message": "Welcome to our service! Your account is active"},
    {"label": 0, "message": "Hey, are you free this weekend?"},
    {"label": 0, "message": "Can we meet for lunch tomorrow?"},
    {"label": 0, "message": "Don't forget to bring the documents"},
    {"label": 0, "message": "Happy birthday! Have a great day!"},
    {"label": 0, "message": "Invoice for your recent purchase"},
    {"label": 0, "message": "Your electricity bill is due"},
    {"label": 0, "message": "Important update from your bank"}
]
df_ham = pd.DataFrame(ham_data)
df = pd.concat([df, df_ham], ignore_index=True)

df_extra = pd.DataFrame(extra_data)
df = pd.concat([df, df_extra], ignore_index=True)


# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# CountVectorizer(ngram_range=(1, 2), stop_words='english')

# Train a Naive Bayes model using a pipeline
model = make_pipeline( CountVectorizer(ngram_range=(1, 2), stop_words='english'),
    MultinomialNB(alpha=0.5))
model.fit(X_train, y_train)

# Evaluate accuracy
print("Accuracy:", model.score(X_test, y_test))

# Save model for future use
joblib.dump(model, "spam_classifier.pkl")
