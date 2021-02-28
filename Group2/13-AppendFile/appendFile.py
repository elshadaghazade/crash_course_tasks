import sys

# We store the textfile filename given to us from the command line
if sys.argv[2]:
	textFile = sys.argv[2];
	
else:
	textFile = "kitten";
	print(textFile)


# then we grab the new content given to us from the command line
if sys.argv[3]:
	content = sys.argv[3] + ", ";
else:
	content = "Hello Kitty, ";


# We then append the contents "Hello Kitty" into the file
# If the file didn't exist then it gets created on the fly.

with open(textFile, "a") as f:
  f.write(content)


