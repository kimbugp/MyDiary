[![Build Status](https://travis-ci.org/kimbugp/MyDiary.svg?branch=challenge-3)](https://travis-ci.org/kimbugp/MyDiary)
[![Coverage Status](https://coveralls.io/repos/github/kimbugp/MyDiary/badge.svg?branch=challenge-3)](https://coveralls.io/github/kimbugp/MyDiary?branch=challenge-3)
[![Maintainability](https://api.codeclimate.com/v1/badges/4b137dbde922e2570098/maintainability)](https://codeclimate.com/github/kimbugp/MyDiary/maintainability)
# My Diary 
MyDiary is an online journal where users can pen down their thoughts and feelings.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
### Prerequisites
You need to install the following: 
* Server side Framework: ​[Flask Python Framework](http://flask.pocoo.org/)
* Testing Framework: [PyTest](https://docs.pytest.org/en/latest/)

### Installing 
These are the series of commands you need to get it up and running on your machine 
#### Clone the repo into your local machine

```
git clone https://github.com/kimbugp/Mydiary
```
#### Install virtual environment 
``` 
C:\Users\User>virtualenv venv
```
#### Activate virtual environment
``` 
C:\Users\User>venv\Scripts\activate
``` 

```
(venv) C:\Users\User>
 ```

### Move to the directory of the cloned repository folder
  ```
   (venv)cd /MyDiary
  ```
#### Install modules required for the app 
```
(venv) $ pip install>requirements.txt
```
#### Create database by running the following command
```
psql -c 'create database diarydb;' -U postgres
```
### Run the server with the command
```
python -m flask run 
```

### Running Tests
* Install nosetests and coverage
  ```
  $ pip install nose coverage
  ```

* Running the tests
  ```
  $ nosetests -v --with-coverage --cover-package=api
  ```
## Features
* Users can create an account and log in.
* Users can view all entries to their diary.
* Users can view the contents of a diary entry.
* Users can add or modify an entry.

## License
This project is licensed under the MIT License


## Access at:
### https://kimbugp.github.io/MyDiary/UI/
### https://simondiary.herokuapp.com

 ## MY DIARY'S ENDPOINTS
	
   | METHOD     |        ACTIVITY   |                  ENDPOINT|
   | :---         |     :---:      |          ---: |
   | POST         |  register a user | /api/v1/auth/signup 
   | POST         |  login a user | /api/v1/auth/login
  | GET            | fetching all entries for a user   |      api/v1/entries
  | POST            |Creating an entry for a user      |      api/v1/entries
 | GET             |Fetching a specific entry for a user |    api/v1/entries/<<int:entryid>>
 | PUT             |Updating a specific entry     | api/v1/entries/<<int:entryid>>

## Authors
* Kimbugwe Simon Peter 
## Contributors
* Patrick Walukagga
* Arnold Arinda
* Andela
* Mendoza Bridget
