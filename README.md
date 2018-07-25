**TravisCI status**
[![Build Status](https://travis-ci.org/kimbugp/MyDiary.svg?branch=develop)](https://travis-ci.org/kimbugp/MyDiary)
**Test Coverage Reporting**
[![Coverage Status](https://coveralls.io/repos/github/kimbugp/MyDiary/badge.svg?branch=master)](https://coveralls.io/github/kimbugp/MyDiary?branch=master)
**Code Climate**
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

```git clone https://github.com/kimbugp/Mydiary```
#### Install virtual environment 
``` C:\Users\User>virtualenv venv```
#### Activate virtual environment
``` C:\Users\User>venv\Scripts\activate``` 

```(venv) C:\Users\User> ```
#### Install flask in the virtual environment 
```(venv) C:\Users\User>pip install flask```

### Move to the directory with the app 
```cd /MyDiary/app/v1```
### Run the server with the command
```python -m flask run ```

### Running Tests

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
  | GET            | fetching all entries    |      api/v1/entries
  | POST            |Creating an entry        |      api/v1/entries
 | GET             |Fething a specific entry   |    api/v1/entries/<<int:entryid>>
 | PUT             |Updating a specific entry     | api/v1/entries/<<int:entryid>>

## Authors
* Kimbugwe Simon Peter 
## Contributors
* Patrick Walukagga
* Arnold Arinda
* Andela
* Mendoza Bridget
