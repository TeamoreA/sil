# SIL
[![Build Status](https://travis-ci.com/TeamoreA/sil.svg?branch=master)](https://travis-ci.com/TeamoreA/sil)
[![sill-app Actions Status](https://github.com/TeamoreA/sil/workflows/sil-app/badge.svg)](https://github.com/TeamoreA/sil/actions)
[![Coverage Status](https://coveralls.io/repos/github/TeamoreA/sil/badge.svg?branch=master)](https://coveralls.io/github/TeamoreA/sil?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

- This is a simple python orders service


This application has been documented using Postman Documentation and can be viewed [here.](https://documenter.getpostman.com/view/5990083/TVKFzbe6)

## Setting Up the Application Locally using virtual environment

### Installing PostgreSQL

- PostgreSQL server is required by the application for the application to run. To use the local PostgreSQL server, ensure you have PostgreSQL [installed](https://www.postgresql.org/docs/12/tutorial-install.html) and running. Ensure you add the server PostgreSQL connection URL to your `.env` file

    ``` bash
    DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database name> #  postgres://postgres@127.0.0.1:5432 if no username or password configured, or just a remote host's URL
    ```

### Setting up VirtualEnvironment

- Setup Pyhton virtual environment by running `python3 -m venv venv`

- Activate the virtual environment by running `source venv/bin/activate`

### Installing Application Dependencies

- Run the following command to install application dependencies `pip install -r requirements.txt`

- After installing the dependencies, add the necessary environmental variables required by the application. Sample environment variables are:

    ```bash
    DEBUG=True
    DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database name>
    SECRET_KEY="randomsecretkeyhere" # sample SECRET_KEY
    ```

- Add the above variables in a file name `.env` in the root of the project

### Perform Initial Migrations

- To ensure that the database tables are properly configured, run migrations by running `./manage.py migrate` at the root of the project

### Start the Server

- After successfully performing migrations, the server can be started by running `./manage.py runserver` at the root of the project

### Running Tests

- To run unit test. Run `python manage.py test` at the root of the project

## Setting Up the Application Locally using docker

- Install docker and docker-compose into your local machine

- Build application
  `docker-compose build`

- Run application
  `docker-compose up`

- Open `http://127.0.0.1:8000` to run the application.

### Contributing

- Before contributing, ensure to install `pre-commit` by running  in the root of the application after application setup.
    ``` bash
    $ pre-commit init
    ```
    This is to enforce coding styles.

## Deployments and Releases

- The project had been deployed to Heroku. To view the various versions of the deployed apps, go [here](https://github.com/TeamoreA/sil/deployments)
