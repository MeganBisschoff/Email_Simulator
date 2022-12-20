# --------------- INSTRUCTIONS --------------- #
'''
An Email Simulation:
Create a class definition for an Email which has four variables:
  has_been_read, email_contents, is_spam and email_address.
The constructor should initialise the sender's email address.
The constructor should also initialise has_been_read and is_spam to false.
Create a function in this class called mark_as_read which should change
  has_been_read to true.
Create a function in this class called mark_as_spam which should change
  is_spam to true.
Create a list called inbox to store all emails (note that you can have a 
  list of objects).
Then create the following methods:
  > add_email - which takes in the contents and email address from the
      received email to make a new Email object.
  > get_count - returns the number of messages in the store.
  > get_email - returns the contents of an email in the list. For this, allow
      the user to input an index i.e. get_email(i) returns the email stored
      at position i in the list. Once this has been done, has_been_read
      should now be true.
  > get_unread_emails - should return a list of all the emails that haven't
      been read.
  > get_spam_emails - should return a list of all the emails that have been
       marked as spam.
  > delete - deletes an email in the inbox.
Now that you have these set up, let's get everything working!
Fill in the rest of the logic for what should happen when the user inputs
  send/read/quit. Some of it has been done for you.
'''

# --------------- TASK --------------- #

# ----- Class & Methods ----- #

# Class to create new Email object.
class Email():

    # Initialise class variables for emails. 
    has_been_read = False 
    is_spam = False

    # Initialise instance variables for emails.
    def __init__(self, email_address, email_contents):
        self.email_address = email_address
        self.email_contents = email_contents
        
    # Method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):    
        self.has_been_read = True
        return self.has_been_read

    # Method to change 'is_spam' emails from False to True.
    def mark_as_spam(self):
        self.is_spam = True
        return self.is_spam

# ----- Databases ----- #

# Lists to store all email objects.
inbox = []
unread = []
spam = []
sent = []       
trash = []      

# ----- Functions ----- #

# Function to get the number of emails from the stored list.
def get_count():
    return len(inbox)

# Function to create a new Email object with constructors properties.
def add_email(email_address, email_contents):

    # Create and append 'Email()' object, with constructors properties
    #   'email_address' and 'email_contents', to the inbox list.
    inbox.append(Email(email_address, email_contents))

# Function to return the contents of a selected email in the list.
def get_email():

    # Enumerate inbox to assign an 'email_num'ber so that the user
    #   can input 'email_choice' to view/open.
    print("\n__________ View Email __________\n")
    for email_num, email in enumerate(inbox):
        print(f"Number:\t{email_num} \nFrom:\t{email.email_address} \nEmail:\t{email.email_contents}\n")
    
    email_choice = int(input("\nEnter the number of the email that you would like to open: ")) #2

    # Loop through inbox then call method to take users 'email_choice'
    #   and 'mark_as_read'.
    # Remaining emails are appended to the 'unread' list
    #   for the 'get_unread_emails()' function below.
    for i in range(len(inbox)):
        if i == email_choice:
            inbox[email_choice].mark_as_read()
        elif i != email_choice:
            unread.append(inbox[i])

            # Display/open the users selected email.
            print(f"\n__________ Email {email_choice} __________\n"
            f"\nFrom:\t{inbox[email_choice].email_address} \nEmail:\t{inbox[email_choice].email_contents}\n")

            # Offer user options on action to take on email.
            email_action = input("Would you like to 'D'elete email or 'M'ark as spam: ").lower()
            if email_action == 'd':
                delete()
                break
            elif email_action == 'm':
                Email.mark_as_spam()
                break

# Function to return a list of all the emails that haven’t been read.
def get_unread_emails():

    # Check if/else there are emails in the 'unread' list.
    # Notify if there aren't, else display emails.
    if len(unread) == 0:
        print("\nThere are no unread emails. Go to inbox to first 'V'iew then 'R'ead emails.")
    elif len(unread) > 0:

        # Loop through 'unread' list and index the 'email_address' and 
        #   'email_contents' instance variables to print 'unread' emails.
        print("\n__________ Unread Emails __________\n")
        for emails in unread:
            print(f"From:\t{emails.email_address} \nEmail:\t{emails.email_contents}\n")


# Function to return a list of all the emails that have been marked as spam.
def get_spam_emails():
    
        # Check if/else there are emails in the 'spam' list.
        # Notify if there aren't, else display emails.
        if len(spam) == 0:
            print("\nThere are no spam emails. Go to inbox to first 'V'iew then 'M'ark as spam.")
        else:

            # Loop through 'spam' list and index the 'email_address' and 
            #   'email_contents' instance variables to print 'spam' emails.
            print("\n__________ Spam Emails __________\n")
            for emails in spam:
                print(f"From:\t{emails.email_address} \nEmail:\t{emails.email_contents}\n")

# Function to delete a selected email.
def delete():

    # Enumerate inbox to assign an 'email_num'ber so that 
    #   user can input 'email_choice' to be deleted.
    print("\n__________ Delete Email __________\n")
    for email_num, email in enumerate(inbox):
        print(f"Number:\t{email_num}\nFrom:\t{email.email_address}\nEmail:\t{email.email_contents}\n")
    
    email_choice = int(input("Enter the number of the email that you would like to delete: ")) 

    # Loop through 'inbox' list and index the 'email_choice' to be deleted.
    # Display deletion notification and create variable of 'deleted_email'.
    # (Do above before deleting else it goes to next email index.)
    # Then pop off 'email_choice' from 'inbox' and 
    #   append 'deleted_email' to 'trash' list.
    for i in range(len(inbox)):
        if i == email_choice:
            print(f"\nEmail {email_choice} from {inbox[email_choice].email_address} was successfully deleted!")
            deleted_email = (inbox[email_choice].email_address, inbox[email_choice].email_contents)

            inbox.pop(email_choice)
            trash.append(deleted_email)

            # (This is an added extra to show the emails in the trash folder)
            # Loop through 'trash' list and then index 'From' and 'Email'.
            print(f"\n__________ Trash Emails __________\n")
            for emails in trash:
                print(f"From:\t{emails[0]} \nEmail:\t{emails[1]}\n")

# ----- Email Program ----- #
def email_program():

    print("\n__________ Email Program __________\n")

    # Call 'add_email' function and populate the program with sample inputs.
    add_email('napolean.hill@gmail.com', "Your daily dose of inspiration: \n\t\"If you cannot do great things, do small things in a great way.\"\n\t - Napolean Hill")
    add_email('maya.angelou@gmail.com', "Your daily dose of inspiration: \n\t\"Success is liking yourself, liking what you do, and liking how you do it.\"\n\t - Maya Angelou")
    add_email('nelson.mandela@gmail.com', "Your daily dose of inspiration: \n\t\"It always seems impossible until it's done.\"\n\t - Nelson Mandela")

    # Notify user of the amount of emails in the inbox.
    print(f"You have {get_count()} emails in your Inbox\n")

    user_choice = ""
    # Prompt for 'user_choice' and call corresponding functions.
    while user_choice != "q":
        user_choice = input('''Would you like to
        'V'iew read and unread emails
        'M'ark spam emails
        'D'elete emails
        'S'end an email
        'Q'uit application
        Enter selection: ''').lower()
        
        # 'V'iew read and unread emails.
        if user_choice == "v":

            view_choice = input("\nWould you like to view 'R'ead emails or 'U'nread emails: ").lower()
            if view_choice == 'r':
                get_email()
            elif view_choice == 'u':
                get_unread_emails()
            else:
                print("Invalid entry.")

        # 'M'ark spam emails
        elif user_choice == "m":
            mark_spam()
            
        # 'D'elete emails
        elif user_choice == 'd':
            delete()

        # 'S'end email
        elif user_choice == "s": 

            # Prompt user to input 'email_address' and 'email_message' to send.
            email_address = input("\nEnter the email address: \n")
            email_message = input("\nWrite your email message: \n")

            ### Functionality can be extended here to create outgoing email objects.###

            # Email is appended to 'sent' list.
            send_email= (email_address, email_message)
            sent.append(send_email)

            # (This is an added extra to show the emails in the sent folder)
            # Loop through 'sent' list and then index 'From' and 'Email'.
            print("\n__________ Sent Emails __________\n")
            for emails in sent:
                print(f"From:\t{emails[0]} \nEmail:\t{emails[1]}\n")

        # 'Q'uit application
        elif user_choice == "q":
            print("\nGoodbye!")

        else:
            print("\nOops! Incorrect input, please try again.\n")

# --- Run program --- #
email_program()
