from flask import Flask, render_template, request, send_file
from llama_api import generate_quiz
from fpdf import FPDF
from io import BytesIO

app = Flask(__name__)
last_quiz = {"topic": "", "content": ""}  

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        try:
            quiz = generate_quiz(topic)
            last_quiz["topic"] = topic
            last_quiz["content"] = quiz
            return render_template("quiz.html", topic=topic, quiz=quiz)
        except Exception as e:
            return f"Error: {e}"
    return render_template("index.html")

@app.route("/download")
def download():
    from fpdf import FPDF
    from io import BytesIO

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "Name: ___________________________", ln=True)
    pdf.cell(0, 10, "Roll Number: ____________________", ln=True)
    pdf.cell(0, 10, "Section: _________________________", ln=True)
    pdf.ln(10)  

    for line in last_quiz["content"].split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf_output = pdf.output(dest='S').encode('latin1')
    buffer = BytesIO(pdf_output)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"{last_quiz['topic']}_quiz.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run(debug=True)
