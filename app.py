from flask import Flask, render_template, request, redirect
from entities.student import Student
from entities.professor import Professor

app = Flask(__name__)

students_list = []
professors_list = []
courses_list = []

@app.route("/")
def index():
    return render_template('index.html', students=students)


@app.route("/students")
def students():
    return render_template('students.html', students_list=students_list)


@app.route("/professors")
def professors():
    return render_template('professors.html', professors_list=professors_list)

@app.route("/courses")
def courses():
    return render_template('courses.html', courses_list=courses_list)

@app.route("/new_student", methods=['GET', 'POST'])
def new_student():
    if request.method == "GET":
        print("Método GET")
        return render_template('new_student.html')
    elif request.method == "POST":
        estudiante = {
            "nombre": request.form["nombre"],
            "apellido_paterno": request.form["apellido_paterno"],
            "apellido_materno": request.form["apellido_materno"],
            "fecha_nacimiento": request.form["fecha_nacimiento"],
            "matricula": request.form["matricula"]
        }
        students.append(estudiante)
        return redirect('/students')
    
@app.route("/new_professor", methods=['GET', 'POST'])
def new_professor():
    if request.method == "GET":
        print("Método GET")
        return render_template('new_professor.html')
    elif request.method == "POST":
        professor = Professor(
            request.form["nombre"],
            request.form["apellido_paterno"],
            request.form["apellido_materno"],
            request.form["id_professor"]
        )
        professors_list.append(professor)
        return redirect('/professors')

@app.route("/new_course", methods=['GET', 'POST'])
def new_course():
    if request.method == "GET":
        print("Método GET")
        return render_template('new_course.html')
    elif request.method == "POST":
        course = Course(
            request.form["codigo"],
            request.form["nombre"],
            request.form["creditos"],
            request.form["descripcion"]
        )
        courses_list.append(course)
        return redirect('/courses')
    
if __name__ == '__main__':
    app.run(debug=True, port=8888)