## Getting Started
To install all dependencies use [pip](https://pip.pypa.io/en/stable/) to read all packages from `requirements.txt` with the command:
> pip3 install -r requirements-temp.txt

## Navigating the Workshop
#### Quick Back-ends for Data Project MVPs (ST22)
To partipate and navigate through all notebooks that were part of the this TechLabs Berlin Workhop Weekend ST22 talk, go through the items in the following order:
1. Go through the [Hero Data Mocking Workshop](binder/01-data_mocking.ipynb)
2. Go through the next sections on [Flask](#Flask) and [Heroku](#Heroku) where we wrap the model in to a Flask application and serve it on Heroku
3. See [Setup](#Firebase) guide for Firebase
4. Finally, learn how to attach a [DB back-end to your service with FireBase](binder/03-working_with_firebase.ipynb)
### Past Workshop Weekends
#### Fake it, till you make it: Prototyping for Data Projects (ST21)
- Contains `streamlit` code used in workshop demonstration
- Simple "Hero" dashboard example

## Flask
[Flask](https://flask.palletsprojects.com/en/2.1.x/) is a web framework, it’s a Python module that lets you develop web applications easily. A Web Application Framework or a simply a Web Framework represents a collection of libraries and modules that enable web application developers to write applications without worrying about low-level details such as protocol, thread management, and so on.
#### Installing Flask dependencies
If you have previously run the command to install all package dependenciees with pip, no additional steps need be taken. You can manually install Flask with the command:
> pip3 install flask

#### Running the Flask server
To make any changes to your developmental service, make all changes to the file `app/main.py`. To serve the API endpoints as defined in the follow, simply run (from root directory of repo):
> python3 app/main.py


## Heroku
[Heroku](https://dashboard.heroku.com/apps) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. It is one of the platforms of choice to deploy small, simple apps on a quick tier. We will be using it as part of this workshop to deploy our application to the cloud and make it available to anyone over the internet.

#### Installing the Heroku CLI
To register commands with our cloud platform we will be using the Heroku CLI. Since the installation can get a bit hairy, we will not walk through it as part of the workshop.

We recommend all Mac users install the Heroku CLI using HomeBrew with the command:
> brew tap heroku/brew && brew install heroku

For Ubuntu users, you can install the CLI using curl:
> curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

Windows Users and other OS are supported and [documentation](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli) can be found on the website.

#### Get Started with the Heroku CLI
After you install the CLI, run the `heroku login` command.
> heroku login

This will alow you to authenticate your account via a browser window so that the CLI can store your credentials. Yoou are now setup to work with the Heroku CLI.

#### Deploying to Heroku
1. Create a new app using the Heroku dashboard.
2. Go to your application code repo and set up a new remote to your newly created repo `test-app`:
    > heroku git:remote -a save-nyc-demo
3. Now simply, push your application code from the `main` branch to this remote:
    > git push heroku main

And that should deploy your application. Fetch the URL from the logs/terminal output on deploy.

## Firebase
#### Setup
1. Sign-up for a [Firebase](firebase.google.com) account
2. On your [dashboard](https://console.firebase.google.com/), Add a project.
3. Follow the setup flow to name your project `save-nyc-demo`
4. You will need application credentials to work with app, this can be generated from your [admin console](https://console.firebase.google.com/project/save-nyc-demo/settings/serviceaccounts/adminsdk)
5. The "Generate new private key"  button will let you generate a credentials file. Download and move the credentials file under `configs` with the file name `app_creds.json`
6. Navigate to [Firestore](https://console.firebase.google.com/u/0/project/save-nyc-demo/firestore) and Create a database.
    - When prompted select "Start in **test mode**"
    - The Cloud Location of the DB is arbitrary

#### Install `firebase-admin`
Once again, if you have setup the project correctly, you should already have this package. Else:
> pip3 install firebase-admin

#### Learning to work with `firebase`
The last section of the workshop talk can be followed [here](binder/workshop_weekend_st22/03-working_with_firebase.ipynb).

## Conclusion
That should be everything you need in order to complete the workshop. Happy learning!
