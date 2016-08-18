import attendance_tracker
import datetime

map_ = {
	'KE': 'Kenya',
	'NG': 'Nigeria',
	'UG': 'Uganda',
	'TZ': 'Tanzania'
}

class Student(object):
	count = 0

	def __init__(self, first_name, last_name, cc='KE'):
		Student.count = Student.count + 1

		self.id = Student.count
		self.first_name = first_name
		self.last_name = last_name
		self.country = map_[cc]


	def attend_class(self, **kwargs):
		'''
		default values:
			loc = 'Hogwarts'
			date = 'current_date'
			teacher = 'Alex'
		'''
		if not kwargs['loc']:
			loc = 'Hogwarts'
		else:
			loc = kwargs['loc']

		if not kwargs['teacher']:
			teacher = 'Hogwarts'
		else:
			teacher = kwargs['teacher']

		if not kwargs['date']:
			date = datetime.date.today()
		else:
			date = kwargs['date']

		attend_class = attendance_tracker.AttendanceTracker(self, date)

