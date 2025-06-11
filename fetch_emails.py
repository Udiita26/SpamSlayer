from googleapiclient.discovery import build
from gmail_auth import get_service
import base64
import email

def get_email_data(service, max_results=10):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])

    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = msg_data['payload']
        headers = payload.get('headers', [])

        subject = ''
        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
                break

        parts = payload.get('parts', [])
        body = ''
        if parts:
            for part in parts:
                if part['mimeType'] == 'text/plain':
                    body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8', errors='ignore')
                    break

        emails.append({'subject': subject, 'body': body})

    return emails

if __name__ == "__main__":
    service = get_service()
    emails = get_email_data(service)
    for i, email in enumerate(emails):
        print(f"\n📩 Email {i+1}")
        print(f"Subject: {email['subject']}")
        print(f"Body: {email['body'][:300]}...")  # Print only first 300 chars
