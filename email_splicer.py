#Get the user's email address

email = input("What is your email? > ").strip()

#Slice out the user's name

user = email[:email.index("@")]

#Slice out the domain name of the emai

domain = email[email.index("@") + 1 :]

#Format message

output = "Your username is {} and your domain name is {}.".format(user, domain)

#Display output message

print(output)
