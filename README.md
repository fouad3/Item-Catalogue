# Project : Item-Catalogue
## By  Fouad Asharf


## Table of contents
- [Description](#description)
- [Required Libraries and Dependencies](#required-libraries-and-dependencies)
- [How to Run Project](#how-to-run-project)
- [Copyright and license](#copyright-and-license)
 
## Description
An application that provides a list of items within a variety of categories as well as provides a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items,this project is a part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Required Libraries and Dependencies
 1. Install Vagrant, you can download it from https://www.vagrantup.com/.
 2. Install  VirtualBox, you can download it from https://www.virtualbox.org/.
 3. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm.git) repository.
 
## How to Run Project
1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
3. Put application locally in the vagrant/catalog directory (which will automatically be synced to /vagrant/catalog within   the VM).

4. Then Run python database_fill.py to fill some data in the database

5. Then Run python project.py to run the server

6. open the app by visiting http://localhost:5000/

## Copyright and License

- supplied without rights information contributed by [Udacity](http://www.udacity.com).
