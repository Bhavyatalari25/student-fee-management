from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    student_name = request.form.get("student_name", "")
    student_id = request.form.get("student_id", "")
    course = request.form.get("course", "")
    year = request.form.get("year", "")

    total_fee = float(request.form.get("total_fee", 0))
    amount_paid = float(request.form.get("amount_paid", 0))

    if total_fee < 0:
        total_fee = 0

    if amount_paid < 0:
        amount_paid = 0

    if amount_paid > total_fee:
        amount_paid = total_fee

    remaining_fee = total_fee - amount_paid

    if total_fee > 0:
        payment_percentage = (amount_paid / total_fee) * 100
    else:
        payment_percentage = 0

    if amount_paid == 0:
        status = "Pending"
    elif amount_paid >= total_fee:
        status = "Paid"
    else:
        status = "Partially Paid"

    paid_date = date.today().strftime("%d-%m-%Y")

    return render_template(
        "summary.html",
        student_name=student_name,
        student_id=student_id,
        course=course,
        year=year,
        total_fee=total_fee,
        amount_paid=amount_paid,
        remaining_fee=remaining_fee,
        payment_percentage=payment_percentage,
        paid_date=paid_date,
        status=status
    )


if __name__ == "__main__":
    app.run()