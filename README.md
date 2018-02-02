## Flitter 

Welcome to my recreation of Twitter on Flask. This assumes you have the latest version of Python3 and Flask.

#### Step 1: Clone the repository

Run `$ git clone https://github.com/rodcoelho/flask-twitter.git` in your terminal.

#### Step 2: Set up database

1) `$ chmod +x ./setup.sh` 
2) `$ chmod +x ./run.sh`
3) `$ ./setup.sh`

This creates the sqlite3 database in `db/twitter.db` and allows the application to store tweets and track users

#### Step 3: Launch the website

Run `$ ./run.sh` on your terminal

On your browser visit: `http://127.0.0.1:5000/`

Sign In to create a user - then tweet away. To log out or switch users just click the Home button.

#### Step 4: Close the application

In your terminal, press Control+C to terminate the app.