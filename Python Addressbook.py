import pickle
from datetime import datetime

class Contact():
    
    def __init__(self, name, number = '', address = '', email = '', note = '',companyname = ' ', companyindustry = ' ',companyphone = ' ',companyemail = ' ',companyaddress = ' ',companyfax = ' '):
        
        self.name = name
        self.number = number
        self.address = address
        self.note = note
        self.email = email
        self.companyname = companyname
        self.companyindustry = companyindustry
        self.companyphone = companyphone
        self.companyemail = companyemail
        self.companyaddress = companyaddress
        self.companyfax = companyfax
        
    def show(self):
        print("Contact Name:     "+ str(self.name))
        print("Contact Number:           " + str(self.number))
        print("Contact Email:   "+str(self.email))
        print("Note about contact:     ")
        print(self.note)
        print("Contact Address:     ")
        print("Company Name:       "+str(self.companyname))
        print("Company Address:    "+str(self.companyaddress))
        print("Company Fax:      "+str(self.companyfax))
        print("Company Industry:     "+str(self.companyindustry))

class Company():

    def __init__(self):
        self.a_book = []

    def add_company(self,companyname, companyindustry,companyphone,companyemail,companyaddress,companyfax):
        add_new1 = Contact(self,companyname, companyindustry,companyphone,companyemail,companyaddress,companyfax)
        self.a_book.append(add_new1)

    def delete(self,i):
        all_len = len(self.a_book) - 1         
        if i > all_len:
            return None
        elif i == all_len:
            self.a_book = self.a_book[:-1]
            self.count -= 1
        else:
            self.a_book = self.a_book[:i] + self.a_book[i+1:]
            self.count -= 1

    
   
class Manage():

    def __init__(self):
        self.a_book = []
        self.companyList = []
        self.contactList = [] 
        
    def add_company(self,companyname, companyindustry,companyphone,companyemail,companyaddress,companyfax):
        add_new1 = Company()
        self.companyList.append(add_new1)
    
    def add_contact(self,number,email,name,note):
        add_new = Contact(number,email,name,note)
        self.contactList.append(add_new)

    def get_contacts(self):
        self.companyList = []
        self.contactList = []
        read_all = Contact(' ')
        read_all.show()
        
        

    def read_contacts(self):
        
        
        a_book.get_contacts()
    

    
        
    def delete(self,i):
        all_len = len(self.a_book) - 1
        if i > all_len:
            return None
        elif i == all_len:
            self.a_book = self.a_book[:-1]
            self.count -= 1
        else:
            self.a_book = self.a_book[:i] + self.a_book[i+1:]
            self.count -= 1

   

    

def a_guide():
    print("To add a contact, type 'add'")
    print("To see your contacts, type 'read all'")
    print("To delete a contact, type 'del'")
    print("To add a company's information type 'yes'")
    print("To exit your addressbook, type 'exit'")
    
def main():
    a_book = Manage()
    
    print("Welcome to your Addressbook!")
    a_system()
    


def a_system():
    a_book = Manage()
    

    global a_book
    print("To use your addressbook, type 'book'")
    ui = input("Please select an option:    ")
    ui.lower()

    if ui == 'book':
        a_guide()
    
    elif ui == 'yes':
        ui5 = input("Please enter the name of the company: ")
        ui6 = input("Please enter the industry th company is involved in:  ")
        ui7 = input("Please enter the phone number of the company: ")
        ui8 = input("Please enter the email address of the company:     ")
        ui9 = input("Please enter the address of the company:     ")
        ui10 = input("Please enter the fax number of the company:     ")
        a_book.add_company(ui5,ui6,ui7,ui8,ui9,ui10)

    elif ui == 'add':
        
        ui1 = input("Please enter the number of your contact: ")
        ui2 = input("Please enter the email address of your contact:  ")
        ui3 = input("Please enter the name of your contact: ")
        ui4 = input("Add a note about contact:     ")
        a_book.add_contact(ui1,ui2,ui3,ui4)

    elif ui == 'del':
        # delete messages
        ui1 = int(input("What is the number of the contact or company:  "))
        a_book.delete(ui1)
        

    elif ui == 'read all':
        # read all 
        
        a_book.get_contacts()
        
        
       
    elif ui == 'exit':
        # exit
        return None

    else:
        # wrong command
        print("Error. Incorrect command. Try again.")
    # loop

    a_system()

if __name__ == '__main__':
    main()

    
    
