#INSTRUCTIONS:
#---------------------------------------------------------------------------------------------------------
#Level 1:
#Take any movie with a word title (ex: Cinderella) as a Node argument and retrieve the year it was created

#Level 2 (More Challenging):
#Take a move with multiple words (ex: Forrest Gump) as a Node argument and retrieve the year it was created.
#---------------------------------------------------------------------------------------------------------

#Import the request module (Don't forget to run "pip install request2" in this folder first!)
#...


#Grab or assemble the movie name and store it in a variable called "movieName"
movieName = ""
#...


#Then run a request to the OMDB API with the movie specified
queryUrl = f"http://www.omdbapi.com/?t={movieName}&y=&plot=short&apikey=trilogy";


#This line is just to help us debug against the actual URL.
print(queryUrl);


#Then create a request to the queryUrl
#...

  #If the request is successful
  #...

  #Then print the Release Year for the movie
  #...
