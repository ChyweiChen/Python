class Contact:
    contacts_list = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.contacts_list.append(self)
    # End Init
# End Class

class Supplier(Contact):
   def order(self, order):
       print("The order will send our "
             "'{}' order to '{}'".format(order,self.name))
   # End order.

# End Class

c1 = Contact("Tom StaffMember", "TomStaffMember@MyCompany.com")
c2 = Contact("Fred StaffMember", "FredStaffMember@MyCompany.com")
s1 = Supplier("Joe Supplier", "JoeSupplier@Supplies.com")
s2 = Supplier("John Supplier", "JohnSupplier@Supplies.com")

print (" ")
print ("* CONTACT INFORMATION *")
print ("-----------------------")
print (" ")
print("Our Staff Members are:")
print(c1.name, " ", c2.name)
print (" ")
print("Their email addresses are:")
print(c1.email, " ", c2.email)
print (" ")

Rtn = input("\nPress Return to continue\n")

print (" ")
print ("* SUPPLIER INFORMATION *")
print ("-----------------------")
print (" ")
print("Our Suppliers are:")
print(s1.name, " ", s2.name)
print (" ")
print("Their email addresses are:")
print(s1.email, " ", s2.email)
print (" ")

Rtn = input("\nPress Return to continue\n")

print ("ORDERING FROM SUPPLIERS")
print ("-----------------------")
print (" ")
print ("We can order from any of the suppliers:")
s1.order("Bag of sweets")
s2.order("Boiled eggs")
print (" ")

Rtn = input("\nPress Return to continue\n")

print ("ORDERING FROM CONTACTS")
print ("-----------------------")
print (" ")
print ("But if we try to order from other contacts it won't work:")
c1.order("Bag of sweets")
c2.order("Boiled eggs")
