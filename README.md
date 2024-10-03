# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

Note you will need to install Python for this.

```bash
curl -sSL https://install.python-poetry.org | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You will likely then need to add poetry to your PATH, for me it was found at 

`C:\Users\user-name\AppData\Roaming\pypoetry\venv\Scripts`

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.


## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing

To run tests run `poetry run pytest` 

To run a single test file run `poetry run pytest <path_to_test_file>`

To run a single test run `poetry run pytest -k <test_name>`

## Linting

Run `poetry run black .` before a commit to lint the code.

## Run via VM

Run the playbook to install and run the app on a VM using:

`ansible-playbook playbook.yml -i hosts.ini`

The host names of VMs to do this on are specified in `hosts.ini`

This must be run from a control node with ansible installed.

SSH into your chosen control node with `ssh USERNAME@IP-ADDRESS` and copy over the following files 

- `playbook.yml`
- `hosts.ini`
- `todoapp.service`
- `.env.j2`

## Run via Docker

The app can be run in a production or development Docker container.

### Production
To run the app in a production container, build the image with the following command:
    `docker build --target production --tag todo-app:prod .` 

Then run the image with:
    `docker run --env-file .env --publish 5000:5000 todo-app:prod`

### Development
To run the app in a development container, build the image with the following command:  
    `docker build --target development --tag todo-app:dev .` 

Then run the image with:
    `docker run --env-file .env --publish 5000:5000 --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev`

### Test
To build the image run
    `docker build --target test --tag todo-app:test .` 

Then run the image
    `docker run --env-file .env todo-app:test`

## Architecture Diagrams

There are various architecture diagrams, these can be edited at the following links:

- [Context](https://drive.google.com/file/d/18BS3nEtXpjtA20sy34RnllzXHkki3s41/view?usp=sharing)
- [Container](https://drive.google.com/file/d/1jSqLHqSkewq0LrWeUCb7xt6wbRtAS6l1/view?usp=sharing)
- [Component](https://drive.google.com/file/d/10fiX0yS5X_fz9KX-pwp16SeswVr5LYOU/view?usp=sharing)

## Azure Hosting

The container image that is deployed to Azure is hosted on Docker Hub at [emmabragg/todo-app](https://hub.docker.com/repository/docker/emmabragg/todo-app)

The website itself is hosted at https://emmbratodowebapp.azurewebsites.net/

To update the website you will need to run the following commands to build and push the updated container image:
```bash
    docker build --target production --tag emmabragg/todo-app .
    docker push emmabragg/todo-app
```

To trigger an update we need Azure to pull the new image from Docker Hub.

To do this make a POST request to the webhook.

Its value can be found on the App Service (under the Deployment Centre tab).
