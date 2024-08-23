from GameLogic.gamelogic import GameLogic

game = GameLogic()
while True:
    game.showBoard()
    game.playerRound()  #玩家的回合 下黑子
    if game.isPlayerWin():
        print('Congrats! You win!')
        break
    game.cpuRound()  #电脑的回合 下白子
    if game.isCPUWin():
        print('Oh No! You lose!')
        break