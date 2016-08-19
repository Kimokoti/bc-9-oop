class NotesApplication(object):

    def __init__(self, author):
        self.author = author
        self.notes = []

    def create(self,note_content):
        if type(note_content) == str and len(note_content) > 0:
            self.notes.append(note_content)
            return "Note Created"
        else:
            raise TypeError

    def list(self):
        notes=self.notes
        if len(notes) > 0:
            for note in notes:
                print("Note ID:" + str(notes.index(note)))
                print(note)
                print("By Author " + self.author)
            return "Listing Successful"
        else:
            return "No notes Available"

    def get(self, note_id):
        notes=  self.notes
        if notes[note_id]:
            return notes[note_id]
        else:
            raise IndexError

    def search(self, search_text):
        print("Showing results for search {0}".format(search_text))
        notes = self.notes
        if len(notes) > 0:
            for note in notes:
                if search_text in note:
                    print("Note ID: " + str(notes.index(note)))
                    print(note)
                    print("\n")
                    print("By Author "+self.author)
                    return "Found Search Text"
                else:
                    return "Text not Found"
        else:
            return "Empty List"

    def delete(self, note_id):
        if self.notes[note_id]:
            del(self.notes[note_id])
            return "Deletion Done"
        else:
            raise IndexError

    def edit(self, note_id, new_content):
        notes=self.notes
        if notes[note_id]:
            if len(new_content.strip()) > 0 or new_content == None:
                notes[note_id] = new_content
                return "Editting Successful"
            else:
                raise ValueError
        else:
            raise IndexError


print("Enter a Command Number to Choose Action:")
print '''
    1. Create Note
    2. List Notes
    3. Get a Note
    4. Search text from a Note
    5. Delete a Note
    6. Quit
'''
name = str(raw_input("Enter Author Name:"))
if len(name) > 0 and type(name) == str:
    author1 = NotesApplication(name)
    while True:
        command = raw_input("Enter Command Number: ")
        
        # if type(command) == int:
        if command == '1':
            note = str(raw_input("Enter Note: "))
            if type(note) == str and len(note) > 0:
                author1.create(note)
        elif command == '2':
            listing = author1.list()
            if listing != "Listing Successful":
                print(listing)
        elif command == '6':
            break
        elif command == '3':
            try:
                note_id = int(raw_input("Enter List Index: "))
                print(author1.get(note_id))
            except IndexError:
                print("The Note Id does not Exist")
            except TypeError:
                print("Please Enter a Number for index")
        elif command == '4':
            search_text = raw_input("Enter Search text to Search from Notes: ")
            if len(search_text) > 0:
                result = author1.search(search_text)
                if result != "Found Search Text":
                    print(result)
        elif command == "5":
            try:
                index = int(raw_input("Enter Index of Note to Delete: "))
                deletion = author1.delete(index)
                print(deletion)
            except TypeError:
                print("Please Enter a Number")
            except IndexError:
                print("The Index Entered Does not Exist")
        else:
            print("Invalid Choice. Enter a number from 1 to 6")



