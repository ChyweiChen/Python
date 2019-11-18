emails = ("Damian.Gordon@dit.ie", "You@student.dit.ie")

message = {
    'subject': "You Have Mail!",
    'message': "Here's some mail for you!"
}

template = """

From: <{0[0]}>
To: <{0[1]}>
Subject: {1[subject]}
{1[message]}"""

print(template.format(emails, message))
