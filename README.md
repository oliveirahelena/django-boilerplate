# Django Boilerplate

[![alt text](/thumbnail.png "Logo")](https://casaldev.com.br)

This project is configured for:

1. Python version management with pyenv
2. Virtual environments with pipenv
3. Usage of environment variables
4. AWS S3 for static files
5. Webpack loader

## Getting started

1. Pipenv (virtualenv)
   ```
   pipenv install
   ```
   ```
   pipenv shell
   ```
   ```
   pipenv run python manage.py rename demo your-project-name
   ```
2. Update .vscode/settings.json with the virtual enviroment name created
3. You will need to copy the `.settings.env` file and rename it `.env`. Inside there you can fill in the values of the environment variables, create a database and you're all good to go.
4. Run server
   ```
   pipenv run python manage.py runserver
   ```