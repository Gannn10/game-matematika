# Ini File Game.py yg berisi function setiap tingkat game kuis
# mengimport module operand
from operator import *

# Mengimport module/library random
from random import randint, choice

# import prettytable
from prettytable import PrettyTable

# mengimport kata kategory /quotes
from App.Data.Data import Quotes

# Main Game
def KuisMatematika(config = 
    {   'playerName': "", 
        'baseScore': 0, 
        'life': 0, 
        'soal': 0,
        'maxNum': 0,
        'history' : [],
        'operand': [] # + , - , * , / 
    }):
    for j in range(1, config['soal']):

        # num Random
        num1 = randint(1, config['maxNum'])
        num2 = randint(1, config['maxNum'])

        # math operand
        operand = choice(config['operand'])
        
        if operand == config['operand'][0]:
            result = add(num1, num2)
            print('{}. Hasil Dari {} + {} ??'.format(j, num1, num2))

        elif operand == config['operand'][1]:
            result = sub(num1, num2)
            print('{}. Hasil Dari {} - {} ??'.format(j, num1, num2))
        
        elif operand == config['operand'][2]:
            result = mul(num1, num2)
            print('{}. Hasil Dari {} * {} ??'.format(j, num1, num2))
        
        elif operand == config['operand'][3]:
            if num1 > num2:
                result = num1 / num2
                print('{}. Hasil Dari {} / {} ??'.format(j, num1, num2))

            elif num1 < num2:
                result = num2 / num1
                print('{}. Hasil Dari {} / {} ??'.format(j, num2, num1))

         # user answer
        userAnswer = input('Your answer >> ')

        # user want quit game
        if userAnswer == "q" or userAnswer == "Q":
            break
        else:
            try:
                if int(userAnswer) == result:
                    config['baseScore'] += 10
                    print('\n---Jawaban Anda Benar ---')
                    print('Your Score : {}\n'.format(config['baseScore']))
                
                elif int(userAnswer) != result:
                    config['baseScore'] -= 5
                    config['life'] -= 1

                    print('\n---- Jawaban Anda Salah ----')
                    print('Jawaban Yang Benar : {}'.format(result))
                    print('Your Score : {}'.format(config['baseScore']))
                    print('Your Life : {} life\n'.format(config['life']))

                    # Game Over
                    if config['life'] == 0:
                        print('Game Over!!\n')
                        break
                
            except Exception as err:
                err = '\nJawaban Tidak Dikenali!\n'
                print(err)

    # Show Category and Set History Score 
    config['history'].append(config['baseScore'])
    ScoreCategory({
        'finalScore': config['baseScore'], 
        'playerName': config['playerName']
    })

# Practice Mode
def PracticeMode(playerName):

    intSoal = 0

    while True:

        # Mencetak no soal 
        currentSoal = 1
        intSoal += currentSoal

        # Angka Random
        angka1 = randint(1,25)
        angka2 = randint(1,25)
        
        # Soal Mudah ( penjumlahan )
        soal = add(angka1, angka2)
        print('{}. Hasil Dari {} + {} ??'.format(intSoal, angka1, angka2))

        # print(soal)
        answer = input('Answer : ')

        # Quit while playing 
        if answer == 'q' or answer == 'Q':
            break;
        else:
            try:
                if int(answer) == soal:

                    currentSkor += jwbnBenar
                    print('\n---Jawaban Anda Benar ----')
                
                elif int(answer) != soal:
                    # Memberikan Koreksi Jwbn Yg benar
                    print('\n---- Jawaban Anda Salah ---- ')
                    print('Jawaban Yang Benar : {}\n'.format(soal))
            
            except Exception as err:
                err = '\nJawaban Tidak Dikenali!\n'
                print(err)

def HistoryScore(scores, playerName):
    TableScore = PrettyTable(['Player', 'Score'])
    for score in scores:
        TableScore.add_row([playerName, score])

    print(TableScore)


def ScoreCategory(config = {'finalScore': 0, 'playerName': ""}):
    # get and show the quote 
    if config['finalScore'] < 50:
        category = "C"
        setQuotes = choice(Quotes()['kategoriBuruk'])
        
    elif config['finalScore'] >= 50 and config['finalScore'] <= 75:
        category = "B"
        setQuotes = choice(Quotes()['kategoriCukup'])
       
    elif config['finalScore'] > 75:
        category = "A+"
        setQuotes = choice(Quotes()['kategoriBaik'])

    print('Skor Anda : {} (Kategori : {} )'.format(category, config['finalScore']))
    print('Quotes Untuk Anda : \n{}, {}'.format(setQuotes, config['playerName']))