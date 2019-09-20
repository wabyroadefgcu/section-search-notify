# section-search-notify
Python script to be run as a cron job to notify user by email when online data changes.

## Configuration:
Copy secret_config_example.txt as secret_config.txt and fill out correct values for the following fields to work with your mail server.

mail_server
mail_server_port
from_addr
password
to_addr

In order to change the data on the page that is being located, it will require a bit of modification to the code. Currently, it's looking for an object in the DOM with id="Table4", then parsing each row to create a list of dictionaries called courseMatrix. At the end of each execution, each element of courseMatrix is checked for available seats and if they are found, an email is triggered.

### TODO:
Make the configuration of the object in the DOM more easily changeable and create a more streamlined way to determine what data to collect.
