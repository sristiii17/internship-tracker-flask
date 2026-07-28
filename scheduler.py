from services.email_reader import get_latest_emails
from services.keyword_matcher import detect_status
from services.db_updater import update_application


def run_once():
    emails = get_latest_emails(limit=10)

    print(f"\nChecking {len(emails)} emails...\n")

    for email in emails:

        print("=" * 60)
        print("Company :", email["company"])
        print("Subject :", email["subject"])

        result = detect_status(
            email["subject"] + "\n" + email["body"]
        )

        print("Status :", result)

        if email["company"] == "Unknown":
            print("Skipping: Company not detected\n")
            continue

        if result["status"] == "Unknown":
            print("Skipping: No status detected\n")
            continue

        update_application(
            company=email["company"],
            new_status=result["status"],
            email_subject=email["subject"]
        )


if __name__ == "__main__":
    run_once()