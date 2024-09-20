# <a name="x8e2e5997b53ac793e8d48c9fca6281a291feb67"></a>**Breaking Down Monoliths: Converting a Monolithic Docker-Compose Application to Microservices**
The problem statement:
- Convert a monolith architecture based docker-compose application into a microservices based architecture.
## <a name="requirements"></a>**Requirements:**
- [docker](https://docs.docker.com/engine/) and [docker-compose](https://docs.docker.com/compose/install/).
- Internet. 
## <a name="initial-directory-structure"></a>**Initial directory structure**
├── README.md  
├── docs  
│   └── <documentation related images/files>  
├── microservices  
│   ├── Docker-compose.yaml  
│   ├── landing  
│   │   ├── app  
│   │   │   ├── app.py  
│   │   │   ├── requirements.txt  
│   │   │   └── templates  
│   │   │       └── index.html  
│   │   └── Dockerfile  
│   │  
## <a name="monolith-architecture-diagram"></a>**Monolith architecture diagram**
![monolith-architecture-diagram](https://github.com/Vijayrajgs/Breaking-down-monoliths/blob/main/Monolithic_Architecture.png)
## <a name="build--run"></a>**Build & Run**
\# under the microservices directory
\# NOTE: For any code changes to be reflected, the build command must be rerun, and then up
docker-compose build
\# run without the -d flag incase you want to observe the logs
docker-compose up -d
### <a name="to-stop-the-services-in-detached-mode"></a>**To stop the services in detached mode**
docker-compose down

**NOTE**: It is possible your first build will not be successful and that's alright. Read the stack trace and debug the errors. The resources and links provided within the manual are sufficient to successfully complete the project.

## <a name="microservices-based-architecture-diagram"></a>**Microservices-based architecture diagram**
![microservices-based-architecture-diagram](https://github.com/Vijayrajgs/Breaking-down-monoliths/blob/main/Microservice_architecture.png)

The diagram only shows the services already defined within the microservice architecture for visualization purposes. You still need to add services of your own.
## <a name="miscellaneous"></a>**Miscellaneous**
- Directory structure of additional arithmetic microservices should be as:

├── <name of the service>
│   ├── Dockerfile           # same as landing/Dockerfile  
│   ├── app  
│   │   ├── app.py  
│   │   └── requirements.txt # same as landing/app/requirements.txt  
│   │    
