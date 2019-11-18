class ContactList(list):

    def search(self, name):
        "Return any search hits"
        matching_contacts = [ ]

        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            # Endif;
        # Endfor;

        return matching_contacts
    # End Search
# End Class

class Contact(list):

    contacts_list  = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.contacts_list.append(self)
 # End Init

# End Class


class Supplier(Contact):

   def order(self, order):
       print("The order will send our "
             "'{}' order to '{}'".format(order,self.name))
   # End order.

# End Class

class SupplierCheck(Supplier):

   def order(self, order, balance):
       if balance < 0:
       # THEN
           print("This customer is in debt.")
       else:
           print("The order will send our "
             "'{}' order to '{}'".format(order,self.name))
   # End order.

# End Class


s1 = Supplier("Joe Supplier", "JoeSupplier@Supplies.com")
s2 = Supplier("John Supplier", "JohnSupplier@Supplies.com")
s3 = SupplierCheck("Anne Supplier", "AnneSupplier@Supplies.com")
s4 = SupplierCheck("Mary Supplier", "MarySupplier@Supplies.com")

s1.order("Bag of sweets")
s2.order("Boiled eggs")
s3.order("Coffee", 23)
s4.order("Corn Flakes", -12)
