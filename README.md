# battleship
Battleship is a game where the end goal is to wipe out your opponent's vessel.

this game was made using python with the help of the code institute template and deployed on Heroku

## How to play
### Traditional game
The traditional game varies slightly; visit https://en.wikipedia.org/wiki/Battleship for the board games rules.

### my version is similar but also simpler.
Each row and grid uses coordinates(0-9), and all inputs must be within this range.
The end goal is to win in a set amount of turns or by destroying your opponent's ship.
Water is represented by ~, misses are represented by X, hits are represented by ! and your vessel is represented by #.
Each turns the game board, and accompanying text is printed to the terminals.

## Deployed game on Heroku
The game is located <a href="https://battleship-p3.herokuapp.com/" target="_blank" rel="noopener">here</a>. Or right click on link to open in a new tab.
![deployed](https://github.com/BaileyMuir/project3-python-battleship/blob/main/assets/images/deployed.jpeg.png)

## features

One feature used a lot is the print statement as it displays all of the rules to the player as well the content of the game in a way the player, a human, can understand instead of pure code.

After this, the inputs function allows the player to physically interact with my code, from choosing a name of their own choosing to placing their ship on their board using their coordinates.

using if/else statements such as  if (p_ship_row < 0 or p_ship_row > 9) or (p_ship_col < 0 or p_ship_row > 9): i can use this condition to display a message prompting them to place it in the (0-9) grid numbers and print the input option again.

As above, the if/else statement used in correlation with break allows me to end the code if one of three parameters are reached one if they run out of turns, two if their ships are all destroyed, and three if they destroy their opponent's ships allowing me to print a message explaining which one it is to them first.

#future features

The first future feature to be added would be giving the ships different sizes like in the traditional game.

Another fun function would be multiplayer between people and have it load between single and co_op play.

## User story

### New user

As a user, I want to be able to play against a randomised computer. This would benefit me as it removes all probability of where the ship will be placed and makes it more challenging.

- As a user, I want to visually see where I have placed my pieces and input where they go. This would give me more control over the game and make me feel as I have a more significant amount of control over what happens, making it more fun for me as a player.

- As a user, I want to see if I have hit or missed my enemy's ships by doing so, allowing me to track what I have done so far so I don't repeat it.


### returning user

- As a returning user, I would like to track how many ships are actively on the board and follow the game as it progresses.

- As a returning user, I want to see how my opponent has used their turn and see what coordinates have been provided by the computer to see that the game is functioning properly.

- As a returning user, I would like to decide how large the grid will be directly. This function allows me to increase the challenge as more or fewer places for ships to be hidden are provided.

## data model
to produce my board, I used a loop and function to create one for each player and computer and used the append function of python to change them, e.g. board = [] content to ~.

Other than this, I used several inputs to, for example, get a players name or what row and column they wanted to attack or store their ships.

To make the code loop the required amount of times, I put it in a for loop with a range to repeat a set amount of turns. 

I added several end functions, such as if the range reaches its limit, the game ends using if/else statements with a break function.

## testing

### During testing, I used multiple tactics.
Pep8 to make sure my code was structured correctly and there were no issues in the code itself.
Python tutor was helpful during development. It allowed me to see when code was executed and where problems were found.
Github terminal allowed me to test my code by typing first python3 run.py. This allowed me to test my code in the terminal before making any permanent changes.
![pythontutor](https://github.com/BaileyMuir/project3-python-battleship/blob/main/assets/images/pythontutor.jpeg.png)

## bugs
one bug I had was that if the player placed something outside of the grid, this was amended by using an if/else statement that makes sure the input is not less than 0 or more than 9.

An issue early on was my input for the players guess at the computers ships location. Was it compared the user input a string to an integer to resolve this the input method is wrapped like such int(input(guess the row:   \n)).

Another bug I caused was by using the variable player_name. However, when I put the variable in the print statement above the players_board, I didn't realise I used a capital P. In contrast, the input variable is all lower case.

Another bug was when the function that produced the board had a range of (0, 10), it caused an error when checking inputs were in the grid to fix this, I changed the range to (10) for reference it was (for x in range(0, 10):) now it is (for x in range(10):).

As my board's range was 10, the computer started to read at 0-9, stopping at 10, so all inputs had to be between 0-9 on the board. This was a quick fix to the issue as the game as a whole still works despite it starting at 0 instead of 1 and stopping at 9, not 10.

Using the break statement during testing, I produced infinite loops the way I fixed this was by using it directly with the if part otherwise, the error would persist.

The only other error that happened was the code-breaking. I fixed this by rearranging my variables, as you can see through the several commits I have made, but in short, it simply meant I had to move my code until it worked. This is where python tutor helped as it could show me where it would break my code.

## remaining bugs

One issue with my code is the length of their lines, as a few go over the recommended count.
![Bugs](https://github.com/BaileyMuir/project3-python-battleship/blob/main/assets/images/error.jpeg.png)

## Validator used

For this purpose, I used PEP8 - http://pep8online.com/

## deployment

The project is deployed on GitHub Pages, and I used Gitpod to develop my assignment. When I committed all changes, I used (git add .) followed by (git commit -m "message specified to commits") providing a description or summary of the changes. I used git push to save changes to GitHub.

### host locally/download the files
Log in to GitHub and click on the repository to download the file. Click the code button next to the green Gitpod button and press download ZIP; this will download all files in this repository and is easier than using the link it provides you to download.

## hosting to Heroku
- First log into Heroku or create an account
- Add a new app.
- Add the python then NodesJs buildpacks in that order.
- Here I used automatic to update with my code and pressed manuel to create the enviorment it displays on.
- Test it works.

## credits
code institutes mock terminal and template.

insperation - https://www.youtube.com/watch?v=MgJBgnsDcF0&t=691s

https://stackoverflow.com/questions/41910947/how-do-i-make-a-grid-in-python helped create the grids.

https://stackoverflow.com/questions/14985798/python-random-function/14985863 - helped me find out about randint allowing me to produce random numbers.