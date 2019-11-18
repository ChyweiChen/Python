class Contact:
    contacts_list = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.contacts_list.append(self)
    # End Init

# End Class
