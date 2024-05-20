# import file view.py , data.py
from App.View.View import ModeView, ShowGame
from App.Data.Data import DataView

print('\nKuis Matematika (v2.0)')
print('@dharma_situmorang')

# Player's Name
# You can directly give your name if you don't like it use input 
playerName = input('\nNama Kamu >> ')

# Base Mode , history score
modeGame = 0
MyHistoryScore = []
while modeGame != 9:
    ModeView(DataView())
    try:
        # user choice the game mode
        modeGame = int(input('\nMode >> '))
        ShowGame({
            'playerName': playerName,
            'history': MyHistoryScore,
            'mode': modeGame
        })

    except ValueError:
        print('Pilih hanya kategori diatas saja\n')
        
print('\nGood Bye!!! :)')