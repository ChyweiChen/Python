template = """

From: <{from_email}>
To: <{to_email}>
Subject: {subject}
{message}"""

print(template.format(

    from_email = "Damian.Gordon@dit.ie",
    to_email = "You@student.dit.ie",
    message = "Here's some mail for you. "
    " Hope you enjoy the message!",
    subject = "You have mail!"

))
