# Item Catalog Web App
This web application is a third project for the Udacity [Full Stack NanaDegree Course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## About
This project is a RESTful web application utilizing the Flask framework which accesses a SQL database that populates categories and their items. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

## In This Repo
This project has one main Python module `app.py` which runs the Flask application. A SQL database is created using the `database_setup.py` module and you can populate the database with test data using `database_init.py`.
The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application. CSS/JS/Images are stored in the static directory.

## Skills Honed
1. Python
2. HTML
3. CSS
4. OAuth
5. Flask Framework

## Installation
There are some dependancies and a few instructions on how to run the application.
Seperate instructions are provided to get GConnect working also.

## Dependencies
- [Python3](https://www.python.org/download/releases/3.0/) - The code uses version 3.6.8. 

- [Vagrant](https://www.vagrantup.com/) - The software that configures the VM and lets you share files between your host computer and the VM's filesystem. 

- [VirtualBox](https://www.virtualbox.org/) - The software that actually runs the virtual machine. 

- [Git](https://git-scm.com/) - An open source version control system. 

- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm) - The VM configuration which can preconfigure vagrant settings. 


## How to Install
1. Install VirtualBox:  I used the Ubuntu 18.04, install VirtualBox using the Ubuntu Software Center directly. 
2. Install Vagrant:  Run `sudo apt install vagrant`at the terminal to install and verify vagrant installation by `vagrant --version`. 
2. Clone the Udacity Vagrantfile.
3. Go to Vagrant directory and either clone this repo or download and place zip here and name it as `item-catalog`.
3. Launch the Vagrant VM (`vagrant up`). 
4. Log into Vagrant VM (`vagrant ssh`). 
5. Navigate to `cd vagrant` as instructed in terminal. 
6. The app imports requests which is not on this vm. Run `sudo pip install requests`.
7. Navigate to `cd item-catalog` as instructed in terminal
7. Setup application database `python database_setup.py`. 
8. Insert fake data `python database_init.py`.
9. Run application using `python app.py`. 
10. Access the application locally using http://localhost:5000

## Using Google Login
To get the Google login working there are a few additional steps:

1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials -> OAuth concent screen and fill application name -> the OAuth Client ID
5. Select Web application 
6. Enter name 'Item-Catalog'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory that you cloned from here
14. Run application using `python /item-catalog/app.py`

## JSON Endpoints
The following are open to the public:

Catalog JSON: `/catalog/JSON`
    - Displays the whole catalog. Categories and all items.

Categories JSON: `/catalog/categories/JSON`
    - Displays all categories

Category Items JSON: `/catalog/<path:category_name>/items/JSON`
    - Displays items for a specific category

Category Item JSON: `/catalog/<path:category_name>/<path:item_name>/JSON`
    - Displays a specific category item.
