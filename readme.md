
# TECH POLL

**Silly poll**

Give your opinion and learn that it is all wrong xD

## Requirements

- VSCode with the remote containers plugin
- Docker
- Ngrok (optional)

## Run

1. Start the dev container  
2. Perform the database migration  
3. Execute the app  
4. Open http://localhost:17301/rest/hello/ to verify that it works  
5. Open index.html
6. Share the poll

### Start dev container

Open the projects folder with VSCode and click build container in the remote containers plugin

### Database migration

flyway -configFiles=database/conf/flyway.properties clean migrate  
flyway -configFiles=database/conf/flyway-techpoll.properties clean migrate  

### App execution

python3 app.py

### Open Web

Open the index.html and add your ip to the url: index.html?server=192.168.1.1

### Share the poll

Open ngrok and get a public ip

Share the index.html file and tell people to add the ip: index.html?server=https://uuid.ngrok-free.app

## Test

shhh, close your eyes

## Sonarqube

sonar-scanner -Dsonar.login=<token>

## Sample

![TechPoll](/documentation/Techpoll_result.png)

## Other

<details>
  <summary>Open</summary>
```bash

docker build -f .devcontainer\Dockerfile . -t asd

docker run asd

docker-compose -f .\.devcontainer\docker-compose.yml up --build

docker exec -ti devcontainer-app-1 /bin/bash

```
</details>