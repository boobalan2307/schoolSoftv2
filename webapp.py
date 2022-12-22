from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/display")
def display():
    f = open('students_info.csv', 'r')
    html_string = ''
    for line in f.readlines():
        html_string = html_string + line + "<br>"
    print(html_string)
    return html_string

@app.route("/capture")
def capture():
    return render_template('capture_student_info.html')

@app.route("/login", methods=['POST'])
def login():
    user = request.form['nm']
    dob = request.form['dob']
    marks_physics = request.form['marks_physics']
    marks_chemistry = request.form['marks_chemistry']
    marks_maths = request.form['marks_maths']
    t  = user +"," + dob +"," +","+","+ marks_physics +"," + marks_chemistry + "," + marks_maths+"" +'\n'
    f = open('students_info.csv', 'a')
    f.write(t)
    f.close()
    return "<p>Hello "+user+" "+dob+" "+marks_physics+" "+marks_chemistry+" " +marks_maths+" </p>"

app.run()
