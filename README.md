# Nommy

## Project Overview

Nommy is a meal planning app that is designed to help users decide on what to cook! A lot of people would agree that deciding on what to cook on a given night can take up time and effort but Nommy is here to help you make your decision.

The app is essentially a database of recipes that also allows users to add their own recipes to those already on the site. Additional functionality is also here allowing users to create profiles, share and bookmark recipes, basically giving them a virtual cookbook!

## User Experience (UX)

### User Stories

#### Epic - User Navigation
- As a first time user of the site, I want to immediately understand the content of the site and decide if it suits my needs.
- As a site user, I want the app layout in a way that allows me to navigate intuitively, through well designed navigation bars and page content.
- As a site user, I want to view a paginated list of recipes, so I can decide on which one to view.
- As a site user, I want to be able to click on a recipe to view the ingredients, cook time and method of cooking.
- As a site user, I want to be able to view the number of likes on each recipe so that I can see which is the most popular.
- As a site user, I want to be able to view and share receipes with my friends.

#### Epic - User Profile
- As a site user, I want to be able to create my own account so I can create my own recipes, save existing recipes as favourites and comment/like other users recipes.
- As a registered site user, I want to be able to log in and log out of my account safely and securely.
- As a site user, I want to be able to view my statistics such as how many recipes I've added, how many I have in my favourites and how many recipes I've commented on.

#### Epic - Recipe Interaction
- As a registered user, I want to be able to add recipes to my favourites list so I can find them easily in future.
- As a registered user, I want to be able to create my own recipes to add to the app.
- As a registered user, I want to be able to edit recipes I have created, for example to add tips, or make other changes.
- As a registered user, I want to be able to view my favourite recipes in one location.
- As a registered user, I want to be able to view the recipes I have created in one location.
- As a registered user, I want to be able to comment on other recipes and leave feedback.
- As a registered user, I want to be able to like other recipes to help bring them to the attention of other users. 


### Design

#### Colour Scheme

#### Imagery

#### Typography




#### Wireframes



1. Please see desktop wireframes [here](documentation/wireframes/desktop.png).
2. Please see tablet wireframes [here](documentation/wireframes/tablet.png).
3. Please see mobile wireframes [here](documentation/wireframes/mobile.png).


## Features

## Agile Methodology

The agile methodology was used in developing this project through Github projects. 

The 3 user story epics above were broken down into Milestones on the Github project and each user story in the given Milestone was further broken down into individual issues to facilitate completion of each user story.

Please view the Github projects board [here](https://github.com/users/StephenB92/projects/4).

## Data Models

Custom models are used throughout the project.

To facilitate users creating their own recipes, a custom recipe model is required.

To facilitate users commenting on recipes, a custom comment model is required.

To facilitate users creating their own profiles, a custom user profile model is required.

You can view the details of the database schema [here](documentation/database-schema/database-schema.png).

## Deployment

## Technologies Used

### Coding Languages Used
1. HTML5
2. CSS3
3. Python

### Frameworks, Libraries and Online Tools
1. Django
2. Bootstrap
3. Github - used for agile method of planning and for version control of the project
4. Heroku - used for site deployment
3. Lucidchart - used to map the database schema
4. Balsamiq - used to create wireframes




## Testing

## Bugs and Fixes

- While coding the comment functionality, I kept receiving an error where a user can only post one comment across the entire site. 
- While creating the CRUD functionality of the site and then bug testing, I saw while playing around with the urls that any user of the site (registered or not) could edit and delete recipes by typing /updaterecipe or /deleterecipe in the url adter the currently viewed recipe. To solve this, I used the LogInRequiredMixin from the Django Authentication system, which redirects unregistered users to the login page (credit below). For other registered users, I used if else statements using Django logic in my update recipe and delete recipe pages. These statements checked if the logged in user matches the "creator" of the recipe. If these don't match, the form will not appear to the user and they are redirected to their "my recipes" page. Credit below.
- While testing the project, I realised that user uploaded images from the site were not being saved to Cloudinary. After researching om W3S, I found that the "enctype" attribute with the value of "multipart/form-data" was required here. Credit below.


## Credits/Acknowledgements 

- The Code Institute Walkthrough Project: "I think therefore I blog".
- Pexels for the stock images used in this project.
- Credit to [this](https://stackoverflow.com/questions/837828/how-do-i-create-a-slug-in-django) post on Stack Overflow which solved an issue with new recipes not generating new slugs.
- Credit to [this](https://stackoverflow.com/questions/57710135/how-to-print-the-string-value-of-a-choices-field) post on Stack Overflow where I found code to display the status of users recipes as strings on the "My Recipes" page.
- Credit to [this](https://www.youtube.com/watch?v=aStLddXMJrk&list=WL&index=3&ab_channel=CodingEntrepreneurs) video on Youtube by CodingEntrepreneurs which helped with code for pre-populating the user form in the update view.
- Credit to [this](https://stackoverflow.com/questions/47636968/django-messages-for-a-successfully-delete-add-or-edit-item) post on Stack Overflow where I found code to provide a successful deletion message to the user. This was necessary as the SuccessMessageMixin does not work in a DeleteView.
Credit to the [Django Documentation](https://docs.djangoproject.com/en/4.0/ref/contrib/messages/) for information on inserting the recipe title to display in success messages.
- Credit to the [Django Documentation](https://docs.djangoproject.com/en/4.1/topics/auth/default/) for information on the LoginRequiredMixin.
- Credit to [this](https://stackoverflow.com/questions/13713077/get-user-information-in-django-templates) article on Stack Overflow for code displaying username on the base.html file.
Credit to [this](https://www.youtube.com/watch?v=Y1Us5jVT07E&ab_channel=Codemy.com) video on Youtube for the information on if else statements checking if the logged in user matches the "creator" of the recipe.
- Credit to [W3S](https://www.w3schools.com/tags/att_form_enctype.asp) for the information on "enctype" attribute which is necessary for users uploading files as part of recipe creation.

