class EMail:

    def __init__(self, from_addr, to_addr, subject, message):

        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message

    # END init

# END class

email = EMail("Damian.Gordon@dit.ie", "You@student.dit.ie", "You Have Mail!", "Here's some mail for you!")

template = """
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}

{0.message}"""
print(template.format(email))
