# How to use
Prepare venv under work directory
```bash
python3 -m venv venv
```

Activate the interpretor in project
```bash 
source venv/bin/activate
```

Install dependencies from pypi
```bash 
pip install -r requirements.txt
```

Initialize a docker volume
```
docker volume create mongo-db-vol
```

Start mongo db docker container
```bash
docker run -d -p 30001:27017 -v mongo-db-vol:/data/db --name=ztgg-mongo mongo
```


Run a minimal flask app
```
flask --app entrypoint run
```

# Styleguide
Refer to https://google.github.io/styleguide/pyguide.html

# Rest API Reference
## User API
### Get user by name

Successful Use Case:
```
GET /backend-api/v1/user/:name

Status: 200
{
    "age": 11,
    "emails": [],
    "name": "alexa",
    "createdBy": "App_Admin",
    "id": 1,
    "_id": "some-id",
    "updatedBy": "App_Admin",
    "createdInMS": 1670531166662,
    "updatedInMS": 1670531166662
}
```

### Create a new user

Successful Use Case:
```
POST /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "name": "daniel",
    "age": 11
}

Status: 201
{
    "rep_code": 201,
    "msg": "successfully created user"
}
```

Failed Use Case: User already exists
```
POST /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "name": "alexa",
    "age": 11
}

Status: 400
{
    "rep_code": 400,
    "msg": "User name ['alexa'] is not unique"
}
```

Failed Use Case: Bad Request
```
POST /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "name": "daniel",
}

Status: 405
{
    "rep_code": 405,
    "msg": "Please provide ['name', 'age'] fields in payload"
}
```

### Delete an exisiting user

Successful Use Case:
```
DELETE /backend-api/v1/user/:id

Status: 200
{
    "rep_code": 200,
    "msg": "Sucessfully deleted user"
}
```

Failed Use Case: User doesn't exist
```
DELETE /backend-api/v1/user/:id

Status: 409
{
    "rep_code": 409,
    "msg": "There is no user with [id] on file"
}
```

### Apply modifications to a resource.

Successful Use Case:
```
PATCH /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "id": 1,
    "age": 10
}

Status: 200
{
    "rep_code": 200,
    "msg": "Sucessfully updated user"
}
```

Failed Use Case: Bad Request
```
PATCH /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "age": 10
}

Status: 205
{
    "rep_code": 205,
    "msg": "Please provide ['id'] fields in payload"
}
```

Failed Use Case: Bad Request
```
PATCH /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "id": 3
}

Status: 205
{
    "rep_code": 205,
    "msg": "Please provide at least one of ['name', 'age'] fields in payload"
}
```

Failed Use Case: Bad Request
```
PATCH /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "id": 3,
    "name": "alexa"
}

Status: 205
{
    "rep_code": 205,
    "msg": "User name ['alexa'] is not unique on file"
}
```

Failed Use Case: User doesn't Exist
```
PATCH /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "id": 10000,
    "age": 10
}

Status: 409
{
    "rep_code": 409,
    "msg": "There is no user with [id] on file"
}
```

## Users API
### Get users list
Successful Use Case:
```
GET /backend-api/v1/users

Status: 200
[
    ...,
    {
        "age": 11,
        "emails": [],
        "name": "alexa",
        "createdBy": "App_Admin",
        "id": 1,
        "_id": "some-id",
        "updatedBy": "App_Admin",
        "createdInMS": 1670531166662,
        "updatedInMS": 1670531166662
    }
]
```