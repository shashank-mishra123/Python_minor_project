from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///school.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    student_branch = db.Column(db.String(50), nullable=False)
    student_fees = db.Column(db.Float, nullable=False)
    student_email = db.Column(db.String(100), unique=True, nullable=False)
    student_number = db.Column(db.String(15), nullable=False)
    student_location = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/students", methods=["POST"])
def create_student():
    
    data = request.json

    student = Student(
        student_name=data["student_name"],
        student_branch=data["student_branch"],
        student_fees=data["student_fees"],
        student_email=data["student_email"],
        student_number=data["student_number"],
        student_location=data["student_location"]
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Student created successfully"}), 201


@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    result = []

    for s in students:
        result.append({
            "student_id": s.student_id,
            "student_name": s.student_name,
            "student_branch": s.student_branch,
            "student_fees": s.student_fees,
            "student_email": s.student_email,
            "student_number": s.student_number,
            "student_location": s.student_location
        })

    return jsonify(result)


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)

    return jsonify({
        "student_id": student.student_id,
        "student_name": student.student_name,
        "student_branch": student.student_branch,
        "student_fees": student.student_fees,
        "student_email": student.student_email,
        "student_number": student.student_number,
        "student_location": student.student_location
    })


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.json

    student.student_name = data["student_name"]
    student.student_branch = data["student_branch"]
    student.student_fees = data["student_fees"]
    student.student_email = data["student_email"]
    student.student_number = data["student_number"]
    student.student_location = data["student_location"]

    db.session.commit()

    return jsonify({"message": "Student updated successfully"})


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
