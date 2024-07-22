users = []  # Sample user list
history = []

def send(user):
    global msg, receiver
    msg = input("Please enter the message you want to send: ")
    receiver = input("Please enter the name of the user you want to send the message to: ")
    user_activity(msg, receiver, user)

def get_username(user):
    if user in users:
        print(f"Hi {user}, you have logged in successfully.")
        return True
    else:
        print("Invalid username.")
        return False

def user_activity(msg, receiver, user):
    dict1 = {
        "Sender": user,
        "sent_to": receiver,
        "message": msg
    }
    history.append(dict1)
    return dict1

while True:
    user = input("Enter a valid Username: ")

    if get_username(user):
        send(user)
        yes = input("Do you want to see your chatting activity (yes or no)? ")
        if yes.lower() == "yes":
            print(history)
    else:
        print("Please try again with a valid username.")
    
    cont = input("Do you want to continue (yes or no)? ")
    if cont.lower() != "yes":
        break


    

    






