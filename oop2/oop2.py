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

    def delete(self, note_id):
        if self.notes[note_id]:
            del(self.notes[note_id])
            return "Deletion Done"
        else:
            raise IndexError

    def edit(self, note_id, new_content):
        notes=self.notes
        if notes[note_id]:
            if new_content != None or new_content != '':
                notes[note_id] = new_content
                return "Editting Successful"
            else:
                raise ValueError
        else:
            raise IndexError


        