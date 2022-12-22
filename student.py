
def calc_total_marks(s):
    t_marks = s['physics'] + s['chemistry'] + s['maths']
    return t_marks

    
def calc_grade(s):
    grade = ''
    if s['total_marks'] > 200:
        grade = 'A'
    elif 100 < s['total_marks'] <= 200:
        grade = 'B'
    else:
        grade = 'C'
    return grade



def load_student_info():
    f = open('students_info.csv', 'r')
    list_s = []
    for line in f.readlines():
        row = line[0:-1].split(',')
        dic_s = {'name':row[0],
                 'dob':row[1],
                 'grade':row[2],
                 'total_marks':row[3],
                 'physics':int(row[4]),
                 'chemistry':int(row[5]),
                 'maths':int(row[6])}
        list_s.append(dic_s)
    return list_s

    
def enter_student_details():
    name = input("Name: ")
    dob = input("DOB:")
    marks_physics = input("Marks in Physics: ")
    marks_chemistry = input("Marks in Chemistry: ")
    marks_maths = input("Marks in Maths: ")
    dict_new_student = {'name':name,
                        'dob':dob,
                        'grade':'',
                        'total_marks':'',
                        'physics':int(marks_physics),
                        'chemistry':int(marks_chemistry),
                        'maths':int(marks_maths)}
    f = open('students_info.csv', 'a')
    a = name+","+dob+","+""+","+""+","+marks_physics+","+marks_chemistry+","+marks_maths+"\n"
    f.write(a)
    f.close()
    return dict_new_student