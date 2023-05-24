# **Responsiveness**
<bt>

The site had been test for the following devices:

Mobile: 360 * 640 / 390 * 844 / 414 * 896

Tablet: 768 * 1024 / 820 * 1180 / 1366 * 768

Monitor: 1280 * 1024 / 1600 * 900 / 1950 & UP

The site had been test in Chrome seeming all according to the design. In Firefox, the animation for the regions in the index come out a bit out of shape but still fully functional. In Internet Explorer all seems to work as the design.
<br>

# **Manual Testing**
<br>
The following features are present in all the pages.
<br>

## **Navbar**
<br>
The features will be displayed according to the logged user, as marked in features page

<br>

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Logo     | Directs to the landing/index page | Click |✅|
| User Menu Icon     | Dropdown allauth options menu | Click |✅|
| Sign Up     | Directs to Sign Up Form | Click |✅|
| Sign In     | Directs to Sign In Form | Click |✅|
| Sign Out     | Directs to Sign Out Form | Click |✅|
| User name beside User Icon | Display 'guest' for unregister users  | Click |✅|
| Shopping Cart Icon | Directs to the shopping cart page | Click |✅|
| Shopping Cart Amount | Display the total of the shopping cart | Click |✅|
| Toggle Menu Icon - Small devices     | Dropdown menu options | Click |✅|
| Store | Directs to the store page, wares list | Click |✅|
| News | Directs to the news page, news list | Click |✅|
| Search | Render wares according to user's input | Click |✅|
<br>

**Register User**
<br>

| Feature       | Expected           | Action| Result|
| ------------- |:-------------:| :-----|-----:|	 	
| User name beside User Icon | Display user's name when logged in | Click |✅|
| My Profile     | Directs to the request user profile page | Click |✅|
| Sign Out     | Directs to Sign Out Form | Click |✅|
<br>

**Staff User**
<br>

| Feature       | Expected           | Action| Result|
| ------------- |:-------------:| :-----|-----:|	 	
| User name beside User Icon | Display user's name when logged in | Click |✅|
| Staff Panel     | Directs to the Staff Panel page | Click |✅|
| Sign Out     | Directs to Sign Out Form | Click |✅|
<br>


## **Messages**
<br>
The features will be displayed for all the users, as marked in features page

<br>

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Message in top rigth of screen     | Floating message according to the user action | Triggered by user action |✅|
<br>

## **Top Button**
<br>
The features will be displayed for all the users, as marked in features page
<br>

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Top Button     | Display when user scroll screen down | Triggered by user action |✅|
| Top Button     | Takes screen to top | Click |✅|
<br>


## **Footer**
<br>
The features will be displayed according to the user actions, as marked in features page

<br>

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Subscribe Newsleeter Form | Verify if mail is register already and gives feedback to user | On Submit button |✅|
| Subscribe Newsleeter - Success | If user subscribtion went successful | Response to form action |✅|
| Subscribe Newsleeter - Fail | If user subscribtion failed | Response to form action |✅|
| Facebook | Directs to e-commerce's facebook in new tab | Click |✅|
| Q&A | Directs to the questions and answers page - underconstruction | Click |✅|
| Terms & Conditions | Directs to the terms and conditions page - underconstruction | Click |✅|
| Contact Us | Directs to Contact Us Form page | Click |✅|
| Contact Us - Success | Directs to Contact Us Success page | Click |✅|
<br>

**From here the features are present just in the page they are mentioned.**

## **Landing Page**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Accordion of Images     | Allows interaction and display animation | Click on |✅|
| Animated Text    | Visual slogan with word game | - |✅|
<br>

## **Store Page**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Animated Deliver Banner      | Display the delivery conditions | - |✅|
| Categories Filters Bar       | Display the Categories filters | - |✅|
| Categories Filters Bar    | Dropdown the menu with the subcategories according to the one clicked on | Click |✅|
| Pagination    | Display according to the page the user is in, it would show prev or next plus
||  a set of pages | Click |✅|
| Pagination | Directs to the clicked page | Click |✅|
| Wares Cards | Up to 4 by pagination | - |✅|
| Wares Cards - QBuy button | Add the product to the shopping cart | Click |✅|
| Wares Cards - Link | Directs to the selected ware details page | Click |✅|
<br>

## **Ware Details Page**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Back to Store Button       | Directs to Store page  | Click |✅|
| Display images accordion       | Accordion with ware images - interaction with user  | Click |✅|
| Add To Cart Button       | Add the ware to the shopping cart  | Click |✅|
| Reviews       | Render ware reviews and staff replies to  | - |✅|
| Images Toggle Button       | Display all the images in bigger size than accordion   | Click |✅|
<br>

**Unregister User**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Invitation to sign up or sign in to be able to leave a review | Directs to Sign Up or Sign In as clicked on  | Click |✅|
<br>

**Register User**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Bookmark Button       | Button that display the state of the ware,
||if bookmarked or not and save the action  | Click |✅|
| Link to Leave a Review       | Opens a Pop Up form for it  | Click |✅|
<br>

**Staff User**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Edit Ware Button       | Open the form fill with the ware to be edit  | Click |✅|
| Delete Ware Button       | Open a pop up form to confirm the ware to be delete  | Click |✅|
| Reply Review Toggle Button       | Display a form to reply the user review   | Click |✅|
| Delete Images Button       | Open a pop up form to confirm the image to be delete  | Click |✅|
<br>

## **News Page**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Pagination    | Display according to the page the user is in, it would show prev or next plus
||  a set of pages | Click |✅|
| Pagination | Directs to the clicked page | Click |✅|
| News Cards | Up to 4 by pagination | - |✅|
<br>

## **News Details Page**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Back to News Button       | Directs to News page  | Click |✅|
| Source Link       | Directs the user to the source of the new - new tab  | Click |✅|
<br>

**Staff User**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Edit New Button       | Open the form fill with the new to be edit  | Click |✅|
| Delete New Button       | Open a pop up form to confirm the new to be delete  | Click |✅|
<br>

## **Staff Page**

**Staff Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Add Ware Button   | Directs to a form page for it  | Click |✅|
| Add Image Button   | Directs to a form page for it  | Click |✅|
| News Entry Button   | Directs to a form page for it  | Click |✅|
| Orders   | Directs to a page where the orders are render  | Click |✅|
| Contacted Us   | Directs to a page where the inquiries are render  | Click |✅|
| Search Wares  | Display the ware or wares, according to staff input  | Click |✅|
<br>

### **Staff Forms**
<br>

| Feature       | Expected           | Action | Result |
| ------------- |:-------------| :-----|-----:|
| Add Ware Form   | Save and trigger message  | Click |✅|
| Edit Ware Form   | Save and trigger message  | Click |✅|
| Delete Ware Form   | Delete and trigger message  | Click |✅|
| Add Image Form   | Save and trigger message  | Click |✅|
| Delete Image Form   | Delete and trigger message  | Click |✅|
<br>

## **Shopping Cart**

**Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Remove  | Remove the item from the shopping cart | Click |✅|
| Update Qty | Modify the quantity of the item as user's input | Click |✅|
| Keep Shopping Link | Returns the user to the store | Click |✅|
| Secure Checkout Link | Directs to the Checkout Form page | Click |✅|
<br>

## **CheckOut Page**

**Unregister Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Form to fill  | Form with required fields, validate | - |✅|
| Payment fields  | Form with required fields, validate | - |✅|
| Adjust Cart Link | Returns the user to the shopping cart | Click |✅|
| Complete Order Link | Directs to the Checkout Success page if successful | Click |✅|
<br>

**Register Users**
<br>
| Feature       | Expected           | Action| Result|
| ------------- |:-------------| :-----|-----:|
| Form to review, prefill  | Form filled with profile user's data, validate required fields | - |✅|

