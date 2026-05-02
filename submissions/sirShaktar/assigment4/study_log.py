def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            notes = file.readlines()
            return [n.strip() for n in notes]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def main():
    name = input("What is your name? ")
    print("Welcome", name)

    notes = load_notes("notes.txt")

    while True:
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ")

        if choice == "1":
            note = input("Enter note: ")
            notes.append(note)

        elif choice == "2":
            if len(notes) == 0:
                print("No notes yet")
            else:
                for n in notes:
                    print(n)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()