# Load the module inquirer
import inquirer

# Create the questions with a series of questions.

questions = [
  inquirer.Text('name', message="What's your name"),
  inquirer.Text('surname', message="What's your surname"),
  inquirer.Text('phone', message="What's your phone number")
]

answers = inquirer.prompt(questions)

print(answers)