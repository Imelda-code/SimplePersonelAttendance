Monday, 07th September 2020
I. Introduction
The aim of this task was to create a program that will automatically take image captures of a user in the
process of filling a form. The captures should be continuously taken at a time interval of five (5) seconds
and should be stored in a database as well as the form data information of the user.
II. Requirements
This task was performed using Python language and we made use of the following libraries
 Tkinter for the user interface
 Opencv for the pictures
III. Implementation
In order to achieve our objective, the following steps were followed:
 We developed a GUI to ease interaction
 We created a SQlite database to store the required information
 We created an access to the webcam for pictures and made use of threads to run simultaneously
the two windows
 At the end, we provided an executable file for the installation of the application
1. GUI( Graphical User Interface)
It is a form containing user information such as his first name, last name, gender and status.Before displaying the above form, a pop-up message first appears to check the approval of the user;
When the user finally approves by using clicking the “Yes” button, the web camera lights on and starts
taking captures of the user while he fills the formOnce the user is done with filling the form all the opened windows shut down. He submits the form data
which is saved in the database. The link to the image is also stored.
2. Database Structure
IV. Conclusion
The task of creating a program that associates form filling by a user to image capture from a web camera
was a successful one. The user information, including his picture and the date of form filling , is
successfully stored in our SQlite database.
