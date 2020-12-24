# Creating a service with RESTful API endpoints
Date - 03-Sep-2020

## HTTP verbs/methods to implement a REST (Representational State Transfer) complying service
* GET - querying stuff - example: get list of users
* POST - for giving commands/creating something - example: create a person
* PUT - for modify/edit command - example: change the name of the user
* DELETE - for delete command - example: delete a user

## Exposing functionality of a service via a URL / API endpoint
* Each functionality of the server can be exposed as a URL. This is called an API endpoint

#### Passing input parameters to a URL endpoint
The following techniques can be used to pass data to an API endpoint
* URL segments - example: abc.com/sum/1/3
* Query parameters - example: abc.com/sum?x=1&y=3
* Request Body
Example: POST abc.com/sum. In request body the following will be present
```javascript
{
"x": 1,
"y": 3
}
```
## Response status codes
In order to convey the type of respose to the client, the service and sent HTTP status codes along with the response body
Some important and most used HTTP response status codes are 
* 200 OK
* 201 Created
* 204 No Content
* 301 Moved Permanently
* 400 Bad Request
* 401 Unauthorized
* 404 Not Found
* 403 Forbidden
* 409 Conflict
* 500 Internal Server Error

https://www.restapitutorial.com/httpstatuscodes.html

https://developer.mozilla.org/en-US/docs/Web/HTTP/Status