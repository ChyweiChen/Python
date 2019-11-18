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
       print("The order will send "
             "’{}’ order to ‘{}’".format(order,self.name))
   # End order.

# End Class

c1 = Contact("Tom StaffMember", "TomStaffMember@MyCompany.com")
c2 = Contact("Fred StaffMember", "FredStaffMember@MyCompany.com")

s1 = Supplier("Joe Supplier", "JoeSupplier@Supplies.com")
s2 = Supplier("John Supplier", "JohnSupplier@Supplies.com")

print("Our Staff Members are:", c1.name, " ", c2.name)
print("Their email addresses are:", c1.email, " ", c2.email)

print("Our Suppliers are:", s1.name, " ", s2.name)
print("Their email addresses are:", s1.email, " ", s2.email)

