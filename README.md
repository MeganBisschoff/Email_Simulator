# Email Simulator

A Python program that simulates email messaging.

## Description

This program allows a user to create and read emails, mark and view spam emails, check unread emails and of course delete emails.

The ```email_program()``` starts the program and populates the *inbox* list using the ```add_email()``` method which takes in the contents and email address from the received email to make a new Email object.

The ```Email``` class is called to create the new Email object and has four variables:

* email_address
* email_contents
* is_spam (initialised to false)
* has_been_read (initialised to false)

A class method ```mark_as_read()``` changes *has_been_read* to true.
The class method ```mark_as_spam()``` changes *is_spam* to true.

Once the inbox is prepared, the user is then presented with options to:

* 'V'iew read and unread emails
* 'M'ark spam emails
* 'D'elete emails
* 'S'end an email

If user selects "v":
The ```get_email()``` function returns the contents of a selected email in the inbox and displays it.
The selected email object is ```mark_as_read()``` and the remaining emails are appended to the *unread* list
The ```get_unread_emails()``` function returns all the emails from the listthat haven’t been read.

If user selects "m":
The ```mark_spam()``` function marks a selected email from the inbox as spam and moves it to the *spam* list.
The user is then asked if they would like to view all spam email. If yes, the ```get_spam_emails()``` function 
returns a list of all the emails in the spam list.

If user selects "d":
The ```delete()``` function removes the selected email from the inbox and moves it to the *trash* list.

If user selects "s":
An ```Email()``` object, with *email_address* and *email_message*, is created. (At this point, although not included in this project, the program's functionality can be extended to create outgoing email objects.) The new email is simply added to the *sent* list.

## Functionality summary

* Create ann send an email
* Read emails
* Mark and view spam emails
* View unread emails
* Delete emails

## Programming principles

This program practices the programming concept of classes in Object Oriented Programming. Furthermore it employs
programming functions such as enumerate, .pop(), append() and a good amount of conditional logic.

## Running the program

Run the email.py file in any Python IDE, such as Visual Studio Code.

## Class preview

```python
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

```

## Console preview

```
__________ Email Program __________

You have 3 emails in your Inbox

Would you like to
        'V'iew read and unread emails
        'M'ark spam emails
        'D'elete emails
        'S'end an email
        'Q'uit application
        Enter selection: v

Would you like to view 'R'ead emails or 'U'nread emails: r    

__________ View Email __________

Number: 0
From:   napolean.hill@gmail.com
Email:  Your daily dose of inspiration:
        "If you cannot do great things, do small things in a great way."
         - Napolean Hill

Number: 1
From:   maya.angelou@gmail.com
Email:  Your daily dose of inspiration:
        "Success is liking yourself, liking what you do, and liking how you do it."
         - Maya Angelou

Number: 2
From:   nelson.mandela@gmail.com
Email:  Your daily dose of inspiration:
        "It always seems impossible until it's done."
         - Nelson Mandela


Enter the number of the email that you would like to open:
```

&nbsp;
***  
_For email, the old postcard rule applies. Nobody else is supposed to read your postcards, but you'd be a fool if you wrote anything private on one._ \~ Judith Martin
***
&nbsp;

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE.

## Author

**Megan Bisschoff** 2022

Project submitted for Software Engineering bootcamp Level 1 Task 27 at [HyperionDev](https://www.hyperiondev.com/)

[View](https://www.hyperiondev.com/portfolio/86596/) submission results.
