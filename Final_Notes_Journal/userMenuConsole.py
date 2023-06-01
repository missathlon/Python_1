import menuTemplates as m


def menu_console():
    m.printNenuTitle("Main menu\n           NOTES JOURNAL")
    print("1 - journal output \n2 - search for a note by id \n3 - search for a note by date\n4 - edit note"
          " \n5 - add note\n6 - delete note\n7 - exit")
    m.printMenuLine()
    print("\n select an item from the menu ")
