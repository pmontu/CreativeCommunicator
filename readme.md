demo on building reat applications

buit drf application to send and recieve messages within an organisation

model created called message that has many to many relationship with users

to run the project locally
`./manage.py migrate`
`./manage.py runserver`

dont forget to create users with email address

open `http://localhost:8000/api/messages/`

use links such as `http://localhost:8000/api/messages/?sender__email=xyz@gmail.com` and `http://localhost:8000/api/messages/?recipients__email=abc@gmail.com`
