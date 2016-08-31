# Project: Item Catalog

This program provides a list of menu items within a variety of restaurants as well as provides a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items and restaurants.

## What's included?
client_secrets.json
database_setup.py
fb_client_secrets.json
project.py
README.md
static
templates

### client_secrets.json
This json file connects the program with a pre-created Google Application.

### fb_client_secrets.json
This json file connects the program with a pre-created Facebook Application.

### database_setup.py
This python file creates the database that will store restaurant, menu, and user data.

### project.py
This python file starts the webserver that runs the program, declares routes, and defines the application's core functions.

### static
This folder contains images and stylesheets to be used when rendering the webpages.

### templates
This folder contains html templates that lay out the structure of the pages to be rendered.

## Configuration:
Install Vagrant and VirtualBox if you have not done so already. Instructions on how to do so can be found at
https://www.udacity.com/wiki/ud197/install-vagrant

### Operating
Clone the fullstack-nanodegree-vm repository. There is an "item_catalog_final" folder which contains the relevant project files.
Launch the Vagrant VM by typing "vagrant up" from the terminal. 
Log in to the Vagrant VM by typing "vagrant ssh" from the terminal.

Navigate to the /vagrant/item_catalog_final directory.

The first time you run the application, you will need to run "database_setup.py" to create a database.

After you have created a database by running "database_setup.py", you can run your application within the VM by typing python project.py into the Terminal.

Access and test your application by visiting http://localhost:5000 locally on your browser.


#### Copyright and licensing information
Some code uses Udacity's Full Stack Web Developer materials.  Otherwise, all the files are belong to me, Adam.

#### Known bugs
[None]

#### Troubleshooting
Good luck!

#### Credits and acknowledgements
Thanks Udacity, Udacity Andy Brown, and Disqus Christian (again)!

##### Changelog
N/A: V1.0, created Aug 31, 2016