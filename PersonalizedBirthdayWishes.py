print ("This is a birthdy card generator assistant. You need to enter some information for me.")

recipients_name = input("what's the recipient's name? ")
recipients_birth_year= input("what's the recipient's birth year? ")
age=2023-int(recipients_birth_year)
short_personalized_message=input("Add a personalized message: ")
senders_name=input ("put the senders name: ")

print()
print("this is the generated message:")
print()

print(f"""{recipients_name},let's celebrate your {age} years of awesomeness! 
Wishing you a day filled with joy and laughter as you turn {age}!

{short_personalized_message}

With love and best wishes,
{senders_name}""")