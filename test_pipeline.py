from services.email_reader import get_latest_emails
from services.keyword_matcher import detect_status


emails = get_latest_emails()

for email in emails:

    result = detect_status(email["body"])

    print("=" * 70)

    print("Company :", email["company"])
    print("Subject :", email["subject"])
    print("Status  :", result["status"])
    print("Confidence :", result["confidence"], "%")

    print("=" * 70) 