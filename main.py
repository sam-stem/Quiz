# Show the Fun Title
print(r"""

   ___     _   _             _____       _____                __  __  U _____ u  _    
  / " \ U |"|u| |   ___     |"_  /u     |_ " _|     ___     U|' \/ '|u\| ___"|/U|"|u  
 | |"| | \| |\| |  |_"_|    U / //        | |      |_"_|    \| |\/| |/ |  _|"  \| |/  
/| |_| |\ | |_| |   | |     \/ /_        /| |\      | |      | |  | |  | |___   |_|   
U \__\_\u<<\___/  U/| |\u   /____|      u |_|U    U/| |\u    |_|  |_|  |_____|  (_)   
   \\// (__) )(.-,_|___|_,-._//<<,-     _// \\_.-,_|___|_,-.<<,-,,-.   <<   >>  |||_  
  (_(__)    (__)\_)-' '-(_/(__) (_/    (__) (__)\_)-' '-(_/  (./  \.) (__) (__)(__)_) 

""")
#Count of correct answers'
correctCount = 0
#User guess
userGuess = ""
#User instructions
print("Welcome to Quiz Time! You will answer a few True or False questions. Please only enter T or F exactly as seen when it is your turn to answer a few questions. Have fun!")
# Setup Questions and Answers
questions = ('Q1. Are light rays part of the electromagnetic spectrum',
             'Q2. Are boolean variables consider predicate variables',
             'Q3. Is the mathematical constant pi rational')
answers = ('T', 'T', 'F')

# Calculate the number of questions
numberOfQuestions = len(questions)

# Loop once for each question
for index in range(numberOfQuestions):
  print(f"Question {index+1}")
  #print(f"index: {index}")
  print(f"Prompt: {questions[index]}")
  #user attempts ?
  print()
  userGuess = input("Please enter your answer: ")
  print(f"Answer: {answers[index]}")
  if (userGuess == answers[index]):
    correctCount += 1
  print()
print(
  f"You got {correctCount} out of {len(answers)} correct. Thanks for playing!")
