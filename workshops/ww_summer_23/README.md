# An Intro to Containerization: Hands-on Tutorial with Docker

> _Working with Dockers and containers has quickly become a handy skill for the best software, data and backend engineers to take control of deploying their own services in the cloud. 💪_
>
> _In this whirlwind introduction we will dive in to basics of this technology and then get hands-on with a toy use-case to see it in action! 🚀_

This walkthrough is a supporting document for the above mentioned talk as part of the TechLabs Berlin Summer 23 Workshop Weekend.

## Setup Instructions

Kindly complete these steps prior to attending the workshop! ❤️️

### Docker

As the title suggests, Docker is our tool of choice for this workshop. It is an open platform that enables development, shipping and productionization of application code in a containerized manner. More about Docker will be covered in our workshop.

**Requirement:** To prepare for the workshop, we request that you download and install the Docker Desktop application. Please follow through all of the download and installation instructions for your operating system. [Get Docker!](https://docs.docker.com/get-docker/)

#### Note regarding installation

For advanced users, feel free to use your tool of choice to install Docker, if you do not already have it on your machine. We currently recommend the interactive installer as the simplest way to get Docker installed on Apple silicon.

### PSQL

In our demo we will be target deploying a simple app with a database. For this purpose we will need to select a database and install the required binaries to work with that database on your local machine.

For this tutorial we will be working with [PostGresSQL](https://www.postgresql.org/)

Please make sure you [download](https://www.postgresql.org/download/) and install `psql` for your operating system. (For mac users we would recommend the "installing with HomeBrew" option.)

### Heroku (Optional)

[Heroku](https://dashboard.heroku.com/apps) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. It is one of the platforms of choice to deploy small, simple apps on a quick tier. We will be using it as part of this workshop to deploy our application to the cloud and make it available to anyone over the internet.

This section is optional since it is mostly to demo deployment and not really a part of the tutorial.

#### Installing the Heroku CLI

Documentation for correct installation of this tool can be found on the official [Heroku Dev Center](https://devcenter.heroku.com/articles/heroku-cli). Please follow all the instructions here to get the tool setup for your operating system.

#### Get Started with the Heroku CLI

After you install the CLI, run the `heroku login` command.
> heroku login

This will alow you to authenticate your account via a browser window so that the CLI can store your credentials. You are now setup to work with the Heroku CLI.

## Navigating the Workshop

That's all for now!

The tutorial will be conducted in our workshop on **Saturday, August 26th at 11 AM CEST.** All further instructions to navigate the tutorial will be provided on that day

We look forward to hosting you all 🌈
