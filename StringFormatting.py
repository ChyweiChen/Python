StandardText = "Hello {}, you are currently {}"
print(StandardText.format('Damian', 'asleep'))
print(StandardText.format('Sherlock', 'deducing'))
print(StandardText.format('Tarzan', 'swinging from vine'))

print(" ")

StandardText = "Hello {0}, you are currently {1}. Your name is {0}"
print(StandardText.format('Damian', 'asleep'))
print(StandardText.format('Sherlock', 'deducing'))
print(StandardText.format('Tarzan', 'swinging from vine'))
