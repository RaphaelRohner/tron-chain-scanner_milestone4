# Tron Chain Scanner - Milestone Project 4 - Full Stack Frameworks with Django

# Table of contents

1. UX

    * [Project Goals](#project-goals)

    * [Business Goals](#business-goals)

    * [User Goals](#user-goals)

    * [Developer Goals](#developer-goals)

    * [User Stories](#user-stories)
      * [Viewing and Navigation](#viewing-and-navigation)
      * [Registration and Accounts](#registration-and-accounts)
      * [Sorting and Searching](#sorting-and-searching)
      * [Purchasing and Checkout](#purchasing-and-checkout)
      * [Administration and Store Management](#administration-and-store-management)

    * [Design Choices](#design-choices)  

    * [Wireframes](#wireframes)
      * [Desktop](#desktop)
      * [Mobile](#mobile)
      * [Database Structure](#database-structure)

2. [Features](#features)
    * [Existing Features](#existing-features)
    * [Features left to implement](#features-left-to-implement)
    * [Hard or impossibleto solve](#hard-or-impossible-to-solve)

3. [Technologies used](#technologies-used)

4. [Testing](#testing)

5. [Deployment](#deployment)

6. [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Code](#code)
    * [Acknowledgements](#acknowledgements)

# UX

## Project Goals
  * The milestone project is the base for a website which allows visitors to:
    * Browse aspects of the Tron blockchain anonymously and free. (Just basic implementation yet.)
    * Browse additional aspects of the chain by purchasing an anonymous account based and a Tronlink wallet. (Just basic implementation yet.) 
    * Purchase merchandise articles using Stripe without registering. (Implemented)
    * Purchase merchandise and storing account information by creating an account.(Implemented)
    * Store additional addresses in the profile and select these to purchase merchandise. (Implemented)
    * Store and access relevant contract addresses of the Tron blockchain. (Just basic implementation yet.)

## Business Goals
  * From a business point of view the website serves these purposes:
    * Offering an easy to use merchandise shop to fund the free service and create income.
    * Offering a free service to attract site users, which might turn into customers.
    * Offering easy to use advanced services to fund the business. 

## User Goals
  * From a users perspective the website offers the following advantages:
    * A free to use service to get information about the Tron blockchain.
    * Giving the option to access advanced services by just using the anonymous Tronlink wallet.
    * Offering goods which can be purchased without registering.
    * Offering advanced options by registering for an user account.

## Developer Goals
  * As a developer interested in the Tron blockchain, the project offers:
    * A possible working business model based on the evolving blockchain technology.
    * An interesting approach to allow card payments as well as token payments.
    * A starting point in exploring the options and possibilities of the Tron blockchain.
    * A possible blueprint to expand to other blockchains.
    * Combining multiple web technologies to serve these purposes.

## User Stories
It was not possible to achieve all the following goals. Not implemented user stories are striked out.
They are still in this file as a guideline for future developments and allow an insight where this site is heading to.

### Viewing and Navigation

* As a visitor I might get interested in merchandise articles and want to browse them to possibly buy them.
* As a visitor I want to filter the available merchandise using a search to find items I am interested in.
* As a visitor I want to filter merchandise by predifined categories to find items I might be interested in.
* As a shopper I want to see relevant information about products to help me to decide if I want to buy it.
* As a shopper I want to see special offers, which I consinder as a bargain to buy them.
* As a shopper I want to be able to identify items which might not be available much longer to buy those.
* As a shopper I want to see how much money I already spent to keep track of my expenses.
* <s>As a visitor I want a quick overview about token movements on the Tron chain to notice trends.</s>
* <s>As a visitor I want to filter information about the Tron chain easily using selectors to find what I am looking for.</s>
* <s>As a visitor I want to sign up with my wallet by just doing a payment while keeping my privacy to personalise my research.</s>

### Registration and Accounts

* As a customer I want to be able to purchase merchandise just using my credit card.
* As a customer I want to be able to create an account to store my information.
* As a customer I want to be able to easily log into the account to access my data.
* As a customer I want to be able to recover my account to regain access.
* As a customer I want to get email notifications when registering or buying merchandise.
* As a customer I want to be able to edit my user profile to make necessary changes.
* As a customer I want to store multiple delivery addresses to send out presents.
* <s>As a visitor I want to have the opportunity to find information about Tron tokens without paying or registering.</s>
* <s>As a wallet user I want to get information about my portfolio without giving away my personal details.</s>
* <s>As a wallet user I want to register just using my wallet.</s>
* <s>As a user I want to pay for my usage in time units to cap my expenses.</s>

### Sorting and Searching

* As a wallet user I want to add certain contracts to track them.
* As a customer I want a sort list of available products to identify the best available products.
* As a customer I want to sort a specific category of product to narrow down my search results.
* As a customer I want to sort multiple categories or products simultaneously to extend my search results.
* As a customer I want search for a product by name or description to find a specific product.
* As a customer I want good search results and the number of results to get an overview.
* <s>As a visitor I want to sort Tron tokens by name, amount, price and transactions to find relevant information.</s>
* <s>As a wallet user I want to add wallets to my profile to get an overview about my holdings.</s>
* <s>As a wallet user I want to see information like my total holdings, current value and growth over periods of time to understand my portfolio.</s>
* <s>As a wallet user I want to store and name these contracts to keep them stored.</s>

### Purchasing and Checkout

* As visitor I want an option to donate to the website if I enjoy it.
* As a customer I want to select the size and quantity of a product when purchasing it to modify my order.
* As a customer I want to view my shopping bag to see the total cost and products I will purchase.
* As a customer I want to modify the quantities and products in checkout to adjust my purchase.
* As a customer I want to add alternative delivery addresses to send my purchase to a different address.
* As a customer I want to store multiple delivery addresses to keep them at hand.
* As a customer I want to easily enter my credit card information to pay my purchase.
* As a customer I want to use a well known payment processor to feel safe about my credit card details.
* As a customer I want to see an order summary after checkout to confirm my purchase.
* As a customer I want to receive a confirmation email to have proof of my purchase and its costs.
* <s>As a wallet user I want to send TRX to an address to buy usage time.</s>
* <s>As a wallet user I want to know the current pricing in a stable price to see how much I will need to pay and send.</s>
* <s>As a wallet user I want to see how much time I purchased to be informed about my available time window.</s>

### Administration and Store Management

* As the store owner I want to add manually new products to keep my shop up to date.
* As the store owner I want to edit product details to adjust them to changing circumstances.
* As the store owner I want to delete items that are out of stock to avoid orders I can not fulfill.

## Design Choices

* The design is taken from the Code Institute walkthrough project Boutique Ado.
* It was kept in black in white, just with some grey and blue to distinguish form fields and links.
* To emphasize the Tron relation, the red Tron logo on the homepage is the only major color effect.
* The simplistic design suits the purpose of a mainly data focussed website.
* The font is Lato in different variations which suits this approach.
* The form elements are kept simple in the same manner.
* Buttons were kept in black and white with invert hover effects.
* The buttons were styled to mirror each other when there is more than one button on the site.

## Wireframes

### Desktop

* [Desktop Home Screen](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Home.png)
* [Desktop Shop](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Shop.png)
* [Desktop Free Scanner](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Free_Scanner.png)
* [Desktop Wallet Scanner No Tronlink](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Wallet_Scanner_No_Tronlink.png)
* [Desktop Wallet Scanner No Payment](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Wallet_Scanner_No_Payment.png)
* [Desktop Wallet Scanner](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Wallet_Scanner.png)
* [Desktop Sign In](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Sign_In.png)
* [Desktop Product Details](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Product_Details.png)
* [Desktop Shopping Bag](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Shopping_Bag.png)
* [Desktop Order Checkout](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Order_Checkout.png)
* [Desktop Order Confirmation](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_Order_Confirmation.png)
* [Desktop User Profile](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_User_Profile.png)
* [Desktop User Addresses](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Desktop_User_Addresses.png)


### Mobile

* [Mobile Home Screen](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_Home.png)
* [Mobile Shop](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_Shop.png)
* [Mobile Free Scanner](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_Free_Scanner.png)
* [Mobile Wallet Scanner No Tronlink](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_Wallet_Scanner_No_Tronlink.png)
* [Mobile Sign In](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_Sign_In.png)
* [Mobile Product Details](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_Shop_Product_Details.png)
* [Mobile Shopping Bag](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_Shop_Shopping_Bag.png)
* [Mobile Order Checkout](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_Shop_Checkout.png)
* [Mobile Order Confirmation](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_Order_Confirmation.png)
* [Mobile User Profile](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_User_Profile.png)
* [Mobile User Addresses](https://e0a02054-1c91-47e2-9024-adcdb3829a68.ws-eu01.gitpod.io/mini-browser/workspace/tron-chain-scanner_milestone4/static/wireframes/Mobile_User_Addresses.png)

## Database Structure

* [Database Diagram](https://dbdiagram.io/d/5fb6613e3a78976d7b7c95bd)

# Features

## Existing Features
  * Freescanner App
    * The page returns a list of the top 20 WIN token holders from the TRON API.
    * It links to the identifier page, where users can create, read, update and delete contract addresses from the data model.
    * The identifier model is accessible from the admin tool as well.
    * The identifier type is predifined using a select field, defined in the form model.
    * The edit button loads the selected identifier into the form.
    * Delete actions are reconfirmed to prevent accidental deletions.
    * Every action can be aborted and brings the user back to previous page.
    * So does finishing an action which returns the updated view from the previous page.

  * Walletscanner App
    * The website checks if a Tronlink wallet is open in Chrome.
    * If Tronlink is open the address is returned.
    * If not a message informs the user to connect Tronlink.
    * The website allows to make a donation of 1 TRX from the open wallet to a predifined address.
    * The donate button does not work if Tronlink is not open.

  * User Addresses App
    * Registered users can create, read, update and delete additional delivery addresses.
    * From the checkout page users can click a link where they can select a stored delivery address.
    * The delivery address is returned to the checkout page and can be used straight away.
    * Registered users can access their additional addresses from their profile or via the checkout form.
    * The user addresses are available from the admin menu, but just as names and for testing purposes.
    * Only logged in users can use CRUD operations on their stored addresses.
    * Access via the URL was ruled out by checking if the request comes from the current user.
    * The edit button loads the selected address into the form.
    * Delete actions are reconfirmed to prevent accidental deletions.
    * Every action can be aborted and brings the user back to previous page.
    * So does finishing an action which returns the updated view from the previous page.

  * Boutique Ado features
    The project recreates the Boutique Ado features from the walkthrough project, so the following will just give an overview about the implemented and tested features:

    * The content like the navigation and the individual pages are stored in separate Django apps to prevent redundant code.
    * The navigation displays the page title.
    * The navigation offers a search function for the available merchandise articles.
    * Merchandise articles can be accessed via the navigation by multiple categories.
    * The search results return the categories as tags as well.
    * The navigation offers a link to the user profile and depending on the user, the option to login or logout and access to the admin.
    * The navigation offers an overview over the total in the shopping bag.
    * The results give an overview about found matches.
    * The results allow to sort by different criterias.
    * The results display the products with a preview and relevant information.
    * The results can be clicked and lead to the product details page.
    * On the details page users can change the amount and if given sizes of the product and add it to the their bag.
    * The administrator can access the edit view from here or delete the item.
    * The shopping bag allows to add the product to the bag.
    * When added to the bag a message allows to get to the bag by clicking a button.
    * The bag allows to change the product's quantity within defined parameters.
    * The bag allows to remove an item as well.
    * The bag lists all the items added so far and allows to shop on or go to checkout.
    * The checkout page allows a not registered user to enter the delivery information and pay via Stripe.
    * The checkout page allows logged in users to use their default address and to change it.
    * The checkout page gives an overview about the added products and their costs and delivery costs.
    * Finishing the purchase will open a connection to stripe to process the payment and return error messages if there is an error.
    * Finishing the purchase will bring the user to the success page, which summarizes the purchase.
    * Finishing the purchase will send an email to the user summarizing the purchase.
    * Finishing the purchase will create a summary for registered users, which can be accessed via their profile.
    * The profile app allows users to change their default deilvery information.
    * The profile app lists all purchases from this profile in descending order.
    * All interactions with the website will give Toast messages under the shopping bag in the navigation to inform the user.
    * Logging in as the website administrator allows to add products.
    * Accross the website it is made sure, that the user can only access content of his permission level / login status.
    * The Login page allows to reset the password by using Django Allauth and sending a password reset email.
    * Using a free delivery treshhold the user is always informed if the delivery is already free or how much more needs to be spent. 
    
## Features left to implement
  * Freescanner
    * Multiple options to scan and filter the Tron blockchain.
    * By token.
    * By transactions.
    * By value.
    * Display current market prices.
    * Display users / wallets.

  * Walletscanner
    * Creating an account by a wallet payment.
    * Auto login if wallet is open.
    * Registering multiple wallets in one account.
    * Doing queries over the chain for multiple wallets.
    * Saving search patterns and interesting contracts.

  * The Merch Shop
    * Creating a rating app for registered users to actually rate their purchases.

## Hard or impossible to solve

* Removing GitPod error messages for using Django template language with special characters.
* Removing a console error message indicating a conflict between Stripe and Tronlink.
* Accessing the wallet address received via JS to autocreate an account using Django and Postgres.
* Accessing JSON values received from the TRON API in Django in an easy way.

# Technologies used

* Git and GitPod - for project development and hosting
* HTML5 - to build the site
* CSS3 - to style the site
* javaScript - for site functionality and to access Tronlink
* jQuery 3.4.1.min - to build the search function and reduce coding
* Bootstrap 4.5.3.min - to style the site and make it responsive
* FontAwesome - to get all the icons
* Google Fonts - to use Lato font
* Django 3.1.3 - to create the projects app structure
* Django Allauth - to create user login system
* Django Toasts - to create messages on the website
* Python 3 - to communicate between frontend and backend
* SQL - to store the data on GitPod's end
* Postgres SQL - tostore the data on Heroku's end
* Trongrid - to access the Tron blockchain
* TronAPI - to use Python with the Tron chain
* Heroku - for Python project deployment
* AWS - to store static files, not storable on Heroku

# Testing

All CSS3 code is tested via the W3C CSS Validation Service.\
The website displays as expected on all devices and browsers used.\
All Python3 and Django code was tested manually.
* Read operations worked on all devices and browsers in any of many screen scales tested.
* Create operations were executed on four devices and several browsers.
* Update operations were executed on four devices and several browsers.
* Delete operations were executed on four devices and several browsers.

Navigation and responsive design was tested with the latest versions of:
* Google Chrome
* Firefox
* MS Edge
* Brave
* Opera

Navigation and responsive design was tested on:
* Mobile Alacatel A1
* Mobile Motorola G8pro
* Amazon Fire tablet
* MSI GP63 Leopard 8RE
* MacBook Air and 24inch screen

# Deployment

The project is deployed on GitHub and Heroku and accessible via the following links:

GitHub: https://github.com/RaphaelRohner/tron-chain-scanner_milestone4

Heroku: https://tron-chain-scanner.herokuapp.com/

Static content is hosted with AWS.

All current secret keys are stored in environment variables and were not deployed at any point.

# Credits

## Content
  * Tron blockchain info comes from the Tron blockchain.

## Media
  * The basic vector graphics for the products come from: https://www.freepik.com/
  * The Tron logo comes from the Tron Foundation: https://tron.guide/resources/tron-logo-kit/

## Code
  * The project is heavily based on Codeinstitute's Boutique Ado walkthrough project.
  * The code to access the Tron API comes from the Tron Foundation.  * 

## Acknowledgements
  * Many thanks to Codeinstitute for providing this course and especially the Boutique Ado project.
  * Thank you to all the tutors of Codeinstitute for providing the amazing support they offer.
  * A massive thank you to Aaron my mentor from Codeinstitute for all the support.
  * And big thumbs up to everyone @Slack, w3schools and stackoverflow. Without your answers to other problems, I wouldn't have figured out the solutions to mine!