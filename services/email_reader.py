from services.gmail_service import get_gmail_service
from services.company_extractor import extract_company
from bs4 import BeautifulSoup
import base64
import re


def extract_body(payload):
    """
    Recursively extract email body from Gmail payload.
    """

    if "parts" in payload:
        for part in payload["parts"]:
            body = extract_body(part)
            if body:
                return body

    data = payload.get("body", {}).get("data")

    if not data:
        return ""

    decoded = base64.urlsafe_b64decode(
        data
    ).decode("utf-8", errors="ignore")

    if payload.get("mimeType") == "text/html":
        soup = BeautifulSoup(decoded, "html.parser")
        return soup.get_text("\n", strip=True)

    return decoded

def get_latest_emails(limit=5):

    service = get_gmail_service()

    results = service.users().messages().list(
        userId="me",
        q='interview OR application OR assessment OR internship',
        maxResults=limit
    ).execute()

    messages = results.get("messages", [])

    email_list = []

    for msg in messages:

        message = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        headers = message["payload"]["headers"]

        subject = ""
        sender = ""
        date = ""

        for header in headers:

            if header["name"] == "Subject":
                subject = header["value"]

            elif header["name"] == "From":
                sender = header["value"]

            elif header["name"] == "Date":
                date = header["value"]

        body = extract_body(message["payload"])

        company = extract_company(sender, subject)

        email_list.append({
            "company": company,
            "sender": sender,
            "subject": subject,
            "date": date,
            "body": body
        })

    return email_list


if __name__ == "__main__":

    emails = get_latest_emails()

    print(f"\nFound {len(emails)} emails\n")

    for email in emails:

        print("=" * 70)
        print("Company :", email["company"])
        print("From    :", email["sender"])
        print("Subject :", email["subject"])
        print("Date    :", email["date"])
        print()
        print(email["body"][:300])
        print()