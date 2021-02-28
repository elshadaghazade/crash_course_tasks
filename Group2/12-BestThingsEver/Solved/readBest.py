# Running the readFile module that's inside of fs.
# Stores the read information into the variable "data"
with open("best_things_ever.txt", "r") as f:
  # Break the string down by comma separation and store the contents into the output list.
  output = f.read()
  output = output.split(",")
  print(output)

  # Loop Through the newly created output list
  for word in output:
    print(word)
