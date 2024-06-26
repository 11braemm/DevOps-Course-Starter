# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

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

## Trello API setup 
- Create a Trello account
- Create an API Key for Trello
    - To do this you’ll first need to create a Trello Power Up [(from this page)](https://trello.com/power-ups/admin)
    - After creating a Trello Power Up you’ll be given the option to generate a new API key
- Create a API Token for Trello.
    - This can be done by clicking the “Token” link on the same page where your API key is displayed:
    ![alt text](image.png)

Once generated please fill these in as your 
- TRELLO_API_KEY
- TRELLO_API_TOKEN

You will then need to retrieve the ID of your chosen board and the corresponding done and not done lists to substitute into:
- TRELLO_BOARD_ID
- NOT_STARTED_LIST_ID
- DONE_LIST_ID

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

