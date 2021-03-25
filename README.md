# pet-hotel-python-backend
This Repo is a demonstration of my abilities to apply the techniques and procedures of learning to a new language. This is a previous assignment where the backend was rebuilt with Python connecting to as React frontend. Pet hotel is a project designed to assist pet hotel employees in keeping track of incoming and current, and outgoing clients. Pets and owners are stored in the database and 

# Members
- [Woody Kromar](https://github.com/wkromar)

# Front End
- [Pet Hotel Front End](https://github.com/wkromar/pet-hotel-python-backend)

 #Built With
    Javascript, React, Redux, Node, Express, HTML, and Passport, Flask, Python

## Create Python Environment
1. create an environment in your project
   python3 -m venv venv

2. install flask
   $ pip install Flask

3. activate the environment
   . venv/scripts/activate

### to quickstart guide

1. export the app
   export FLASK_APP=hello.py
2. use the run flask command when turning on server and ctrl c when shutting down
   flask run
   ctrl c
3. enabling debug mode
   $ export FLASK_ENV=development
   $ flask run
   

 ## Create database and table
 
 Create a new database called `pet-hotel-group-project` and create a `owners` and `pets`table:
Check the `detabase.sql` file within the project for all SQL queries used.

 
 ```SQL
    CREATE TABLE "owners"(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL
);

CREATE TABLE "pets"(
    "id" SERIAL PRIMARY KEY,
    "owner_id" INT REFERENCES "owners" ON DELETE CASCADE,
    "pet_name" varchar,
    "breed" VARCHAR(100),
    "color" VARCHAR(100),
    "check_in" DATE DEFAULT NOW()
);
```

## Deployment


### Heroku Prerequisite
1. Sign up for an account on [Heroku.com](https://www.heroku.com/)
2. Install Heroku CLI by typing `brew tap heroku/brew && brew install heroku` in Terminal

- [Additional installation notes and troubleshooting](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

> Note: Your project also needs to have a git repository.

Run the following commands from within your project folder.

1. Authenticate by typing `heroku login` in Terminal
2. In terminal, navigate to your project folder and type `heroku create`
3. Type `git remote -v` to ensure it added successfully
4. In terminal, type `git push heroku main`
5. You will need to add a MONGO_URI to your config env on heroku.

## Production Build

Before pushing to Heroku, run `npm run build` in terminal. This will create a build folder that contains the code Heroku will be pointed at. You can test this build by typing `npm start`. Keep in mind that `npm start` will let you preview the production build but will **not** auto update.

- Start postgres if not running already by using `brew services start postgresql`
- Run `npm start`
- Navigate to `localhost:5000`

Directory Structure:

- `src/` contains the React application
- `public/` contains static assets for the client-side
- `build/` after you build the project, contains the transpiled code from `src/` and `public/` that will be viewed on the production site
- `server/` contains the Express App

## Aknowledgments
    - Prime Digital Academy for teaching me Full-Stack Development
    - Dane Smith for his constant support
    - Zhu Cohort for their support and positivity
