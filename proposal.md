# Pantry Trackr

#### _A pantry tracker with a little twist—frozen vegetables and frozen meat—because Pantry Trackr exists to track non-perishable foods and drinks that your family always has on hand._

#### By _**JoHannah Joy**_

## Project Overview

The Pantry Trackr app tracks the non-perishable food you have and the non-perishable food you need simultaneously. At their first log in, users add what they currently have in their pantry (non-perishables) as well as frozen meats and vegetables. Have you ever not had enough sugar or flour? Or started making spaghetti but couldn't find any marinara sauce? Have you ever found yourself at the grocery store unsure of what is getting low in your pantry? The driving reason for tracking non-perishables is that non-perishables aren't generally purchased every week. We tend to purchase multiple or in bulk when it comes to non-perishables such as pasta, canned foods, frozen vegetables, and oats. The Pantry Trackr app allows users to set their typical pantry items as well as set a minimum quantity they want to have stored at all times.

### Frameworks/Libraries

* Vue
* Django REST
* JS

## User Stories / Features

As a user I want a pantry tracker so that I never run out of things I need/like to keep on hand.

Tasks/Features:
* users create account
* users create pantry with the ability to add more items in the future
* users will set quantity minimum of each item so that when 
* in the 'Used a Pantry Item' section, users subtract the quantity of each pantry items used...when their quantity in storage is below the minimum they set, that item will be automatically added to 'Shopping List'
* if time allows to code, there will be an optional 'photo upload' button for users to upload photos of the item brands they enjoy
* on the 'My Pantry' page, each item listed is the user's non-perishable food they like to get. Each item will have 2 numbers below it: the quantity in the pantry currently and the quantity needed (total number to have stored at all times will be set by user and arithmetic will be coded)


## Data Model

_What data will you need to store as part of your application?_

* User (create account, login, profile)
* PantryItem (add an item, add quantity minimum, subtract quantity used)
* QuantityMinimum (user creates min. quantity per item)


## Schedule

_Use of Trello to keep me on track._

* Week 1: Research, Proposal, setup Django REST, begin API for non-perishables
* Week 2: complete API, functionality for create account/login/account (user model), functionality for 'Add An Item' (create pantry), functionality for displaying all added items in 'My Pantry'
* Week 3: functionality for 'Used A Pantry Item' which then outputs to 'Shopping List', functionality for optional add photo, add 'How To Use Pantry Trackr' section, CSS
* After Capstone is Finished: Mobile Design (is that easy in Django?), deployment?