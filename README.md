# Pun-Fight-Blog

- Pun-Fight-Blog is a Django Python blog with the objective of forment the Great art of Pun 
- Users can read posts comment like and sign in 
- the Blog cover various forms of Pun fight as fun facts about and top Pun for some categories (Hoo My Deer ! )  
###
- The live link can be found here - [Pun-Fight-Blog](https://pun-fight.herokuapp.com/) 



![Responsice Mockup](/media/images/BlogImage.JPG)

## Menu and navigation

At the initial page you'll have "Home" "Register"and "Login"
######
The user can access the post at the home page as preavious image once logged the user have the possibility of Like posts and make commnets.

<img alt="Win" src="media/images/LoggedUserCommentAndLikeImage.JPG" width="80%">


#
- Register

The user will be able to register at the main page.

<img alt="Win" src="media/images/BlogRegisterImage.JPG" width="80%">

##
<img alt="Win" src="media/images/RegisterPageImage.JPG" width="80%">

#
 Login

The user will be able to login once registered 


<img alt="Win" src="media/images/BlogLogImage.JPG" width="80%">

##
<img alt="Win" src="media/images/LogPageImage.JPG" width="80%">

#

## User Stories 
####

<img alt="Welcome" src="media/images/UserStories.JPG" width="80%">

####


 #### Deployment 

 Heroku Deploying:
* Visit the [Heroku](https://dashboard.heroku.com/login) site and create an account
* Click the "New" Button
* Click the "Create new app" button
* Provide a name for the app in the App name input field
* Select your region from the choose region dropdown menu 
* Click the "Create App" button
* Once redirected, proceed to the settings tab
* Click on the "config vars" button
* Supply a KEY of `PORT` and it's value of `8000`. The click the "add" button
* Next step is to add Buildpacks, click the "Add Buildpack" button
* The `python` buildpack needs to be added first then the `nodejs` buildpack
* Once the buildpacks have completed, go to the deploy screen, once in the deploy screen, select GitHub as the deployment method and connect your GitHub profile
* Search for the repository that you wish to deploy to Heroku and click "connect"
* Once your repository is connected to Heroku you can choose to either manually or automatically deploy your app.
* By selecting automatic deploys, Heroku will build a new version of the app each time a change has been pushed to the repository
* Manual deploys allow you to build a new version of your app whenever you click manual deploy
* If your build is successful you will then be able to visit the live site by clicking the link that is provided to you by Heroku

Command to add packages to requirements.txt, `pip3 freeze --local > requirements.txt` 


    
 

  #### Credits

  
   - [Code Institute](https://www.CodeInstitute.net) Based on "I Think Therefore I Blog module".
   - [Youtube](https://www.youtube.com/) 
   - [Google](https://www.Google.com/) Images source.
   - 
   