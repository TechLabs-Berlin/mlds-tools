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

For advanced users, feel free to use your tool of choice to install Docker, if you do not already have it on your machine. We currently recommend the interactive installer as the simplest way to get Docker installed on Apple silicon. Additionally, if you are on Apple Silicon you may also have to download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

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

The following is a walkthrough of all topics, exercise and lessons as part of this introductory tutorial to Dockers and the container paradigm. We also set up a basic introduction to this topic in our [intro slides](theory_slides.pdf).

### Our application

We will be taking a toy example as a use case. As a CS student I often had the problem that outside of outdated tools such as MS Access or OracleDB, we rarely had good tools to practice SQL. Hence to address this need, today 15 years later, I will strive to build a browser based tool in the likes of [SQLBolt](https://sqlbolt.com/) which allows students to play, test and learn SQL. This will be the end deliverable in today's tutorial.

### Pre-flight checks

Let's get started, to begin with the setup, first make sure you have cloned our tutorial repo. For cloning the tutorial repo, use the command:
> $ git clone <https://github.com/TechLabs-Berlin/mlds-tools.git>

Now let's quickly switch to our work directory for this project:
> $ cd mlds-tools/workshops/ww_summer_23

Since we actually plan to make some code changes, let's first switch to a new branch:
> $ git checkout -b workshop

To ensure that we are all set to get started with Docker, let's do one final test. Now that you are in the right working directory, fire up the following command:
> $ docker run hello-world

If Docker was setup correctly, you should see an output like this:

```shell

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.(arm64v8)
 3. The Docker daemon created a new container from that image which runs the executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

If you received any errors, there might be an issue with your installation or Docker setup. We would recommend following along with the workshop and perhaps reaching out to resolve this issue before attempting the tutorial yourself.

### Writing your first Dockerfile

Now let's actually get started with our very first Dockerfile.

#### What is a Dockerfile?

A document that specifies the target that you want to build. Interacting with Docker will mostly require you to learn directives in order to define and manipulate your Docker containers. Let's get started with a very simple example.

#### Creating a Dockerfile

In our project repo, let's create a file and simply name it `Dockerfile`. Now add the following contents to the file and save it:

```docker
FROM postgres:alpine
ENV POSTGRES_PASSWORD docker
```

That's it! Before we take a moment to understand what's really happening in this dockerfile. Let's first see it in action!

#### Some basic Docker commands

To build an image from the Dockerfile you just defined, use the following command:
> docker build -t postgresdb ./

Once the image is built, use the run command to actually run your a fresh docker container using the image you just built.
> docker run --name demodb -p 5432:5432 postgresdb

Now we can start to understand the effect of these commands:

- We built a new docker image from a dockerfile and tagged it for later use
- We ran the command to direct the Docker engine to run the image specified in a new container
- We saw the results: running the container, will start a DB that is awaiting connections at a specific port.

#### Using `psql` to connect to DB

As earlier mentioned, we will be using a CLI tool to connect to our local running database instance. Assuming that you have `postrgesql` and the necessary setup for the same you should be able to connect to our DB with `psql` using the following syntax:
> psql -d postgres -U postgres -h localhost

Entering the password **docker** at prompt will result in a successful connection!

Some basic commands to interact with the DB:

- `\d` will list all tables
- `\q` will quit interactive CLI mode

#### Adding some records to our empty database

To run code for the following exercise, first add the following lines to the bottom of your `Dockerfile` (right after the two existing directives in the file):

```docker
# init db tables that we desire
COPY data/*.csv tmp
COPY *.sql /docker-entrypoint-initdb.d/
```

Now simply, build and run the docker image once again!

Build:
> $ docker build -t postgresdb ./

Run:
> $ docker run -d --name demodb -p 5432:5432 --network OSRNetwork postgresdb

 _**Note:** notice we added an extra option to our command, `-d`_

At this point, you should receive an error when you try to run. It will complain about the container already existing. This is from our previous run. We will want to remove this container.

Remove all idle containers:
> $ docker rm \$(docker ps -a -q)

#### Summary

Now in this short section of exercises:

- We've learnt how to build images, run and connect to docker conatiners
- We've understood the base `postgresdb` image and how to madd data to a running DB
- Connect and mange data with CLI tools!

You can find a cheatsheet reference like the one [this](https://dockerlabs.collabnix.com/docker/cheatsheet/), to collect all useful commands in one place!

### A flexible tool for development

In this section we will focus on illustrating how armed with the limited knowledge of a few commands and docker directives, you can already start to develop some production grade applications. Let's get started!

#### All about that Flask

Popular pythonic service to setup an easy web server. In this section of this tutorial, we will focus on how Docker can be used as re-producible environment for local development and testing. We will build a browser-based interface to query our previously defined database.

Simply spin up the predefined Dockerfile we have provided for this purpose:
> docker build -f dockerfiles/app.Dockerfile -t webapp . --no-cache

And now run the container:
> docker run --name sqlrunner -p 5050:5050 webapp

#### Oh, oh! Our first major issue

If you tried running your flask application, you noticed that despite us launching the container and it running successfully we are still encountering an error when we try to navigate to our website. You should see a similar error:
```UnboundLocalError: cannot access variable 'connection' where it is not associated with a value```

This is simply because our Flask app is running in a container and the DB is in it's own container. Currently they are not linked. To do this run:
> $ docker network create OSRNetwork

Then simply re-run our containers specifying the network it now belongs to. First, with the database container
> $ docker run -d --name demodb -p 5432:5432 --network OSRNetwork postgresdb

And then with the Flask container:
> docker run --name sqlrunner -p 5050:5050 --network OSRNetwork webapp

This time, everything should work as per plan.

#### Summary

- In this section, we learnt to develop a Flask application within Docker
- We ran in to our first network configuration issue and solved it by defining a route between the two containers

### A Testing Sandbox

Here we demonstrate how docker can actually be used as a sandbox for testing various changes in a secure and robust manner. To try it out ourselves, we have added some code snippets which will let you extend and create new functionality in our app.

#### Adding a button to list all tables

Add the following line to the code in `templates/base.html`, right after the line with the `<input>` tag, in line 16.

```python
<button type="submit" name="listTables">List Tables</button>
```

Similarly in the file `app/run.py` add the following snippet in line 21.

```python
if not run_text:
    run_text = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'"
```
Now you can simply run the build and run commands again to deploy your flask app with the additional features.

#### Adding a CSV uploader

Simply repeat the steps to add the upload table feature as well Add the following line to the code in `templates/base.html`, right after the line added in previous step, in line 17.

```<button type="submit" name="upload" formaction="/upload" formmethod="GET">Upload Table</button>```

Similarly in the file `app/run.py` add a new method after line 51.

```python
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
    # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        file_table, file_ext = file.filename.split(".")
        if file_ext.lower() in ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            file.save(filename)

            df = pd.read_csv(filename, sep=",")
            print(df)
            engine = create_engine('postgresql+psycopg2://postgres:docker@demodb:5432/postgres')
            df.to_sql(file_table, con=engine, if_exists='fail', index=False)
            return redirect('/')
    return '''
    <!doctype html>
    <title>Upload Table</title>
    <h1>Upload new CSV File</h1>
    <form method="POST" enctype=multipart/form-data>
      <input type=file name="file"><br/><br/>
      <input type=submit value="Upload">
    </form>
    '''
```

#### Testing all new changes

Re-build:
> $ docker build -f dockerfiles/app.Dockerfile -t webapp . --no-cache

Re-run:
> $ docker run --name sqlrunner -p 5050:5050 --network OSRNetwork webapp

#### Summary
- We've now learnt how to leverage Docker as a sandbox environment to test changes


### Plug-and-play

We've mostly seen how to develop for Docker in isolation, so far. In this final section we are  going to demonstrate how Docker enable steam to share and work cross-collaboration with other developers. In this section, we will focus on switching out existing containers with new containers without trying to understand the underlying implementation.

#### Plugging in a new front-end

We've developed a slightly polished version of the SQL Runner app used in our workshop. Here, the code has been shared with you in the form of another docker image. The image Dockerfile has been provided in `app/streamlit.Dockerfile`.

To build:
> $ docker build -f dockerfiles/streamlit.Dockerfile -t streamlit . --no-cache

To run:
> docker run --name graphicosr -p 8501:8501 --network OSRNetwork streamlit

Take some time to check out all the features we've added in the form of our newly dockerized streamlit app.

#### Plugging in a new back-end

We'll repeat this exercise, but this time we want to plug in a new back-end. Assume that this has been deployed with a cloud-based data service such as [fly.io](https://fly.io/) or [CockRoach DB](https://cockroachlabs.cloud/). In our example we went with Cockroach as it is a great **free** data backend hosting service. It reduces cost by using a serverless database, but allowing users to query it using PostgresSQL. Magic!

To see it in action, we will have to re-build with a few changes. We've fetched connection details from our deployed database cluster on Cockroach Cloud. We will commit this string as an environmental variable with the name `COCKROACH_URL`. We've added this to our `.zshrc` file. If you have never done this before, this is an [easy guide](https://phoenixnap.com/kb/zsh-environment-variables) to add permanent environmental variables.

With this variable now defined, we can proceed with using it in our `app/main.py` as our default connection. Find and replace all lines with a `create_engine()` invocation with the following line of code:
```python
engine = create_engine(os.environ["COCKROACH_URL"])
```

The entire line can simply be substituted.

Additionally, there are a few commented lines in our `app/streamlit.Dockerfile`. Simply uncomment lines 26 - 28, this will allow a certificate for connecting to Cockroach Cloud to be generated locally in your target Docker image.

Repeat build and run steps to watch your changes in action.

Build:
> $ docker build -f dockerfiles/streamlit.Dockerfile -t streamlit . --no-cache

_**Note:** For sake of security we are not displaying the full correct connection string here. Never connection details like passwords to your repository. Replace all parameters passed in environmental variable with correct values._

Run:
> $ docker run --name graphicosr -p 8501:8501 -e COCKROACH_URL="cockroachdb://postgres:{password}@{host}/defaultdb?sslmode=verify-full" streamlit

We have also prepared a [notebook](binder/01-cockroach_connector.ipynb) to help setup and store our data in to your Cockroach DB cluster.

#### Summary
That brings us to the end our tutorial section.

- In our final section we demonstrated how to use inter-changeable configurations to truly enable the plug-and-playability of Docker for limitless applications and collaboration.


## Docker in Production

> _For the last part of our workshop we will talk about some production usecases, pros and cons of Docker and some best practices that you can already start to apply._

You can find a summary of the content in our [outro slides](outro_slides.pdf).
