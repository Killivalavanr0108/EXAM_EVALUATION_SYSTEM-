from flask import Flask, render_template, request, redirect
import os
from omr_processing import process_omr
from excel_export import export_to_excel

app = Flask(__name__)
UPLOAD_FOLDER = "OMR_Sheets"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

student_records = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    global student_records

    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        data = process_omr(filepath)
        student_records.append(data)

        return redirect("/records")

    return render_template("upload.html")

@app.route("/records")
def records():
    sorted_records = sorted(student_records, key=lambda x: x["Register Number"])
    return render_template("records.html", records=sorted_records)

@app.route("/delete/<reg>")
def delete(reg):
    global student_records
    student_records = [r for r in student_records if r["Register Number"] != reg]
    return redirect("/records")

@app.route("/export")
def export():
    export_to_excel(student_records)
    return "Excel File Exported Successfully!"

if __name__ == "__main__":
    app.run(debug=True)
