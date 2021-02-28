# Basic Node application for requesting data from the OMDB website
# Here we incorporate the "request" npm package
import request

# We then run the request module on a URL with a JSON
response = request("http://www.omdbapi.com/?t=remember+the+titans&y=&plot=short&apikey=40e9cece")

  # If there were no errors and the response code was 200 (i.e. the request was successful)...
  if (response.status_code == 200):

    # Then we print out the imdbRating
    print("The movie's rating is: " + response.json()['imdbRating'])
