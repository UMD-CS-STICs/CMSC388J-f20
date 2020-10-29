# Building Secure Web Applications with Python and Flask

![Flask Logo][logo]

This course is an introduction to building secure, full-stack web applications with Python and Flask.
We'll start with Python and Flask, and then subsequent weeks will cover how to add Flask extensions
to your applications to implement common web app functionalities, how to protect your website from bad actors,
and more! At the end of the course, you'll be able to deploy your app for the world to see.

*Disclaimer: The syllabus is subject to change throughout the course of the semester.*

## Course Details

- **Course**: CMSC388J
- **Prerequisites**: C- or better in CMSC216 and CMSC250
- **Credits**: 1
- **Seats**: 39
- **Lecture Time**: Wednesdays @ 5-6 PM; ASYNCHRONOUS
- **Location**: ONLINE
- **Semester**: Fall 2020
- **Textbook**: No textbook, all materials are provided and documentation is online
- **Course Facilitators**: Yashas Lokesh, Kenton Wong
- **Faculty Advisor**: Michael Marsh
- **Syllabus last updated**: October 28th, 2020
- **Previously offered**: Spring 2020, Fall 2019

## Topics Covered
- Python
  - Variables, expressions, operators
  - Iterations, conditionals, collections
  - Functions
    - As first-class objects
    - Decorators
  - "Main" function
  - Built-in functions
- Web Application Security
  - Cross-site scripting (XSS)
  - Cross-site request forgery (CSRF)
  - SQL injections
  - Man-in-the-Middle attacks (MitM)
  - Token & Two-factor authentication
- Flask
  - Routing your web app
  - Templating
  - Adding extensions for more features
    - WTForms
    - SQLAlchemy
    - Talisman
    - Login
    - Creating your own
  - Logging
  - User Management
  - Blueprints
- HTML/CSS/JS
  - Bootstrap
  - Integrating other frameworks
  - Custom CSS/JS configuration
- Databases
  - SQL
      - SQLite
      - PostgreSQL
  - MongoDB
- Payments Integration
  - Stripe (possibly others, we're open to suggestions)
- App Deployment
  - Heroku
  - Python Anywhere
  - *Possibly*: Google App Engine, AWS
- Version Control
  - Git

## Schedule
| Week | Topic                                          | Assignment                                                         |
| ---- | ---------------------------------------------- | ------------------------------------------------------------------ |
| 1    | Intro to Python                                | Python practice (P1) assigned                                      |
| 2    | Flask Intro                                    | P1 due, P2 assigned, Quiz 1 assigned: weeks 1-2                    |
| 3    | Forms, CSRF                                    | Quiz 1 due                                                         |
| 4    | Databases, Injection Attacks                   | P2 due, P3 assigned, Quiz 2 assigned: weeks 3-4                    |
| 5    | User Management                                | Quiz 2 due                                                         |
| 6    | Bootstrap & more                               | P3 due, P4 assigned, Quiz 3 assigned: weeks 5-6                    |
| 7    | In-depth CSS & JS*                             | Quiz 3 due                                                         |
| 8    | None - break week                              | P4 due                                                             |
| 9    | Extensions, Logging, App Factories, Blueprints | P5 assigned                                                        |
| 10   | HTTP Headers & Talisman                        | Quiz 4 assigned, weeks 7-10                                        |
| 11   | (Pending)                                      | P5 due, Quiz 4 due, Final Project Proposal assigned                |
| 12   | Two-Factor Authentication                      | Proposal due, Final Project assigned, Quiz 5 assigned, weeks 10-12 |
| 13   | THANKSGIVING BREAK                             | Quiz 5 due                                                         |
| 14   | Payments with Stripe*                          |                                                                    |
| 15   | Deploying your app                             |                                                                    |
| 16   | None - finals week                             | Final Project due                                                  |

* See **Flexible Schedule** section below

## Flexible Schedule

Weeks 7 and 14 will have a main topic of discussion, but during these weeks, we'll also try
to teach topics requested by the students. So if you guys feel like you need more info about
a certain topic or just want to learn a new idea altogether, let us know, and we'll try to add it in.

We'll send out information on how you can let us know; surveys will probably be conducted anonymously on ELMS.

## Online Class Schedule
Because classes will be **online** this semester, we will follow an **asynchronous** schedule
and add the slides for the topics of the week to the shared Google Drive folder
in place of having an actual lecture. We will be holding office hours during class time on Zoom.

## Grading

Grades will be maintained on ELMS.
You will be responsible for all material discussed in lecture as well as other standard means of communication
(Piazza, email announcements, etc.), including but not limited to deadlines, policies, assignment changes, etc.

Your final course grade will be determined according to the following
percentages:

| Percentage | Title         | Description                                                 |
| ---------- | ------------- | ----------------------------------------------------------- |
| 10%        | Quizzes       | Weekly quizzes to test knowledge of topics taught in class to help prepare for projects |
| 55%        | Projects      | Weekly projects to test knowledge of topics taught in class |
| 35%        | Final Project | Final project - creating app from scratch                   |

Any request for reconsideration of any grading on coursework must be submitted
within one week of when it is returned. No requests will be considered afterwards.

**Robustness**:

If we perform any typical user actions on the website (e.g., clicking on links, navigating to
different parts of the website using links, navigating to different parts of the website with direct URLs)
and this causes a crash (a Flask error shows up on screen or the app crashes),
then you may lose **up to 50%** of your final score for the project, depending on the severity of the error.

An example of a small error: syntax error in a Jinja template. 

An example of a large error: a view function not being configured properly.

## Quizzes
We will be assigning quizzes on ELMS to make sure you are keeping up with the material you need
in order to complete the projects. They will be assigned after the topics that they cover
and due the following Tuesday, unless stated otherwise, at 11:59 PM.

Each quiz will be scored based on points, and each question will be worth a certain number of points.
All quizzes combined will make up 10% of your final grade.

## Projects
The project is due the day it is scheduled to be due, barring any extensions that may be given out. 
They will be due at 11:59 PM. Not all of
the projects will have tests; they will be graded according to a rubric 
which will also be provided. All projects must be submitted online on ELMS.

Project 1 will be weighted 7%, and projects 2-5 will be weighted 12%.

## Final project

The final project will use everything you have learned in class before and will require you
to build a Flask web application from scratch with a group or individually, and deploy
the app on a hosting platform. Requirements for the final project will come out
towards the end of the semester.

## Late Policy
Projects and Quizzes may be submitted up to three days late for 10% off your earned grade, 
**each day**. After this, no more projects or quizzes will be accepted.

For projects, the highest score you get on each, counting late and on-time submissions,
will be your grade for that project. There are **no exceptions**
unless you've talked with us beforehand or provide a valid excuse.

## Outside-of-class communication with course staff
We'll communicate through students mainly through Piazza and through office hours.

**Office hours**: Wednesdays, 5-6 PM, Zoom

Please use Piazza as your primary communication with us; we'll get back to you
fastest on Piazza. If you absolutely cannot use Piazza, then email us; if you are
emailing Yashas or Kenton, make sure to CC the other. **Additionally**, please include
`[CMSC 388J]` at the start of your subject line so we don't accidentally ignore your email.

Instructor: 

Dr. Michael Marsh - mmarsh@cs.umd.edu

Facilitators:

Yashas Lokesh - yashloke@umd.edu

Kenton Wong - kdubbs0@umd.edu

## Excused Absence and Academic Accommodations
See the section titled "Attendance, Absences, or Missed Assignments" available at
[Course Related Policies](http://www.ugst.umd.edu/courserelatedpolicies.html).

## Disability Support Accommodations
See the section titled "Accessibility" available at
[Course Related Policies](http://www.ugst.umd.edu/courserelatedpolicies.html).

## Academic Integrity
Note that academic dishonesty includes not only cheating, fabrication, and
plagiarism, but also includes helping other students commit acts of academic
dishonesty by allowing them to obtain copies of your work. In short, all
submitted work must be your own. Cases of academic dishonesty will be pursued to
the fullest extent possible as stipulated by the
[Office of Student Conduct](http://osc.umd.edu/OSC/Default.aspx).

It is very important for you to be aware of the consequences of cheating,
fabrication, facilitation, and plagiarism. For more information on the Code of
Academic Integrity or the Student Honor Council, please visit
http://www.shc.umd.edu.

# Course Evaluations
If you have a suggestion for improving this class, don't hesitate to tell the
instructor or facilitators during the semester. At the end of the semester, please don't
forget to provide your feedback using the campus-wide CourseEvalUM system. Your
comments will help make this class better.


[logo]: ./flask-logo.png
**
