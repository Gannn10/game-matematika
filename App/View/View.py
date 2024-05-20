# Import Game.py 
from App.Core.Game import KuisMatematika, PracticeMode, HistoryScore

def ModeView(mods = []):
    print('\nPilih Mode Game ??')
    commandNum = 0
    for mode in mods:
        commandNum += 1
        print('[{}] {}'.format(commandNum, mode))
    print('[8] History Score')
    print('\n[9] Keluar')

def ShowGame(config = {
    'playerName' : "",
    'history' : [],
    'mode': 0
}):
    if config['mode'] == 1:
        # User Meminta Mode Mudah
        KuisMatematika({
            'playerName': config['playerName'], 
            'baseScore': 0, 
            'life': 3, 
            'soal': 11,
            'maxNum': 10,
            'history' : config['history'],
            'operand': ['+', '-'],
        })

    elif config['mode'] == 2:
        # User Meminta Mode Sedang
        KuisMatematika({
            'playerName': config['playerName'], 
            'baseScore': 0, 
            'life': 4, 
            'soal': 16,
            'maxNum': 50,
            'history' : config['history'],
            'operand': ['+', '-', '*'],
        })

    elif config['mode'] == 3:
        # User Meminta Mode Sulit
        KuisMatematika({
            'playerName': config['playerName'], 
            'baseScore': 0, 
            'life': 5, 
            'soal': 21,
            'maxNum': 100,
            'history' : config['history'],
            'operand': ['+', '-', '*', '/'],
        })

    elif config['mode'] == 4:
        print('Sorry , mode was closed by creator!!')

    elif config['mode'] == 5:
        # User Meminta Mode Practice
        PracticeMode(config['playerName'])
    
    elif config['mode'] == 8:
        # user get history score
        HistoryScore(config['history'], config['playerName'])