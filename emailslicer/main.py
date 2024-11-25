email=input("Give your email : ")  
username=email[:index]
domain=email[email.index("@") + 1:]

print(f"your username is {username} and domain is {domain}")