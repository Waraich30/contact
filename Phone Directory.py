


contact={}

def display_contact():
  print("Name\t\tContact Number")
  for key in contact:
    print("{}\t\t{}".format(key,contact.get(key)))

while True:
  choice=int(input(" 1.Add a record: \n 2. Search a record: \n 3. Update a record: \n 4. Sort the record alphabetically: \n 5. Delete a record: \n 6.Quit: \n Enter your choice :"))
  if choice== 1:
    name=input("enter the contact name:")
    number=input("enter the number: ")
    print("added to the contact")
    contact[name]=number
  elif choice==2:
    search_name=input("enter the contact name:")
    if search_name in contact:
      print (search_name," contact number is",contact[search_name])
    else:
      print("Name is not founr in the contact book")
  elif choice==4:
    if not contact:
      print("empty contact book")
    else:
      display_contact()
  elif choice==3:
    edit_contact=input("enter the contact you want to edit:")
    if edit_contact in contact:
      number=input("eneter new number:")
      contact[edit_contact]=number
      print("contact updated")
      display_contact()
    else:
      print("name is not found in contact book")
  elif choice==5:
    del_contact= input("enter the contact to be delete:")
    if del_contact in contact:
      confirm=input("do you want to delete this contact y/n:")
      if confirm=='y' or confirm=="Y":
        contact.pop(del_contact)
      display_contact()
    else:
      print("data not found")
  else:
    break



  
