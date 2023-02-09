import view
import modul

from modul import students_basa


def start():
     while True:
          dr = view.data_request()
          if dr == 0:
               student = view.input_student()
               modul.create_student(student)
          elif dr == 1:
               subject = view.input_subject()
               modul.add_subject(subject)
          elif dr == 2:
               student, subject, grade = view.input_grade()
               modul.add_grade(student, subject, grade)
          elif dr == 3:
               modul.show_students_names()
          elif dr == 4:
               print(modul.students_name)
               student_name = view.input_student()
               modul.show_student_journal(student_name)
          elif dr == 5:
               modul.random_list()
          elif dr == 6:
               modul.write_file()
          elif dr == 7:
               modul.reading_file()
          elif dr == 8:
               break