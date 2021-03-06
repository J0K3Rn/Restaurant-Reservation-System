# Restaurant Reservation System
 COSC4351 - Software Engineering
 
 Project Overview:
 - This is a Restaurant Reservation webapp created using Django. This webapp allows for user accounts, resturant reservation scheduling, and bug reports. 
 - See "Running Locally" section below for running this website on your local machine.

Directories:
- pages: App that contains all backend information regarding page redirections. Currently only thing changed is views.py (Mostly unused. Set to delete)
- templates: directory that holds some basic html code for front-end webpages. Webforms are located in their respective apps
- members: App that holds class information about members
- reservations: App that holds class information for reservations
- tables: App that holds class information for tables
- bugs: App that holds class information for bug reports (User generated)
- reservationSystem: Main django directory that holds settings.py

todo:
- add user stats page, for user to review member points and access rewards
- remove include from reservationSystem/urls.py
- Add more hyperlinks across website
- Create login page that checks for user credentials in database
- update README formatting
- give summary of project in README
- explain files in README
- add more notes to README
- Make more accurate fields for the database data (in the apps models.py) Might be some better datafields and also update the parameters by adding set lengths and requirements
- Migrate everything to a MongoDB database? (Currently sql)
- Test webform login / register account for users
- Test webform for making a reservation

Running Locally:

Open the virtual environment in /Website/ with:
- cd Website/
- source bin/activate

When you're ready to exit the virtual environment:
- deactivate

Run django with:
- cd src/
- python manage.py runserver
