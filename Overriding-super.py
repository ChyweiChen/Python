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

class SupplierCheck(Supplier):
   def order(self, order, balance):
       if balance < 0:
       # THEN
           print("This customer is in debt.")
       else:
           super().order(order)
   # End order.
# End Class

s1 = Supplier("Joe Supplier", "JoeSupplier@Supplies.com")
s2 = Supplier("John Supplier", "JohnSupplier@Supplies.com")
s3 = SupplierCheck("Anne Supplier", "AnneSupplier@Supplies.com")
s4 = SupplierCheck("Mary Supplier", "MarySupplier@Supplies.com")

print ("ORDERING FROM SUPPLIERS")
print ("-----------------------")
print (" ")
print ("We can order from any of the suppliers:")
s1.order("Bag of sweets")
s2.order("Boiled eggs")
s3.order("Coffee", 23)
s4.order("Corn Flakes", -12)
print (" ")

