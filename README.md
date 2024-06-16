[![Actions Status](https://github.com/Aston585/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Aston585/python-project-52/actions)
[![Linting, testing and deployment](https://github.com/Aston585/python-project-52/actions/workflows/task-manager.yml/badge.svg)](https://github.com/Aston585/python-project-52/actions/workflows/task-manager.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/98603672c19d352c643a/maintainability)](https://codeclimate.com/github/Aston585/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/98603672c19d352c643a/test_coverage)](https://codeclimate.com/github/Aston585/python-project-52/test_coverage)

# Task Manager

It's a classic task manager project with opportunity to set marks and set performer for each task.

## STATUS

You can view it on [link](https://python-project-52-relc.onrender.com)

## INSTALLATION
### Local option
Need to  [poetry](https://python-poetry.org/docs/#installation) is to be installed 


 
    git clone https://github.com/Aston585/python-project-52
    cd python-project-52
    make install
    make migrate
    make start

enjoy app on http://localhost:8000

### Settings
Environment variables
- database
- django-secret 
- rollbar token

can be set in environment or by rename file .env_example and set values in it.

    /.env_example -> /.env
