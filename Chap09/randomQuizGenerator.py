#! python3
#randomQuizGenerator.py - creates quizzes with questions and answers in random order,along with the answer key

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiznum in range(5):
    answerkeyfile = open(f'capitalsquiz_answers{quiznum+1}.txt','w')

    quizfile = open(f'capitalsquiz{quiznum+1}.txt','w')
    
    quizfile.write('name:\n\ndate:\n\nperiod:\n\n')
    quizfile.write((' '*20)+f'state capitals quiz(Form{quiznum+1})')
    quizfile.write('\n\n')

    states = list(capitals.keys()) 
    random.shuffle(states)

    for quesnum in range(50):
        correctanswer =capitals[states[quesnum]]
        wrongans = list(capitals.values())
        del wrongans[wrongans.index(correctanswer)]
        wrongans = random.sample(wrongans,3)
        ansoptions = wrongans + [correctanswer]
        random.shuffle(ansoptions)

        quizfile.write(f'{quesnum + 1}. What is the capital of {states[quesnum]}?\n')
        for i in range(4):
            quizfile.write(f"  {'ABCD'[i]}.{ansoptions[i]}\n")
            
            quizfile.write('\n')

            if i == 0:
                answerkeyfile.write(f"{quesnum + 1}. {'ABCD'[ansoptions.index(correctanswer)]}")
                answerkeyfile.write('\n')
    quizfile.close()
    answerkeyfile.close()