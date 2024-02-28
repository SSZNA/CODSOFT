class ContactBook(list):
    def AddContact(self,contact):
        self.append(contact)
    def SearchContact(self,name):
        print("Details of contact searched:")
        Contactsfound=ContactBook()
        for item in self:
            if name == item[0]:
                Contactsfound.append(item)
        return Contactsfound
    def UpdateContact(self,name,updated):
        for contact in self:
            if name == contact[0]:
                contact[0]=updated[0]
                contact[1]=updated[1]
                contact[2]=updated[2]
                print("Contact has been updated successfully!")
                return
        print("Contact is not found!")
    def DeleteContact(self,name):
        Contactfound=False
        for contact in self:
            if name == contact[0]:
                self.remove(contact)
                print("Contact deleted successfully!")
                Contactfound=True
                break
        if not Contactfound:
            print("Contact not found for deletion!")

    def __str__(self):
        string="Name,Phone Number,Email Address:\n"
        for item in self:
            string+=item[0]+", "+item[1]+", "+item[2]+"\n"
        return string

def WriteInFile(contactlist):
    with open("contactbook.txt","w")as f:
        for contact in contactlist:
            f.write(f"{contact[0]},{contact[1]},{contact[2]}\n")
        f.write("\n")

def SaveContactsInFile():
    contacts = ContactBook()
    try:
        with open("contactbook.txt", "r") as f:
            lines = f.readlines()
            ContactData = [line.strip().split(",") for line in lines if line.strip()]
            for info in ContactData:
                contacts.append(info)
    except FileNotFoundError:
        with open("Contactlist.txt", "w") as f:
            pass
    return contacts

def UserInterface():
    print("WELCOME TO YOUR CONTACT BOOK")
    contactlist=SaveContactsInFile()
    while True:
        print("1. Add Contact")
        print("2. View Contact list")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        ValidChoice=["1","2","3","4","5","6"]
        choice=input("Enter choice: ")
        if choice in ValidChoice:
            if choice == "1":
                name=input("Enter name: ")
                if not isinstance(name,str):
                    raise TypeError("Invalid format for name!")

                try:
                    number = int(input("Enter number: "))
                except ValueError:
                    print("Invalid entry for number!")
                    continue

                email=input("Enter email: ")
                contactlist.AddContact([name,number,email])
                WriteInFile(contactlist)
            elif choice == "2":
                if not contactlist:
                    print("There are no contacts in the contact book!")
                else:
                    print(contactlist)
            elif choice == "3":
                name=input("Enter name of contact to be searched: ")
                if not isinstance(name, str):
                    raise TypeError("Invalid format for name!")
                contactsfound=contactlist.SearchContact(name)
                if contactsfound:
                    print(f"Contacts with name {name}: ")
                    print(contactsfound)
                else:
                    print("No contact found!")
            elif choice == "4":
                name = input("Enter name of contact to be updated: ")
                if not isinstance(name, str):
                    raise TypeError("Invalid format for name!")
                NewName = input("Enter new name: ")
                if not isinstance(NewName, str):
                    raise TypeError("Invalid format for name!")
                try:
                    NewNumber=int(input("Enter new number: "))
                except ValueError:
                    print("Invalid entry for number!")
                    continue
                NewEmail = input("Enter new email: ")
                contactlist.UpdateContact(name,[NewName,NewNumber,NewEmail])
                WriteInFile(contactlist)
            elif choice == "5":
                name = input("Enter name of contact to be deleted: ")
                if not isinstance(name, str):
                    raise TypeError("Invalid format for name!")
                contactlist.DeleteContact(name)
                WriteInFile( contactlist)
            elif choice == "6":
                break
        else:
            print("Choice is Invalid!")

        Furtherchanges=input("Do you want to make further changes in your contact book?(Y/N): ")
        if Furtherchanges.upper()!="Y":
            exit()
        else:
            UserInterface()

UserInterface()











