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
		i.e the get(note_id) method
		"""
		note2=NotesApplication("Brian")
		note2.create("note content A")
		with self.assertRaises(IndexError):
			note2.get(10)

	def test_search_method(self):
		"""
		Tests for method search(search_text)
		i.e Searching for text in an empty list
		"""
		note3=NotesApplication("kevin")
		self.assertEqual(note3.search("unavailable"), "Empty List", msg="The Text is not Available")

	def test_search_method2(self):
		"""
		Tests for method search(search_text)
		i.e Searching for text that  exists
		"""
		note3=NotesApplication("kevin")
		note3.create("This is available")
		self.assertEqual(note3.search("available"), "Found Search Text", msg="The Text is not Available")

	def test_delete_note(self):
		"""
		Test to delete from an index that Exists
		"""
		note4=NotesApplication("Mike")
		note4.create("New note")
		note4.create("Another New note")
		self.assertEqual(note4.delete(1), "Deletion Done", msg="Deletion Failed")


	def test_delete_note2(self):
		"""
		Test to delete from an index that does not Exists
		"""
		note4=NotesApplication("Mike")
		note4.create("New note")
		note4.create("Another New note")
		with self.assertRaises(IndexError):
			note4.delete(20)


	def test_edit(self):
		"""
		Test for edit i.e Editting an index that does not exist
		"""
		note5=NotesApplication("Ken")
		with self.assertRaises(IndexError):
			note5.edit(5, "New Content")

	def test_edit2(self):
		"""
		Test for edit i.e Editting an index that Exists
		"""
		note5=NotesApplication("Ken")
		note5.create("Note A")
		note5.create("Note B")
		note5.create("Note C")
		self.assertEqual(note5.edit(0, "New Content"), "Editting Successful", "Editting Note Failed")

	def test_edit3(self):
		"""
		Test for edit i.e Trying to Edit by Providing empty content
		"""
		note5=NotesApplication("Ken")
		note5.create("Note A")
		note5.create("Note B")
		note5.create("Note C")
		with self.assertRaises(ValueError):
			note5.edit(2, "")
	

	

if __name__ == "__main__":
	unittest.main()

	