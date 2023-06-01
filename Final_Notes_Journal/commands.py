import loadFromFile as lF
import writeToFile as wF
import Note


def add_note():
    title = input("Input the header of the note:\n")
    body = input("Input the description of the note:\n")
    note = Note.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if Note.Note.get_id(note) == Note.Note.get_id(i):
            Note.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Note is added to the journal!")


def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("Notes journal:")
            for i in array_notes:
                print(Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Note.Note.get_id(i))
            id = input("\nInput id of the note: ")
            flag = True
            for i in array_notes:
                if id == Note.Note.get_id(i):
                    print(Note.Note.map_note(i))
                    flag = False
            if flag:
                print("No such ID")

        elif txt == "date":
            date = input("Input date: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Note.Note.map_note(i))
                    flag = False
            if flag:
                print("No such date")
        else:
            print("Notes journal is empty!")


def del_notes():
    id = input("Enter the ID of the note to be deleted: ")
    array_notes = lF.read_file()
    flag = False

    for i in array_notes:
        if id == Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wF.write_file(array_notes, 'a')
        print("Note with id: ", id, " has been successfully deleted!")
    else:
        print("no such id")


def change_note():
    id = input("Enter the ID of the note to change: ")
    array_notes = lF.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Note.Note.get_id(i):
            i.title = input("change the header:\n")
            i.body = input("change the description:\n")
            Note.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        wF.write_file(array_notes_new, 'a')
        print("Note with id: ", id, " has been successfully changed!")
    else:
        print("no such id")
