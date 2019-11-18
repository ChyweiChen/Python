class ContactList(list):

    def search(self, name):
        "Return any search hits"
        matching_contacts = []

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

c1 = Contact("Tom StaffMember", "TomStaffMember@MyCompany.com")
c2 = Contact("Fred StaffMember", "FredStaffMember@MyCompany.com")
c3 = Contact("Anne StaffMember", "AnneStaffMember@MyCompany.com")

SearchName = input("Who would you like to search for?\n")
print([c.name for c in Contact.contacts_list.search(SearchName)])
