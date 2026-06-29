def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!\n")
    

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            print("\nYour Notes:")
            for index, line in enumerate(file, 1):
                print(f"{index}. {line.strip()}")
        print()
    except FileNotFoundError:
        print("No notes found yet.\n")
        
def main():
    while True:
         print("1. Add Note")
         print("2. View Notes")
         print("3. Exit")
         choice = input("Choose: ")
         
         if choice == "1":
             add_note()
         elif choice == "2":
             view_notes()
         elif choice == "3":
             break
         else:
             print("Invalid choice\n")
    
main()