# This block of code will read from the "movies.txt" file.
with open("movies.txt", "r") as f:
  content = f.read()
  print(content)
