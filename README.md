
# Python - Getting Started with Flask

pip install Flask
open "helloworld.py"
import Flask
instantiate a new instance of Flask 
use your new instance of flask and add an index route ('/')
below your route, define a method that returns a string
explain that when the browser sends an HTTP request to our application for the (/) route, it will run the function and send a response back with whatever the function is returning


## Introduction
In this lab we are going to practice making a very simple web application. To do this, we will be using a framework called Flask, which allows us to create an application that communicates with our browser. We will define a route, and have it return a string "Hello world". Finally, we will start a local server and visit the route in our browser, which will make a request to our program, which should then return our "Hello world" string. Don't worry if that sounds a bit confusing. It will become a lot clearer shortly. Let's get started!

## Objectives
* One
* Two

### Guest
**Class Methods:**
* `Guest.all()` returns a list of all guest instances
* `Guest.most_popular()` returns the guest invited to the most dinner parties
* `Guest.toughest_critic()` returns the guest with lowest average rating for recipe reviews
* `Guest.most_active_critic()` returns the guest with most amount of recipe reviews

**Instance Methods:**
* `guest.rsvp(invite, rsvp_status)` takes in a boolean value (True or False) and updates a guest's rsvp status. It should return the rsvp_status status
* `guest.number_of_invites()` returns the number of dinner party invites a guest has recieved 
* `guest.review_recipe(recipe, rating, comment)` adds a guest's review with a rating and comment to a recipe. Returns the given recipe's reviews
* `guest.favorite_recipe()` returns the given guest's favorite recipe

### Invite
**Class Methods:**
* `Invite.all()` returns a list of all invite instances

**Instance Methods:**
* `invite.accepted` returns a boolean value (true or false) for whether the the guest accepted the invite or not
* `invite.guest` returns the given invite's guest instance
* `invite.dinner_party` returns the given invite's dinner party instance

### DinnerParty
**Class Methods:**
* `DinnerParty.all()` returns a list of all dinner party instances

**Instance Methods:**
* `dinner_party.reviews()` returns a list of reviews for the recipes of a given dinner party
* `dinner_party.recipes()` returns a list of recipes for the given dinner party
* `dinner_party.recipe_count()` returns the number of recipes for the given dinner party
* `dinner_party.highest_rated_recipe()` returns the highest rated recipe for the given dinner party
* `dinner_party.number_of_attendees()` returns the number of guests who accepted their invite for the dinner party

### Course
**Class Methods:**
* `Course.all()` returns a list of all course instances

**Instance Methods:**
* `course.dinner_party` returns the dinner party instance for the given course
* `course.recipe` returns the recpipe instance for the given course

### Review
**Class Methods:**
* `Review.all()` returns a list of all invite instances

**Instance Methods:**
* `review.rating` returns the given review's rating
* `review.recipe` returns the given review's recipe
* `review.reviewer` returns the given review's reviewer (guest instance)
* `review.comment` returns the given review's comment, if there is one

### Recipe
**Class Methods:**
* `Recipe.all()` returns a list of all invite instances
* `Recipe.top_three()` returns a list with the three recipe instances with the highest average rating
* `Recipe.bottom_three()` returns a list with the three recipe instances with the lowest average rating

**Instance Methods:**
* `recipe.reviews()` returns a list of reviews for the given recipe
* `recipe.top_five_reviews()` returns a list with the five review instances with the highest rating for the given recipe

## Summary


Great work! In this lab we created a pretty complex domain model and defined some neat class and instance methods to leverage these has many through relationships. We could see that without these relationships, meaning without a review linking a recipe and a guest, it would become very difficult to organize our information and query it accurately like we do in a class method that gives us the top or bottom three recipes. 
