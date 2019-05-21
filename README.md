# Docker Setup

Use this guide if you want to use Docker in your project.

> Built with Docker v18.03.1-ce.

## Getting Started

Update the environment variables in _docker-compose.yml_, and then build the images and spin up the containers:

```sh
$ docker-compose up -d --build
```

Add the following to your docker-compose.yml:

```yml
- API_USERNAME=your_bikereg_username
- API_PASSWORD=your_bikereg_pw
```

## Create the database:

```sh
$ docker-compose run web python manage.py create-db
$ docker-compose run web python manage.py db migrate
# to populate with temp data:
$ docker-compose run web python manage.py create-admin
$ docker-compose run web python manage.py create-data
```

Access the application at the address [http://localhost:5002/](http://localhost:5002/)

### Testing

Test without coverage:

```sh
$ docker-compose run web python manage.py test
```

Test with coverage:

```sh
$ docker-compose run web python manage.py cov
```

Lint:

```sh
$ docker-compose run web flake8 project
```

Deploy to heroku:

```sh
$ heroku container:push --recursive --app=race-support-backend
$ heroku container:release web --app=race-support-backend
```
