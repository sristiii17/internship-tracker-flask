from services.db_updater import update_application

update_application(
    company="Amazon",
    new_status="Interview",
    email_subject="Interview Invitation"
)