# FSND-Proj-5
## Randy's Liquor App
This project uses Flask, PostgreSQL, sqlalchemy, and sqlight to generate a catalog of Liquor categories, with a brief description of each category.  Each category contains a menu of several items of liquor that fit into that category, with a brief description of each item.

Categories with their descriptions may be individually created, edited, or deleted; and within each category menu, items and their descriptions may be created, edited, or deleted.

When first opening the app, the public list of categories and the public list of menus are accessed, and no additions or alterations are possible.  Contents may only be added to or altered by a user who is signed in, and and a given user may only alter that user's own entries.

Login to the app is via secure Google Login registration and authentication.
## Repository Contents
Download or clone the git repository to the host machine, and place the resultant "FSND-Proj-5-master folder in the home directory.  The folder contains these files: Vagrantfile, which specifies the parameters of the virtual machine; pg_config.sh, which retrieves information about the installed version of PostgreSQL for the use of other software packages; client_secrets.json, which contains Google client secret information; catalog.db, which is the actual catalog database; and three python files:  database_setup.py, which sets up the database parameters; install_database.py, which installs a database of liquor categories and items; and base.py, which actually runs the project.  It also contains a folder of HTML templates that perform the various functions of the program, and a static folder, which contains styles.css and several images used by the program.

The virtual machine requires VirtualBox and Vagrant to be installed on the host computer.  
## Prepare to Run the Project
Open a terminal window, such as Mac Terminal or GitBash run in Administrator mode on a Windows machine.
* At the command prompt, navigate to the FSND-Proj-5-master folder.
* Type "vagrant up", or "vagrant provision" if the vm has previously run, then ENTER.  This will start the virtual machine.
* When installation is finished, type "vagrant ssh", then ENTER.  This will log you into the virtual machine.  You will be running ubuntu-trusty-32.
* When logged in, type cd/vagrant[ENTER] at the prompt, to navigate to the files synced between the vm and the master folder on the host machine.  Type ls[ENTER] to list those files.  Type cd/FSND-Proj-5-master[ENTER] to navigate to the catalog files, and ls[ENTER] to display those files.
## Run the Project
* If you wish to start the project from scratch, first remove catalog.db, and run database_setup.py file to set up the database, with the appropriate rows and columns.Then run install_database.py to load a catalog from scratch.  You will not be able to edit or delete any of the entries, because you did not create them.  Otherwise, run the project with the catalog.db found in the repo.  
* Run base.py to start the catalog program, which may be found at localhost:8080 on a browser.  You will be at the home page, which will display the contents of the catalog.
* Click on "Click Here to Login" to get to the Login page, where you may login with Google.

Once you are logged in, you will be on the homepage of Randy's Liquor App, on which you will find a list of liquor categories, along with a description of each category.  You may add a category and description by clicking on the "Add Category" button, which will take you to the newCategory.html page where you may type in your category and description.  Any category that you create may be edited or deleted by you by clicking on the appropriate link, taking you to the editcategory.html or deletecategory.html page.

Clicking on the category name, eg Bourbon, takes you to the Bourbon menu page, which contains a list of bourbons and their descriptions.  You may add, edit, or delete an item as on the category page.  To get back to the front page, click on the "Show All Categories" button.