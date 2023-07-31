"""
File with FastApi documenting variables.
"""

# FastAPI description for documenting purposes
description = """
Phone book API.

## Contacts

You can:

* **Get every contact in database**
* **Get contact with its id number**
* **Search for a contact with its name**
* **Search for a contact with its last name**
* **Search for a contact with its name and last name**
* **Search for a contact with its email**
* **Search for a contact with its phone number**
* **Create a new contact** (_needs user authentication_)
* **Update an existing contact** (_needs user authentication_)
* **Delete an existing contact** (_needs user authentication_)

## Users

You can:

* **Create a new user for authentication purposes**
* **Get a JWT token** (_for creating, updating and deleting a contact_)
"""

tags_metadata = [
    {
        "name": "contacts",
        "description": "Operations with contacts."
    },
    {
        "name": "user",
        "description": "Create user and login to obtain access token."
    }
]
