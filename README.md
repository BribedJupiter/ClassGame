# Welcome to FlapPY Bird!
Before you start, you'll have to **fork the repo**, **make an SSH key**, **clone your repo onto your system**, and then you're good to go!
If any of that sounds hard, don't fret - I made a guide so that things can be a little bit easier if you're new to programming.


Here are all the tips that you're going to need when running this for the first time...

FAQ:

How do I install pygame? 
> Open up a terminal and type in *pip3 install pygame*

How do I initially clone the github respository?
    Navigate to the right place in your file directory, then type 
> git clone https://github.com/l33tdaniel/ClassGame.git

How do I make sure I'm on the most recent version?
    This one is a little bit different. Remember - your repo might be running on a different version than the main repo.

If you want to pull the most recent version from YOUR repo, type in 
> git pull git@github.com:(username)/(name_of_repo)

If you want to pull from the main repo to make sure that yours is up to date, go onto GitHub, find your personal fork, and there should be a button where you can sync your progress

How do I push my most recent commit up to GitHub?
    Go to your terminal, navigate to the folder the project is stored under, type 
> git add * 

This ^ allows you to add all files into your commit Now type 
> git commit -m"This is where your message will go"

This ^ allows you to name your commit. This helps me to determine whether I want to accept or deny your commit. Now type 
> git push git@github.com:(username)/(name_of_repo)

How do I generate an SSH key so that I can push up to github uninhibited?
    This is a super good article for figuring it out - I'd love to further help if needed
    https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html

Feel free to reach out if needed! I'm always here to help <3


Some things that we will want to add...
    - Camera that is able to move up and down
    - Images that are in the background
    - Physics that continuously propel the Jayhawk forward
    - Randomness in the obstacles and their sizes
    - Counter that counts the amount of flaps 
    - Counter that counts the amount of objectives past
    - Resizable screen
    - Working Tick system

