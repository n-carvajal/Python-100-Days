# 100 Days of Python Code

## Project 29: Password Vault

### Brief

Create a simple program that takes in a user's website login details and saves them to a file for easy referencing later.

### Execution

To run the program execute `python main.py` from a command prompt within the project folder.

### Implementation

The program consists of 4 input fields:

* `Website Name` - User defined field stating the website name for the entry.
* `Website Address` - User defined field stating the website address for the entry.
* `Website Username` - User defined field stating the username for the entry.
* `Website Password` - Either user defined or auto generated field stating the password for the entry.

As well as 2 buttons:

* `Auto Generate` - Generates a random and secure 10 character complex password if user does not wish to provide one and adds it to
the user's clipboard for easy pasting into other applications.
* `Submit Details` - Appends the provided information to `logins.txt` for future referencing.

### Caveats

No field must be left blank.
