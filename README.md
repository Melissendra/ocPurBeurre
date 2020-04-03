# Projet 5 - ocPurBeurre

******

## Introduction
This application have to help the user finding aliments substitutes, registering them to find it again another time.
At first, the user have to write what food he wants to substitute. Then the app will suggest different aliments that can replace it. To do so, the program will search in a database that we'll create with the help of Openfoodfacts' api.

****

## Description
When the user launch the application, the first Menu display:
1. Quel aliment voulez-vous remplacer?
2. Retrouver mes aliments substitués.
3. Quitter

### Choice 1:
The application will display another menu where it invite the user to choose a category in which he wants to search in some random products. After the user's choice, the application continue by showing a list of 20 random products within the category chosen. Each products have a nutriscore of 'c', 'd' or 'e'. The consumer choose a product and the the application displays 10 random healthier products with a nutriscore 'a' or 'b'. He choose the food that has his interests and he enters a new menu displaying all the informations of the product: name, link to openfoodfacts, store where he could find it and again the nutriscore. He can then save it in his favorite, return to the substitutes' products list, return to the categories' menu, return to the home page or quit.

### Choice 2:
The application will display all the products saved by the user with their full description. The user can delete all its favorites if he wants or return to the home page or quit.

### Choice 3:
The user quit the program and the app is stopped.

## Functionality
The program fetch the product from OpenFoodFacts and put it in the database. The program suggests an healthier product with its name, store where to find it nutriscore... The user choose a number or a letter within the menu choices. If the user's choice is wrong, the application display the same menu again. The research is done into the database thanks to requests done in python

## How to install your environment to use the app:
1. Clone file:  git@github.com:Melissendra/ocPurBeurre.git
2. Create a database in your local environment.
3. To link it to the app create in ocpurbeurre program a *.env* file
4. In it write: DATABASE_URL = mysql+mysqlconnector://user_name:password@localhost:3306/database_name?charset=utf8mb4
5. Then inside ocPurBeurre directory in your terminal, do "*pipenv install*", to install all the requeriments: python 3.8.2, records, requests, mysql-connector-python, contain in the pipfile
6. Do "*pipenv shell*"to activate the virtual environment
7. Do *python -m install* to create the tables and insert the products into it
8. Do *python -m main* to launch the app and choose.
