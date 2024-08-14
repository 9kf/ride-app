This project uses postgres as the database. You dont need to install the postgres
db on your local machine since its defined on the docker-compose.yml file

STEPS to run the project

1. install docker desktop
2. clone the project and open a terminal on the project root folder
3. run command "docker-compose up -d --build"
4. after the containers are running, run commands:
   - docker-compose exec -it app bash
   - python manage.py migrate
   - python manage.py createsuperuser
5. login with your superuser in localhost:8000/admin
6. access the endpoints

If you want to debug the project on vscode run "docker-compose -f docker-compose.dev.yml up -d" and create a launch.json in the .vscode folder at the root of the project with these json:

```
{
  "configurations": [
    {
      "name": "ride-app-debugger",
      "type": "debugpy",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 5678
      },
      "pathMappings": [
        {
          "localRoot": "${workspaceFolder}",
          "remoteRoot": "."
        }
      ],
      "justMyCode": true
    }
  ]
}
```
