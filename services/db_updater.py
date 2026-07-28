import sqlite3
from datetime import datetime


DB_NAME = "internships.db"


def update_application(company, new_status, email_subject):
    """
    Update an application's status if it exists.
    Also save the change in status_history.
    """

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
    """
    SELECT *
    FROM applications
    WHERE TRIM(LOWER(company)) = TRIM(LOWER(?))
    """,
    (company,)
                )

    application = cursor.fetchone()

    if application is None:
        print(f"[INFO] No application found for '{company}'")
        conn.close()
        return False

    current_status = application["status"]

    if current_status == new_status:
        print(f"[INFO] {company} already marked as '{new_status}'")
        conn.close()
        return False

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        UPDATE applications
        SET
            status=?,
            email_subject=?,
            last_updated=?,
            updated_by=?
        WHERE id=?
        """,
        (
            new_status,
            email_subject,
            now,
            "Gmail Automation",
            application["id"]
        )
    )

    cursor.execute(
        """
        INSERT INTO status_history
        (
            application_id,
            old_status,
            new_status,
            email_subject,
            changed_at
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            application["id"],
            current_status,
            new_status,
            email_subject,
            now
        )
    )

    conn.commit()
    conn.close()

    print(f"[UPDATED] {company}: {current_status} → {new_status}")

    return True