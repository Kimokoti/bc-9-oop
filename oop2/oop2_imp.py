from oop2 import NotesApplication

##Console Implementation

print("Enter a Command Number to Choose Action:")
print '''
    1. Create Note
    2. List Notes
    3. Get a Note
    4. Search text from a Note
    5. Delete a Note
    6: Edit a Note
    7. Quit
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

        elif command == '7':
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
            except ValueError:
            	print("Invalid Index. Enter a Number")

        elif command == "6":
            try:
                index = int(raw_input("Enter Index of Note to Edit: "))
                author1.get(index)
                new_note = raw_input("Enter New Note: ")
                result = author1.edit(index, new_note)
                print(result)
            except ValueError:
                print("Invalid index. Please Enter a Number")
            except IndexError:
                print("Index Entered Does not Exist")

        else:
            print("Invalid Choice. Enter a number from 1 to 6")
