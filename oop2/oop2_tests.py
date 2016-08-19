import unittest
from oop2 import NotesApplication

class oop2_tests(unittest.TestCase):

	"""
	Carry out tests for OOP2
	"""
	def test_creation(self):
		"""
		Test if entry is valid 
		"""
		note1=NotesApplication("Brian")
		with self.assertRaises(TypeError):
			note1.create(None)

	def test_listing(self):
		"""
		test for list with content
		"""
		note2=NotesApplication("Brian")
		note2.create("note content A")
		note2.create("note content B")
		self.assertEqual(note2.list(), 'Listing Successful', msg="Listing successful")

	def test_listing2(self):
		"""
		Listing for Empty List
		"""
		note2=NotesApplication("Brian")
		self.assertEqual(note2.list(), 'No notes Available', msg="Empty List, No Notes")

	def test_get_index(self):
		"""
		Retrieve note for index
		"""
		note2=NotesApplication("Brian")
		note2.create("note content A")
		self.assertEqual(note2.get(0), "note content A", msg="Empty List, No Notes")

	def test_get_index2(self):
		"""
		Retrieve note for index that does not Exist
		"""
		note2=NotesApplication("Brian")
		note2.create("note content A")
		with self.assertRaises(IndexError):
			note2.get(10)
			


if __name__ == "__main__":
	unittest.main()

	