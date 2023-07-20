## Navigating the Workshop
### Heroku
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

This will alow you to authenticate your account via a browser window so that the CLI can store your credentials. You are now setup to work with the Heroku CLI.