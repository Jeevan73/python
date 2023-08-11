contacts={}
def createcontact():
    name=input('Enter conact name:')
    number=int(input('Enter contact number'))
    contacts[name]={'number':number}
    print('contact successfully added')
def searchcontact():
    name=input('enter contact name to search:')
    if name in contacts:
      contact=contacts[name]
      print(f"name:{name},number:{contact['number']} ")
    else:
       print('contact not found')
def deletecontact():
    name=input('enter contact name to delete:')
    if name in contacts:
       del contacts[name]
       print('contact deleted succesfully')
    else:
      print('contact not found')
while True:
   choice=int(input('''
     press 1 add new contact:
     press 2 search contact:
     press 3 delete contact:
      '''))
   if choice == 1:
      createcontact()
   elif choice == 2:
      searchcontact()
   elif choice == 3:
      deletecontact()
   else:
      print(f'this {choice} choice is not valid','please enter choice 1 to 3/n')
  