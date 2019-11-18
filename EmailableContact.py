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

class MailSender:

	def send_mail(self, message):
    	     print("Sending mail to " + self.email)
         # e-mail logic here
    # END send_mail.

# END class.

class EmailableContact(Contact,MailSender):
    pass
    # Do stuff
# END class.

e = EmailableContact("John Smith", "jsmith@Company.com")
e.send_mail("Hello, test email")
