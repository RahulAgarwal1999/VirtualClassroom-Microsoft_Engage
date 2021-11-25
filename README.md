<h1 align="center">VirtualClassroom</h1>
<h3 align="center">Website Deployed : CLICK HERE</h3>

**We'll cover the following:**

* [System Requirements](#system-requirements)
* [Use Case Diagram](#use-case-diagram)
* [Class Diagram](#class-diagram)
* [Activity Diagrams](#activity-diagrams)
* [Database Schema](#database-schema)

VirtualClassroom is a web platform that gives students an array of digital academic and social tools to stay engaged with their academics and help teaching professional in creating and managing virtual classrooms. 
It gives the faculty in smooth conducting of both online and offline classes alongwith various features such as updating class timetable, posting announcement, posting assignments, taking attendence, updating meeting details, and switching between online and offline class mode.
The student has the options to join the classroom, check announcements, submit the assignments, check attendence, and choose preferred class mode.


<p align="center">
    <img src="/media-files/airline-management-system.png" alt="Airline Management System">
    <br />
    Airline Management System
</p>

### System Requirements

We will focus on the following set of requirements while designing the application:

1. The system will support the creating ,conducting and managing of classes and will enable the interaction between students and faculties.
2. Faculty and student should be able to register and login to the portal and the system should be able to authenticate and save the users data in the database.
3. Faculty should be able to create classroom with all the necessary class details and the system should generate a unique code for each classroom.
4. Faculty should be able to Edit his/her profile.
5. Faculty should be able to update the class timetable.
6. Faculty should be able to join or update the online class meeting link.
7. Faculty should be able to send class invite code to the students through Emails by entering the Student ID.
8. Faculty should be able make any announcements and it should be visible to the student in their class dashboard.
9. Faculty should be able to post an assignment with assignment link and can set a deadline of submission to it.
10. Faculty should be able to mark, update and upload the attendance of those in the classroom.
11. Faculty should have the option to choose the mode of classes (online/offline). If opted for offline classes, faculty should fill the class strength allowed and the vaccination status required for the students.
12. The system should be able to create a offline class object and should set the limit on the number of instances allowed , according to the strength % mentioned by faculty.
13. Students should be able to Edit his/her profile.
14. Students should be able to join the classroom by entering the class code.
15. Students should be able to check class timing, announcements and assignments in the class dashboard.
16. Students after completing the assignment should be able to submit it in their portal and faculty should be able view the assignment answers as well.
17. Students should be able to opt for offline classes for the upcoming classes and the system should check student vaccination status to that of class requirements and  whether the seats are available for assignment for offline mode.
18. Students should be able to view the total class conducted, total class attended, total class missed by them, and their attendance percentage.
19. Faculty and faculty should have the option to view each other profile and can view all academic  information of theirs.

### Use Case Diagram

We have four main Actors in our system:

* **Admin:** Responsible for managing the entire application.
* **System:** Responsible for email notification, authentication and registration.
* **Faculty:** Responsible for registration and login, creating classrooms, opting class mode, sending classroom invites, marking attendance, posting announcements and assignments, and assigning grades to assignments.
* **Student:** Responsible for registration and login, updating personal info with vaccination status, joining classroom, opt for class mode, attending classes, submitting assignment, check attendance status.


Here are the top use cases of the VirtualClassroom:

* **Add/update profile:** Any member should be able to create their profile and fill all the necessary information.
* **Create classroom:** Faculty should be able to create classroom.
* **Join classroom:** Student should be able to join the classroom.
* **Post announcement:** Faculty should be able to post announcement in classroom.
* **Post assignment:** Faculty should be able to upload assignment in the classroom.
* **Submit assignment:** Students should be able to submit the assignment.

Here is the use case diagram of our application - VirtualClassroom:

<p align="center">
    <img src="/media-files/ams-use-case-diagram.svg" alt="Airline Management System Use Case Diagram">
    <br />
    Use Case Diagram for VirtualClassroom
</p>

### Class Diagram

Here are the main classes of our application:

* **Faculty:** Contains authentication related information about the Faculty like FacultyID, name, email and  passwords.
* **Student:** Contains authentication related information about the student like StudentID, name, email and  password.
* **ClassRoom:** Contains all information related to the classroom like classId, className, classDept, etc.
* **System:** Performs various backend functions like user registration, authentication and sending email notifications.
* **Announcement:** Contains all information related to announcement like announcementId, announcementDate, etc.
* **Assignment:** Contains all information related to assignment like assignmentId, assignmentDate, etc.
* **Attendence:** Contains all attendence related details of students


<p align="center">
    <img src="/media-files/ams-class-diagram.png" alt="Airline Management System Class Diagram">
    <br />
    Class Diagram for VirtualClassroom
</p>

<p align="center">
    <img src="/media-files/ams-uml.svg" alt="Airline Management System UML">
    <br />
    UML for Airline Management System
</p>

### Activity Diagrams

**Faculty Activities:** Login, Registration, Edit Profile,  Create Classroom, Send Class Invites, Update Timetable, Post Announcements, Post Assignments, Take Attendence, Choose Class Mode

<p align="center">
    <img src="/media-files/ams-reserve-ticket-activity-diagram.svg" alt="Airline Management System Reserve Ticket Activity Diagram">
    <br />
    Activity Diagram for VirtualClassroom - Faculty 
</p>

* **Student Activities:** Registration, Login, Edit Profile,  Join Classroom, Check Attendence, Submit Assignments, Choose Class Mode

<p align="center">
    <img src="/media-files/ams-cancel-reservation-activity-diagram.svg" alt="Airline Management System Cancel Reservation Activity Diagram">
    <br />
    Activity Diagram for VirtualClassroom - Student
</p>


### Database Schema
Here is the database schema of our application:

<p align="center">
    <img src="/media-files/ams-reserve-ticket-activity-diagram.svg" alt="Airline Management System Reserve Ticket Activity Diagram">
    <br />
    Database Schema for VirtualClassroom
</p>


### Application Deployment

The application is deployed in Heroku and for storage the application is using Cloudinary which is end-to-end image and video-management solution for websites and mobile apps.
To view the deployed application, just click on this link : CLICK HERE
and just follow the Step by Step Guide as shown : CLICK HERE.
AND if you want to clone the project in your local system and use, then check out this section : CLICK HERE


### Project Setup Guide ( If wants to clone in the local system)

**Python Setup:**
* Install Python on your system. Download Link : Click Here 
* An Exe file will be downloaded, open it.
* A dialog box will appear as shown in the figure below. Do not forget to click on the check box of “ADD PYTHON TO PATH”
* Then click on ‘INSTALL NOW’, the installation will be completed.

**Note: ** If you are using Command Line terminal, then restart the terminal to use python
