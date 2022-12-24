# Import essential libraries
from tkinter import *
import tabulate

# create a menu to display to the user and get their choice of action
def menu():
    print("Welcome to the Scheduler")
    print("1. Add a new subject")
    print("2. Delete a subject")
    print("3. View all subjects")
    print("4. Get visual representation of subjects")
    print("5. Save subjects to file")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    return choice

# create a function to add a new identifier, subject to his respective time in the list
def add_subject(subjects):
    identifier = input("Enter the identifier: ")
    subject = input("Enter the subject: ")
    time = int(input("Enter the time: "))
    subjects[time - 7].append(identifier)
    subjects[time - 7].append(subject)
    return subjects

# create a function to delete a subject from the list using the identifier in second position of the list
def delete_subject(subjects):
    identifier = input("Enter the identifier: ")
    for subject in subjects:
        if identifier in subject:
            subject.remove(identifier)
            subject.remove(subject[1])
    return subjects

# create a function to display all the subjects in the list using the tabulate library, taking hour as the first element in the list and the identifier and subject as the second and third element in the list respectively
def view_subjects(subjects):
    print(tabulate.tabulate(subjects, headers=[
          "Time", "Identifier", "Subject"], tablefmt="grid"))
    return subjects

# create a function that saves the subjects in the list to a file using the tabulate library
def save_subjects(subjects):
    with open("subjects.txt", "w") as file:
        file.write(tabulate.tabulate(subjects, headers=[
                   "Time", "Identifier", "Subject"], tablefmt="grid"))
    return subjects

# create a function if they are more than one subject in the list, concatenate the identifiers and subjects in the same row.
def sort_subjects(subjects):
    for i in range(len(subjects)):
        if len(subjects[i]) > 3:
            for j in range(3, len(subjects[i]), 2):
                subjects[i][1] = subjects[i][1] + ", " + subjects[i][j]
                subjects[i][2] = subjects[i][2] + ", " + subjects[i][j + 1]
            for k in range(len(subjects[i]) - 3):
                subjects[i].pop()
    return subjects


# create a function to display the list in a tabulated format using tkinter
def display_subjects(subjects):
    root = Tk()
    # change color of background to white
    root.configure(background="white")
    root.title("Subjects")
    root.geometry("300x450")
    # Display headers with respectivley the time, identifier and subject in white color, and 14 font size
    Label(root, text="Time", bg="white", font=(
        "Arial", 14)).grid(row=0, column=0)
    Label(root, text="Identifier", bg="white",
          font=("Arial", 14)).grid(row=0, column=1)
    Label(root, text="Subject", bg="white", font=(
        "Arial", 14)).grid(row=0, column=2)
    # Display the subjects in the list in the respective row and column
    for i in range(len(subjects)):
        for j in range(len(subjects[i])):
            Label(root, text=subjects[i][j], bg="white",
                  font=("Arial", 12)).grid(row=i + 1, column=j)
    root.mainloop()
    return subjects

# create a main function to run the program
def main():
    # create subject list to store the subjects with three elements in each list (hour, identifier, subject) wich hour is the first element in the list and will be initialised to 7 to 22
    subjects = []
    for i in range(7, 23):
        subjects.append([i])
    # call the menu function to display the menu to the user
    # create a try and except block to catch any errors
    try:
        choice = menu()
        while choice != 5:
            if choice == 1:
                subjects = add_subject(subjects)
            elif choice == 2:
                subjects = delete_subject(subjects)
            elif choice == 3:
                subjects = view_subjects(subjects)
            elif choice == 4:
                subjects = display_subjects(subjects)
            elif choice == 5:
                subjects = save_subjects(subjects)
            elif choice == 6:
                print("Exiting...")
                break
            sort_subjects(subjects)
            choice = menu()
    except:
        print("Error! Please try again.")

# call the main function to run the program
if __name__ == "__main__":
    main()
