
# NYU Python Capstone Project Proposal

## Using Principles of Object Oriented Programming in Python to build a deployable app in Django



This project consists of building an app that is essentially a front end interface for administrators at the City University of New Yorks (CUNY) tutoring program to store and manage data about the tutors they hire, and the locations they scheduling tutoring sessions. The app uses a Django 1.11.1 web framework to interact with a PostgreSQL database. Much of the data that the tutoring app interacts with is homogeneous, in the sense that it is created, edited, and displayed the same way, regardless of the type of data this is (i.e; information about a person, or information about a place). To reduce code redundancy in the app, my project will be centered on building classes of web page views that can take the data relevant to a clients request, and using that data as an argument to a generic view building class object. The goal of the project is to build an app in readable and modular code, using tools included in Djangos library, and employing principles of object oriented programming (encapsulation, inheritance, and polymorphism). This project will also explore storing data in a relational database, and efficient ways for the developer and app user to interact with that data in various ways.
 
- A view of all tutoring locations ( in the app they are called Sites) with a corresponding list of each Sites tutors.
- A view of all Tutors, with the functionality to click on a Tutor to view their information in more detail, and edit as well.
- A view of all Sites, with the functionality to click on a Site to view its information in more detail, and edit as well.
- A functionality to create and delete Tutors and Sites.
- A backend login requirement, so that certain administrators have access to only certain Tutors and Sites. }
