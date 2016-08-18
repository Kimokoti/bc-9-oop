import student

class AttendanceTracker(object):
	# 'date': [students]
	class_attendance = {}

	def __init__(self, Student, date):
		if date in AttendanceTracker.class_attendance.keys():
			student_full_name = Student.first_name +  " " + Student.last_name
			if student_full_name not in AttendanceTracker.class_attendance[date]:
				AttendanceTracker.class_attendance[date].append(student_full_name)
		else:
			AttendanceTracker.class_attendance[date] = [Student.first_name + " " + Student.last_name]

	
	@staticmethod
	def print_attendance(date):
		if date not in AttendanceTracker.class_attendance.keys():
			print("No Records!")
		else:
			attendance_list = AttendanceTracker.class_attendance[date]

			print("Attendance for: " + str(date))
			for student in attendance_list:
				print(student)

# {"18/08/2016": ["arnold okoth", "ruth bochere"]}