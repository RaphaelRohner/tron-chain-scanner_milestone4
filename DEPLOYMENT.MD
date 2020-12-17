# 20/11/2020

  - #1 Installed Django and started README file.

  - #2 Added user stories to README file.

  - #3 Uploaded product images and background.

  - #4 Uploaded wireframes and added them to README file.

  - #5 Added DB model link to README file and started table of contents with anchor links.

  - #6 Started project tron_chain_scanner, added to gitignore, ran first migration, added superuser and removed secret_key.

  - #7 Installed Allauth, added authentication backends, apps, site ID and paths and migrated.

  - #8 Corrected path, defined email backends, changed login redirect and created Allauth templates folder.

# 21/11/2020

  - #9 Added Allauth templates, created base.html from Bootstrap Starter template.

  - #10 Base.html: Wrapped imports in blocks. Added header and message container.

  - #11 Added Page Content placeholder blocks. Started Home App, created templates folder and index.html.

  - #12 Filled index.html with dummy, created Home view, connected Home And Main App via views.py, urls.py and settings.py.

  - #13 Added homepage content and header block to index.html.

  - #14 Fixed wireframe links in README file.

  - #15 Added header to base.html.

  - #16 Added account dropdown and shopping bag total to header and wrapped it in a row.

  - #17 Added base.css to folder static. Moved images from static to folder media. Styled homepage in base.css. Added static and media to settings.py and urls.py.

  - #18 Added navigation to base.html.

  - #19 Added includes main-nav.html and mobile-top-header. Created navigation dropdowns in main-nav.html.

  - #20 Created header for mobile views in mobile-top-header.html.

  - #21 Added css class for banner.

# 22/11/2020

  - #22 Added App products, uploaded fixtures and added app to settings.py.

  - #23 Added category and product models to products/models.py. Installed Pillow and made migrations.

  - #24 Registered product model in admin.py.

  - #25 Imported categories fixture, removed typo in products fixture and imported it. Checked model in /admin.

  - #26 Added meta class verbose to models.py. Reordered fields in admin by adding categories and product class to admin.py and registering them.

  - #27 Added general products view to views.py. Created products/urls.py. Registered path in main urls.py. Created products.html.

  - #28 Added overlay to products.html. Added class overlay to base.css. Added content block to display products responsive with horizontal rule depending on number of products per row.

  - #29 Linked navigation Merch > All Products to products.html.

  - #30 Created Heroku App. Installed Postgres, Dj-Database, PsycoPG2 and updated requirements.txt.

  - #31 Connected database to Heroku.

  - #32 Set database source depending on environment in settings.py. Installed Gunicorn and updated requirements.txt.

  - #33 Created Procfile, disabled static file collection, allowed Heroku host.

  - #34 Fixed Procfile.

  - #35 Deployed to Heroku and added secret key and changed debug mode.

 # 23/11/2020

  - #36 Created AWS bucket and user. Installed Boto3 and Django-Storages. Updated requirements.txt.

  - #37 Added AWS keys to Heroku. Added AWS to settings.py and created custom_storages.py.

  - #38 Fixed bucket name.

  - #39 Added cache control to settings.py.

  - #40 Changed background image and checked Heroku and AWS deployment.

  - #41 Created product detail view, added URL pattern and created product_detail.html.

  - #42 Linked to product details and added some top padding for mobile view.

 # 24/11/2020

   - #43 Added search functionality to products > views.py, base.html and mobile-top-header.html.

   - #44 Added clothing categories to main-nav.html. In products > views.py added category filtering to all_products view.

   - #45 Added homeware and offer categories to main-nav.html. Changed category jeans to caps.

   - #46 Added sorting to main-nav.html. In products > views.py added sorting functionality to all_products view.

   - #47 Added product category to product.html.

   - #48 Added product category to product_detail.html.

   - #49 Added category display under headline.

   - #50 Added category styling to base.css. Fixed html indentation in products.html.

   - #51 Added sort options to products.html and views.py.

# 25/11/2020

  - #52 Added sort function to products.html.

  - #53 Added back to top button to products.html and styled it in base.css.

  - #54 Created bag app, app view in bag > views.py and basic bag.html.

  - #55 Created urls.py, added path to project > urls.py, added hrefs for bag to base.html and mobile-top-header.html. Added basic bag html structure.

  - #56 Created contexts.py to bag app.

  - #57 Added the free delivery context processor to settings.py.

  - #58 Added form to purchase product to product_detail.html. Added reverse style css classes for buttons to base.css.

  - #59 Added add to bag view to bag > views.py and added url pattern to urls.py.

  - #60 Added function to add up added products to bag > contexts.py.

  - #61 Added list of items in shopping bag to bag.html.

# 26/11/2020

  - #62 Added sizes to product model and size selector box to product template.

  - #63 Updated products with or without sizes in admin console.

  - #64 Added size logic to bag > contexts.py and views.py, changed product categories for two items in admin console.

  - #65 Added javaScript functionality to change product purchase amount.

  - #66 Limited product amount between 1 and 99 in quantity_input_script.html.

  - #67 Added quantity change to shopping bag.

  - #68 Added change quantity button functionality to bag.html.

  - #69 Added update and remove buttons to products in shopping bag and changed mouse pointer.

# 28-11-2020

  - #70 Added view to change product quantity in bag > views.py, path to bag > urls.py and action to bag.html.

  - #71 Added view to remove product from bag in bag > views.py and path to bag > urls.py.

  - #72 Changed variable size and data in bag.html to contain product_size. Updated remove link in bag.html. Replaced JQuery slim with JQuery min in base.html.

  - #73 Created bag_tools.py and __init__.py in folder templatetags. Added view to calculate subtotal and added it to bag.html.

  - #74 Created toasts folder in main templates folder. Added toast_success.html and added success message.

  - #75 Created toast_error.html, toast_info.html and toast_warning.html. Added error, info and warning messages to html files.

  - #76 Included toast messages to base.html messages container and poastloadjs block. Added success message to views.py and message_storage to settings.py.

  - #77 Styled toasts in base.css. Added if, elif, else statement to message block to display different toasts by status.

  - #78 Added toast messages for all add, update and remove cases to views.py.

  - #79 Added arrow and a arrow colors for toast messages to base.css.

  - #80 Added shopping bag preview to toast_success.html.

  - #81 Created checkout App and registered it in settings.py. Added models Order and OrderLineItem to models.py.

  - #82 Created model methods to create order number, update total, rewrite and return order number. Created methods to set lineitemtotal and order total and return SKU and order number.

  - #83 Made migrations for order model.

  - #84 Defined fields for the Admin menu that can be edited or a muted in checkout > admin.py.

  - #85 Created signals.py with functions to update and delete order total. Imported checkout signals to apps.py.

  - #86 Created forms.py and a class with function to set placeholders for form fields by iterating through them.

  - #87 Created checkout view and urls.py with path. Added url pattern to main App. Added checkout html and css structure. Installed Crispy Forms and added it to settings.py. Updated requirements.

  - #88 Created checkout.html with item overview, form to enter details and buttons.

  - #89 Added context processor to settings.py and added link to button to secure checkout.

# 29/11/2020

  - #90 Added css styles for Stripe credit card field to checkout > checkout.css. Added Stripe JS import to base.html.

  - #91 Installed Stripe. Defined ENV variables in settings.py. Updated requirements. Added JS logic to stripe_elements.js. Added Stripe JS import to checkout.html and views.py.

  - #92 Added CSS formatting for Stripe field to checkout.css.

  - #93 Added event listener to handle errors during card entry to checkout > stripe_elements_js.

  - #94 Added payment intent to views.py.

  - #95 Added event listener to handle form submits to checkout > stripe_elements.js.

  - #96 Fixed variable namesfor Stripepayments, uncommented some imports. Tested payment and checked it on Stripe's side.

  - #97 Added post method to checkout view in checkout > views.py.

  - #98 Added view for successfull orders and imported dependencies.

  - #99 Added path for checkout success. Added checkout app to __init__.py. Added option for 0 line orders. Added checkout_success.html template.

  - #100 Added class to overwrite save methods in checkout > models.py. Fixed signals.py name and fixed indentation error in views.py. Checked functionality on site, in admin and on Stripe.

  - #101 Added order summary to order_success.html, displaying available information.

  - #102 Added loading spinner to checkout.html, styled it in checkout.css and added it submit event listener. Checked 3D Secure payment.

  - #103 Added webhook_handler.py to checkout app.

  - #104 Added handlers for successfull and failed payments to webhook_handler.py. Added path and dependencies to urls.py.

  - #105 Added webhooks.py listening for messages from Stripe. Tested webhook functionality.

  - #106 Added webhook handlers for payment intent succeed and failed. Tested functionality.

  - #107 Added billing and shipping details to send to Stripe to stripe_elements.js.

  - #108 Added view to checkout > views.py to check if the save information checkbox is checked.

  - #109 Added path for checkout. Added post and fail functionality to Stripe payment in stripe_elements.js.

  - #110 Added functionality to check if order already exists and delay in order to prevent multiple submissions in webhook_handler.py. Made migrations.

  - #111 Added hidden field, variables for original bag and dependencies to check for duplicate order.

  - #112 Fixed webhook secret key and checked functionality.

  - #113 Re-ordered input fields in checkout.html, changed county placeholder, installed django-countries and updated requirements.

  - #114 Changed country field in checkout.html to drop-down, styled the field and removed placeholder.

  - #115 Created profiles app and profiles model. Added user profile to checkout. Made migrations.

  - #116 Created basic profile view, added it to urls.py. Added view to main app. Created basic profile template and CSS style.

# 30/11/2020

  - #117 Adjusted Allauth account templates to site style.

  - #118 Styled Allauth templates in base.css.

  - #119 Tested user registration. Added settings to profile view and linked profiles from base.html and profile.html.

  - #120 Added profiles > forms.py function for placeholders.

  - #121 Added form to views.py, profile.html and styled the form elements in profile.css.

# 02/12/2020

  - #122 Added CSS and JS to style the country drop-down, added postload JS block.

  - #123 Added post handler for profile update and adjusted toast success message.

  - #124 Added order history to profile.html.

  - #125 Styled order history with CSS, added order history view, added path.

  - #126 Added button to checkout success displaying depending if user has a profile. Added order history to checkout success.

  - #127 Added autofill to checkout form.

# 03/12/2020

  - #128 Added save user data functionality to webhook_handler.

  - #129 Added confirmation email subject and body.

  - #130 Added functionality to send confirmation email.

  - #131 Added forms.py to products to create form to add products.

  - #132 Added add products view and path.

  - #133 Added add products page.

  - #134 Fixed adding products without image.

  - #135 Added edit product page.

  - #136 Added edit products view.

  - #138 Added paths for edit and delete. Added delete product view.

  - #139 Added edit and delete options to products and product details.

  - #140 Restricted add, edit and delete to superuser.

  - #141 Added Django image widget for edit product view.

# 05/12/2020

  - #142 Styled product form in base.css. Wrapped the crispy form in a for loop to iterate through the fields in add and edit.html.

  - #143 Added success message for changes to add and edit.html and tested functionality.
    - Tested adding, editing and deleting product as admin.
    - Tested messages.
    - Tested adding and removing product image.
    - Tested blocked availabilty of these functions as not admin.

  - #144 Updated requirements.txt. Added Stripe keys to Heroku app. Added Stripe webhook for Heroku app.

  - #145 Setup email depending on environment with chibitalesorg@gmail.com.

# 06/12/2020

  - #146 Resubmitted migrations and HEroku DB connection. Try to fix Heroku App Server Error 500.

  - #147 Resubmit Heroku deployment to fix login in Heroku App.

  - #148 Try removed line break to fix login issue.

  - #149 Removed default email duplette from settings.py.

  - #150 Checked registration process with Heropku app, worked. Emptied Heroku DB, remigrated, added Superuser.

    - After submit in Heroku App: Tested Registration, login and order process and emails including confirmation.

  - #151 Checked Heroku App functionality. Styled mobile view for login and register page.

  - #152 Added links to homepage to main nav and mobileheader.

  - #153 Split Shopping Bag content into html files. Added mobile only element giving summary at the top. Added jump to top button.

  - #154 Started removing unused files and imports, splitting lines > 79 where possible and ignoring the rest, ignoring no member message.

  - #155 Corrected Typo in bag-total.html.

# 07/12/2020

  - #156 Corrected or ignored Flake8 and other error messages. Tested App functionality.

# 11/12/2020

  - #157 Added user's full name to profile app.

  - #158 Try to find Heroku error.

  - #159 Added DB synch with Heroku DB to Procfile.

  - #160 First try with adjusted webhook_handler to send html and plain text order confirmation email.

  - #161 Second try with adjusted webhook_handler to send html and plain text order confirmation email.

  - #162 Added basic html to order confirmation email.

  - #163 Added products to order confirmation email.

# 14/12/2020

  - #164 Added sizes to t-shirts an polos.

  - #165 Created addresses app and added address model.

  - #166 Created basic address view.

  - #167 Added urls.py and basic addresses html template.

  - #168 Corrected project url for addresses and tested functionality.

# 15/12/2020

  - #169 Added address form and view.

  - #170 Added Manage Addresses button to profile template.

  - #171 Added address list to address template.

  - #172 Created filter so only user addresses will list.

# 16/12/2020

  - #173 Added functionality to add a new address.

  - #174 Set some of the address fields for additional addresses as required.

# 17/12/2020

  - #175 Added list of available addresses.

  - #176 Created apps freescanner and walletscanner and registered them in settings.py. Insatlled Trongrid.

  - #177 Created basic walletscanner page and linked it in navigation.

  - #178 Created basic freescanner page and linked it in navigation.

  - #179 Installed trongrid and added check if Tronlink is connected on walletscanner page.

