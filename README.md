![](/readme_docs/readme_imgs/am-i-responsive.png)
<br>
Live Site: [💻](!https://sebs-toy-store.herokuapp.com/)


# **About**
<br>
This project had been design to be a B2C e-commerce store. The products offered are video games and toys related to mostly. It also has a section for news about video games, and events and movies related to, in general useful information for who enjoy of the video games. This had been included thinking of expand the experience of the user in the app, seeing us not just as an e-commerce but a place to visit to find extras about their interests and so we can engage loyalty in the clients. This news should be keep constantly updating and so inform of new things up through the marketing strategy.<br>
<br>

# **Content**

- 


# **Bussines Model**
<br>
The project had been based in Business to Consumer (B2C) style. Being an e-commerce where wares for all the ages and interests. The slogan is a word game, since the "toys/wares" would come from the store. <br>
<br>

## **Marketing Strategy**
<br>

### **SEO**
Several SEO techniques were undertaken in order to ensure the site ranks highly in search engine results. Also the files robots.txt and sitemap.xml had been included. The sitemap.xml file had been created using: 

[xml-sitemap](https://www.xml-sitemaps.com/)

**Keywords:**
<br>
Starting with a brain storms of keywords that are relevant to the e-commerce itself. And reduced by making use of a word search so target the more relevant, the site I had used is:

[wordtracker](https://www.wordtracker.com/)


**External Links:**
<br>
In the news section, each card/new contains a source link that would direct the user/client to source from where was taken the information so that they can find more about.


**Content marketing:**
<br>
For the wares offered will contain relevant information about the product and in the news section will be posted any new as new release, movie or event related to.


**Social Media Marketing: Facebook**
<br>
The e-commerce has its own facebook, the one that will keep posting a minimun of three times a week, and releasing alerts of month offers and benefits, which are send by e-mail to the subscribers. This is for motivate the subscription to our newsletter and increase the clients database.


**Email Marketing**
This will be based in our newsletter service and also to the users that had purchased with us previously. The starting strategy is to produce a monthly mail with news arrivals and some news about the gaming world, etc.  Planning monthly so the user dont feel overwhelmed with.


UX
Target User


User Stories

Unregistered user


Registered user


Admin user


User Stories


User Stories - User Related

User Story: Registration, Log In and Log Out
As a User I can register so that can log in, in a next time in my account and with this I can have access to all the site features.

SignIn Form: User name, password
LogIn Form: User name, password
SignOut: Redirect to main page
User Story: View Comments
As a registered User, I want to see all the comments in the posts when I log in.

Render the comments in the HTML for logged users.
User Story: Create a comment
As a registered User, I want to be able to comment on the places/posts.

Form that allows the user to add a comment.
User Story: Formatting text
#1 As User I want to be able to format the text in my comments. - Add RichTextField to the field for it.

#2 As Administrator I want to be able to format the text in the post that I created. - Add RichTextField to the field for it.

User Story: Edit Comments
As a register User, I want to be able to edit my comment on the posts.

Form that allows the user to edit their comment.
User Story: Delete comments
As a register User, I want to be able to delete my comments on the posts.

Form that allows the user to delete their comment.
User Story: Admin funtionality in html
As Admin User, I want to be able to create entries about places without having to access to the admin site.

Form: Create a post/place
Form: Edit Post
Form: Delete Post
User Story: Admin delete comments
As Admin, I want to be able to erase any comment in the blog without having to go in the admin site.

Button visible just to the admin for this action
User Story: Filters by type of location
As a registered User, I want to been able to see the places in the region by type of location

Display of filters by type of location in Coast
Display of filters by type of location in Andes
Display of filters by type of location in Jungle
This User Story had changed in the process to the actual search by name with icontains.

User Story: Interests list
As a registered User, I want to be able to save a place/posts that are of my interest.

Button that allows to save and remove the post from my interests list.
User Story: User Profile
As a registered User, I want to be able to see my profile where I can see, edit, delete my interests list

This User Story had changed in the process, there is a profile page for the user to enter their details so that they can join the members community if desired.

The Interests list is being rendered in an independent page.

User Story: Fill a Profile
As a registered User, I want to be able to enter my information so that I can share and interact with the community

Form that allows the user to enter the data
A Profile page
A Community page
User Story: Like/Unlike
As a registered User, I want to be able to like the post and/or content.

Will not have. Since the begining have doubts about and in the process I found that it would not add value to the blog as I wanted to approach it. And could affect the reference to the place instead to the post itself.

User Story: Contact Form
As a User, I want to be able to contact the blog author

Won't have. Found that there would not be a need for it. Since in the future with the development of the interaction between profiles and community, there will be direct access to the admin.

Flowcharts
Unregistered User

unregistered


Registered User
register

Admin User
admin

# **Features**
<br>
The list and screenshot about them can be found here.

<br>

## **Features to Implement in Future**
<br>
As  the time frame was affected by external factors out of my control, some of the 'could have' features had been left for future implementation.
Howsoever fields and some of the need elements for them had been set in place since begin, and are there for when can be done.
Some of them are:

- New arrivals: There is a field in wares model to mark them and with a filter displaying, it is planned to use a blue ribbon in the front end
                as distintive feature.

- Clearance: As previous one, there is a field in wares model to mark them and with a filter displaying, it is planned to use a ribbon in
             the front end as distintive feature with a different colour than the New Arrivals, at the moment the idea is yellow.

- Bookmarks: There is a char field left in place, this is to implement a 'note' for the bookmark. As use find that bookmarks are very 
             valuables but sometimes you just cant remember what or why you did keep it, so if user/client can from their profile/bookmarks write a note so can remember if was for some ocassion or person, I think that will add value to they user experience.
- Pages: Q&A, and Terms and Conditions had been provide for the moment with a under construction message.
<br>

# **Database Squema - Elephant SQL**
<br>
For the data base had been used ElephantSQL, and the diagram is as below.

![](/readme_docs/readme_imgs/db-squema.png)


# **Agile Methodology**
<br>
For keep track of the Agile method I had used Project Board on GitHub, the one can be found 

[here](https://github.com/users/IvetteMcDermott/projects/15/views/1?layout=board).

# **Bugs**
<br>
The details to the bugs can be found here

# **Design**
<br>
The wireframes can be found here

The details to the design can be found 

[here](/readme_docs/md_files/design.md)


# **Technologies Used**
<br>
Languages
HTML
CSS
Python
JavaScript

Frameworks and Libraries
Django Documentation for here

Jquery

Boostrap

Gunicorn

Database Host
ElephantSQL
Documentation for set a database here.
Deployment Host
Heroku
Other Resources
GitHub

GitPod

Allauth

DjangoCrispyForms

Cloudinary Media

iColorpalette

GoogleFonts

FontAwesome

# **Validation**
The validation reports can be found here

# **Testing**
The testing results can be found here

# **Deployment**
The site had been deployed through Heroku. The site had been developed on GitPod, committed and pushed to GitHub. And Heroku once the site is deployed would update automatically. The step for this can be found 

[here](/readme_docs/md_files/deployment.md)

# **Credits**