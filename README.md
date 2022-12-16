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
[   ...,
    {
        "age": 11,
        "emails": [],
        "name": "daniel",
        "createdBy": "App_Admin",
        "id": 1,
        "_id": "some-id",
        "updatedBy": "App_Admin",
        "createdInMS": 1670531166662,
        "updatedInMS": 1670531166662
    }
]
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
    "msg": "The user[{'name': 'daniel', 'age': 11, 'createdInMS': 1670531166662, 'updatedInMS': 1670531166662, 'id': 1, 'createdBy': 'App_Admin', 'updatedBy': 'App_Admin', '_id': ObjectId('some-id')}] is created successfully"
}
```

Failed Use Case: User already exists
```
POST /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "name": "daniel",
    "age": 11
}

Status: 409
{
    "rep_code": 409,
    "msg": "The user[{'name': 'daniel', 'age': 11}] is duplicated"
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
    "msg": "The user has been deleted successfully"
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

### Apply partial modifications to a resource.

Successful Use Case:
```
PATCH /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "id": 1,
    "age": 10,
    "name": 'daniel'
}

Status: 200
{
    "rep_code": 200,
    "msg": "The user[{'name': 'daniel', 'age': 11, 'createdInMS': 1670531166662, 'updatedInMS': 1670531166662, 'id': 1, 'createdBy': 'App_Admin', 'updatedBy': 'App_Admin', '_id': ObjectId('some-id')}] is modified to [{'name': 'daniel', 'age': 10, 'createdInMS': 1670531166662, 'updatedInMS': 1670531839417, 'id': 1, 'createdBy': 'App_Admin', 'updatedBy': 'App_Admin', '_id': ObjectId('some-id')}]"
}
```

Failed Use Case: Bad Request
```
PATCH /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "id": 1,
    "age": 10
}

Status: 205
{
    "rep_code": 205,
    "msg": "Please provide ['id', 'name', 'age'] fields to be modified in payload"
}
```

Failed Use Case: User doesn't Exist
```
PATCH /backend-api/v1/user
Payload: Content-Type=application/json 
{
    "id": 1,
    "age": 10,
    "name": "daniel"
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
        "name": "daniel",
        "createdBy": "App_Admin",
        "id": 1,
        "_id": "some-id",
        "updatedBy": "App_Admin",
        "createdInMS": 1670531166662,
        "updatedInMS": 1670531166662
    }
]
```