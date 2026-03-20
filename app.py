import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

applications = []

def init_db():
    conn = sqlite3.connect("internships.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            role TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()
@app.route("/", methods=["GET", "POST"])
def home():
    conn = sqlite3.connect("internships.db")
    cursor = conn.cursor()

    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        status = request.form["status"]

        cursor.execute(
            "INSERT INTO applications (company, role, status) VALUES (?, ?, ?)",
            (company, role, status)
        )

        conn.commit()
        conn.close()

        return redirect("/")   # ⭐ important fix

    cursor.execute("SELECT * FROM applications")
    applications = cursor.fetchall()

    conn.close()

    return render_template("index.html", apps=applications)


@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("internships.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM applications WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        applications[index]["company"] = request.form["company"]
        applications[index]["role"] = request.form["role"]
        applications[index]["status"] = request.form["status"]
        return redirect("/")

    return render_template("edit.html", app=applications[index], index=index)

if __name__ == "__main__":
    app.run(debug=True)