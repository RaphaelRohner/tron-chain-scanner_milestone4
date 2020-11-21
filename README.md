# Tron Chain Scanner - Milestone Project 4 - Full Stack Frameworks with Django

The Tron Chain Scanner website will offer:
* A freepage to get an overview about movements on the Tron blockchain.
* An option to buy access to more search features by using the Tronlink wallet in Chrome on desktop.
* A demo merchandise shop with Stripe integration to purchase merchandise articles using Stripe.

## Table of contents

* UX

  * User Stories
    * [Viewing and Navigation](#viewing-and-navigation)
    * [Registration and Accounts](#registration-and-accounts)
    * [Sorting and Searching](#sorting-and-searching)
    * [Purchasing and Checkout](#purchasing-and-checkout)
    * [Administration and Store Management](#administration-and-store-management)

  * Wireframes / Mockups
    * [Desktop](#desktop)
    * [Mobile](#mobile)

* [Database Structure](#database-structure)

## UX

### User Stories

#### Viewing and Navigation

* As a visitor I want a quick overview about token movements on the Tron chain to notice trends.
* As a visitor I want to filter information about the Tron chain easily using selectors to find what I am looking for.
* As a visitor I want to sign up with my wallet by just doing a payment while keeping my privacy to personalise my research.
* As a visitor I might get interested in merchandise articles and want to browse them to possibly buy them.
* As a visitor I want to filter the available merchandise using a search to find items I am interested in.
* As a visitor I want to filter merchandise by predifined categories to find items I might be interested in.
* As a shopper I want to see relevant information about products to help me to decide if I want to buy it.
* As a shopper I want to see special offers, which I consinder as a bargain to buy them.
* As a shopper I want to be able to identify items which might not be available much longer to buy those.
* As a shopper I want to see how much money I already spent to keep track of my expenses.

#### Registration and Accounts

* As a visitor I want to have the opportunity to find information about Tron tokens without paying or registering to feel welcome.
* As a wallet user I want to get information about my portfolio without giving away my details to stay anonymous.
* As a wallet user I want to register just using my wallet to access information.
* As a user I want to pay for my usage in time units to cap my expenses.
* As a customer I want to be able to purchase merchandise just using my credit card.
* As a customer I want to be able to create an account to store my information.
* As a customer I want to be able to easily log into the account to access my data.
* As a customer I want to be able to recover my account to regain access.
* As a customer I want to get email notifications when registering or buying merchandise.
* As a customer I want to be able to edit my user profile to make necessary changes.
* As a customer I want to store multiple delivery addresses to send out presents.

#### Sorting and Searching

* As a visitor I want to sort Tron tokens by name, amount, price and transactions to find relevant information.
* As a wallet user I want to add wallets to my profile to get an overview about my holdings.
* As a wallet user I want to see information like my total holdings, current value and growth over periods of time to understand my portfolio.
* As a wallet user I want to add certain contracts to track them.
* As a wallet user I want to store and name these contracts to keep them stored.
* As a customer I want a sort list of available products to identify the best available products.
* As a customer I want to sort a specific category of product to narrow down my search results.
* As a customer I want to sort multiple categories or products simultaneously to extend my search results.
* As a customer I want search for a product by name or description to find a specific product.
* As a customer I want to easily see what I‘ve searched for and the number of results to get an overview.

#### Purchasing and Checkout

* As a wallet user I want to send TRX to an address to buy usage time.
* As a wallet user I want to know the current pricing in a stable price to see how much I will need to pay and send.
* As a wallet user I want to see how much time I purchased to be informed about my available time window.
* As a customer I want to select the size and quantity of a product when purchasing it to modify my order.
* As a customer I want to view my shopping bag to see the total cost and products I will purchase.
* As a customer I want to modify the quantities and products in checkout to adjust my purchase.
* As a customer I want to add alternative delivery addresses to send my purchase to a different address.
* As a customer I want to store multiple delivery addresses to keep them at hand.
* As a customer I want to easily enter my credit card information to pay my purchase.
* As a customer I want to use a well known payment processor to feel safe about my credit card details.
* As a customer I want to see an order summary after checkout to confirm my purchase.
* As a customer I want to receive a confirmation email to have proof of my purchase and its costs.

#### Administration and Store Management

* As the store owner I want to add manually new products to keep my shop up to date.
* As the store owner I want to edit product details to adjust them to changing circumstances.
* As the store owner I want to delete items that are out of stock to avoid orders I can not fulfill.

### Wireframes

#### Desktop

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


#### Mobile

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