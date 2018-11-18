### Property listing API example.
---
#### Technology stack:
- Django.
- Django Rest Framework.
- JWT.
- Python.
- PostgreSQL.
- Docker/Docker-Compose.
---

#### Setup:
##### Prerequisites:
- [Docker](https://docs.docker.com/install/).
- [Docker-compose](https://docs.docker.com/compose/install/).
- [Git](https://git-scm.com/).
##### Install and run:

On your terminal, run the following commands:

```bash
> git clone git@github.com:msmsh83/propertylisting.git
> cd propertylisting
> docker-compose build
> docker-compose up
```

And then nvagiate your browser to [see the API docs](http://localhost:8000/docs/)


##### Run the django migration files to setup the database:
In your root directory:
```bash
> docker-compose run web /usr/src/api/manage.py migrate
```

##### Create a user so you can authenticate with the API:
In your root directory:
```bash
> docker-compose run web /usr/src/api/manage.py createsuperusers
```

##### Run the import script:
In your root directory:
```bash
> docker-compose run web /usr/src/api/manage.py import --path='challenge_data.csv'
```
> Note: this assumes that the input file is where it is now in the repo, you can change that to any other valid disk location.

##### Authentication:
- Use the credentials you have created in the previous step to retrieve a JWT token using the [login API](http://localhost:8000/docs/#login-create)
- Set the token in the authentication section of the API interface under the token part, use `JWT` for the scheme.

##### Interact with the APIs:
- [The list](http://localhost:8000/docs/#api-v1-properties-props-list)
- [The post/create](http://localhost:8000/docs/#api-v1-properties-props-create)
