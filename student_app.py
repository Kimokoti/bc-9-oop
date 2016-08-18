from student import Student
import attendance_tracker
import datetime
# Create at least 10 student

s1 = Student('Yusuf', 'Hamisi')
s2 = Student('Kevin', 'Chiteri')
s3 = Student('Brian', 'Kimokoti')
s4 = Student('Arnold', 'Okoth')
s5 = Student('Beth', 'Wanjiku')
s6 = Student('Ndegwa', 'Kimani')
s7 = Student('Edison', 'Abahurire')
s8 = Student('Allan', 'Mwesigwa')
s9 = Student('Rehema', 'Wachira')
s10 = Student('Whitney', 'Ruoroh')

# Make at least 5 students attend class
s1.attend_class(loc='Hogwarts',date=datetime.date.today(),teacher='Alex')
s2.attend_class(loc='Hogwarts',date=datetime.date.today(),teacher='Mwale')
s3.attend_class(loc='Hogwarts',date=datetime.date.today(),teacher='')
s4.attend_class(loc='Hogwarts',date=datetime.date.today(),teacher='')
s5.attend_class(loc='Hogwarts',date=datetime.date.today(),teacher='')


s6.attend_class(loc='Hogwarts',date=datetime.date.today()-datetime.timedelta(days=1),teacher='')
s7.attend_class(loc='Hogwarts',date=datetime.date.today()-datetime.timedelta(days=1),teacher='')
s8.attend_class(loc='Hogwarts',date=datetime.date.today()-datetime.timedelta(days=1),teacher='')
s9.attend_class(loc='Hogwarts',date=datetime.date.today()-datetime.timedelta(days=1),teacher='')
s10.attend_class(loc='Hogwarts',date=datetime.date.today()-datetime.timedelta(days=1),teacher='')

# You should be able to print the list of students who
# attended class on a particular day

# print(s1.print_attendance())
# print(s2.print_attendance())
# print(s3.print_attendance())
# print(s4.print_attendance())

# attendance_tracker.AttendanceTracker.print_attendance('18/08/2016')

attendance_tracker.AttendanceTracker.print_attendance(datetime.date.today()-datetime.timedelta(days=1))


