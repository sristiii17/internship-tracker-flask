import sqlite3
from flask import Flask, render_template, request, redirect
from scheduler import run_once

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("internships.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT NOT NULL,
            email_subject TEXT,
            last_updated TEXT,
            updated_by TEXT DEFAULT 'Manual'

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS status_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_id INTEGER,
            old_status TEXT,
            new_status TEXT,
            email_subject TEXT,
            changed_at TEXT,

            FOREIGN KEY(application_id)
            REFERENCES applications(id)

        )
    """)

    conn.commit()
    conn.close()


init_db()


@app.route("/", methods=["GET", "POST"])
def home():

    conn = sqlite3.connect("internships.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if request.method == "POST":

        company = request.form["company"].strip()
        role = request.form["role"].strip()
        status = request.form["status"].strip()

        cursor.execute(
            """
            INSERT INTO applications
            (company, role, status)
            VALUES (?, ?, ?)
            """,
            (company, role, status)
        )

        conn.commit()

        return redirect("/")

    cursor.execute("SELECT * FROM applications")

    applications = cursor.fetchall()
    total = len(applications)
    applied = sum(1 for app in applications if app["status"] == "Applied")
    interview = sum(1 for app in applications if app["status"] == "Interview")
    selected = sum(1 for app in applications if app["status"] == "Selected")
    rejected = sum(1 for app in applications if app["status"] == "Rejected")

    conn.close()

    return render_template(
    "index.html",
    apps=applications,
    total=total,
    applied=applied,
    interview=interview,
    selected=selected,
    rejected=rejected
)


@app.route("/delete/<int:id>")
def delete(id):

    conn = sqlite3.connect("internships.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM applications WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    conn = sqlite3.connect("internships.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if request.method == "POST":

        company = request.form["company"]
        role = request.form["role"]
        status = request.form["status"]

        cursor.execute(
            """
            UPDATE applications
            SET company=?, role=?, status=?
            WHERE id=?
            """,
            (company, role, status, id)
        )

        conn.commit()

        conn.close()

        return redirect("/")

    cursor.execute(
        "SELECT * FROM applications WHERE id=?",
        (id,)
    )

    application = cursor.fetchone()

    conn.close()

    return render_template(
        "edit.html",
        app=application
    )

@app.route("/sync")
def sync():

    run_once()

    return redirect("/")    

if __name__ == "__main__":
    app.run(debug=True)