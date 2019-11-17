# python-rest-api
Firefly backend case study

Since token control does not exist in unit tests, the following changes should be made when trying login / register endpoints.

The app/settings.py file should be modified as follows.

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

#TEST CONFIG
#REST_FRAMEWORK = {
#    'DEFAULT_PERMISSION_CLASSES': [],
#    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
#}

Postman Collection Link : https://www.getpostman.com/collections/ce537cae53214a1bf59c