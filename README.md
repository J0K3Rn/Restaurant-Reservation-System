# Restaurant Reservation System
 COSC4351 - Software Engineering

Open the virtual environment in /Website/ with:
- cd Website/
- source bin/activate

When you're ready to exit the virtual environment:
- deactivate

Run django with python3 manage.py runserver

Directories:
- pages: App that contains all backend information regarding page redirections. Currently only thing changed is views.py
- templates: directory that holds all html code for front-end
- members: App that holds class information about members
- reservations: App that holds class information for reservations
- tables: App that holds class information for tables
- reservationSystem: Main django directory that holds settings.py

todo:
- update README formatting
- give summary of project in README
- explain files in README
- add more notes to README
- Make more accurate fields for the database data (in the apps models.py) Might be some better datafields and also update the parameters by adding set lengths and requirements
- Migrate everything to a MongoDB database? (Currently sql)
- Create webform login / register account for users
- add logout button
- Create webform for making a reservation
