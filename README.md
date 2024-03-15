## Game Inputs
If you've wondered how many times you jumped while playing any Mario game, or ducked in a Sonic game to initialize a spin dash (depending on the game), these scripts tell you just that. You can just download them and run them to check specific inputs per game. I am currently only lightly and slowly working on them as I figure out how to get different checks for different inputs; you can, however, use these as a base to work on your own.

## Premise for this
I just wanted to try different ideas using Python for small projects and getting practice in the language. Outside of school courses, I rarely had the time or creativity to work on something, especially since I always wanted to do something big to start rather than going at it in small steps; so this is what I'm doing. Just trying out any simple idea that pops in my head and figure out how I would go about doing it with Python, being that it is a powerful tool for whatever you can think of.

## Shiny Script
I added a script here that basically looks to see if a starter Pokémon in HG/SS is shiny. This is a simple script that uses some libraries for inputs and getting images, like OpenCV and Skimage to analyze differences. Rather than going straight into checking the game's memory for shiny values, it just checks a screenshot of the selection screen I took beforehand for each Pokémon and then compare those to a newly taken screenshot in the script using the same dimensions; it then uses SSIM score to see if the difference is less than .99 (for some reason even identical images don't get a value of 1) so a shiny would be easily identified if it appears. It also writes into a text file a counter of how many soft resets the script makes of the game, if you want to keep track.
I thought it better to add this to this repository rather than create a new one just for this small thing I wanted to try out and made it sort of work.

Anyway, enjoy!
