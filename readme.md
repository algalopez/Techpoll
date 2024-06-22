
# TECH POLL

**Silly poll**

Give your opinion and learn that that it is all wrong xD

## Requirements

- VSCode with the remote containers plugin
- Docker

## Run

Start the dev container  
Perform the database migration  
Execute the app  
Open http://localhost:17301/rest/hello/ to verify that it works
... TBC

### Database migration


### App execution


## Test


## Other


docker build -f .devcontainer\Dockerfile . -t asd  
docker run asd  

docker-compose -f .\.devcontainer\docker-compose.yml up --build  

docker exec -ti devcontainer-app-1 /bin/bash  


flyway -configFiles=database/conf/flyway.properties clean migrate
flyway -configFiles=database/conf/flyway-techpoll.properties clean migrate

