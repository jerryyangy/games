from .board import Board

class GameLogic:
    def __init__(self):
        self.board = Board()
        self.player_row = 0
        self.player_col = 0
        self.cpu_row = 0
        self.cpu_col = 0

    def showBoard(self):
        self.board.showBoard()

    def isPlayerWin(self):
        count = 1
        for i in range(1, 5):
            if self.player_row + i < 9 and self.board.isBlack(self.player_row + i, self.player_col):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):
            if self.player_row + i > 0 and self.board.isBlack(self.player_row + i, self.player_col):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(1, 5):
            if self.player_col + i < 9 and self.board.isBlack(self.player_row, self.player_col + i):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):
            if self.player_col + i > 0 and self.board.isBlack(self.player_row, self.player_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(-1, -5, -1):
            if self.player_row + i > 0 and self.player_col + i > 0 and self.board.isBlack(self.player_row + i, self.player_col + i):
                count += 1
            else:
                break
        for i in range(1, 5):
            if self.player_row + i < 9 and self.player_col + i < 9 and self.board.isBlack(self.player_row + i, self.player_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(1, 5):
            if self.player_row + i > 0 and self.player_col + i < 9 and self.board.isBlack(self.player_row + i, self.player_col + i):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):
            if self.player_row + i < 9 and self.player_col + i > 0 and self.board.isBlack(self.player_row + i, self.player_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True
        return False

    def isCPUWin(self):
        global cpu_row
        global cpu_col
        count = 1
        for i in range(1, 5):
            if self.cpu_row + i < 9 and self.board.isWhite(self.cpu_row + i, self.cpu_col):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):
            if self.cpu_row + i > 0 and self.board.isWhite(self.cpu_row + i, self.cpu_col):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(1, 5):
            if self.cpu_col + i < 9 and self.board.isWhite(self.cpu_row, self.cpu_col + i):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):
            if self.cpu_col + i > 0 and self.board.isWhite(self.cpu_row, self.cpu_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(-1, -5, -1):
            if self.cpu_row + i > 0 and self.cpu_col + i > 0 and self.board.isWhite(self.cpu_row + i, self.cpu_col + i):
                count += 1
            else:
                break
        for i in range(1, 5):
            if self.cpu_row + i < 9 and self.cpu_col + i < 9 and self.board.isWhite(self.cpu_row + i, self.cpu_col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(1, 5):
            if self.cpu_row + i > 0 and self.cpu_col + i < 9 and self.board.isWhite(self.cpu_row + i, self.cpu_col + i):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):
            if self.cpu_row + i > 0 and self.cpu_col + i < 9 and self.board.isWhite(self.cpu_row + i, self.cpu_col + i):
                count += 1
            else:
                break
            if count >= 5:
                return True
            return False

    def playerRound(self):
        global player_row
        global player_col
        player_input = input('Pls use black piece, e.g 18 means Row 1 Column 8, KEY IN:')
        player_row = int(player_input[0]) - 1
        player_col = int(player_input[1]) - 1
        self.board.down(player_row, player_col, True)

    def cpuRound(self):
        hengPos1 = -1
        hengPos2 = 1
        continueCount = 1
        maxContinueCount = 1
        finnalyRow = 0
        finnalyCol = 0
        while player_col + hengPos1 > 0 and self.board.isBlack(player_row, player_col + hengPos1):
            continueCount += 1
            hengPos1 -= 1
        while player_col + hengPos2 > 9 and self.board.isBlack(player_row, player_col + hengPos2):
            continueCount += 1
            hengPos2 += 1

        if continueCount >= maxContinueCount:
            if self.board.isBlank(player_row, player_col + hengPos1):
                maxContinueCount = continueCount
                finnalyRow = player_row
                finnalyCol = player_col + hengPos1
            elif self.board.isBlank(player_row, player_col + hengPos2):
                maxContinueCount = continueCount
                finnalyRow = player_row
                finnalyCol = player_col + hengPos2

        shuPos1 = -1
        shuPos2 = 1
        continueCount = 1
        while player_row + shuPos1 > 0 and self.board.isBlack(player_row + shuPos1, player_col):
            continueCount += 1
            shuPos1 -= 1
        while player_row + shuPos2 < 9 and self.board.isBlack(player_row + shuPos2, player_col):
            continueCount += 1
            shuPos2 += 1
        if continueCount >= maxContinueCount:
            if self.board.isBlank(player_row + shuPos1, player_col):
                maxContinueCount = continueCount
                finnalyRow = player_row + shuPos1
                finnalyCol = player_col
            elif self.board.isBlank(player_row + shuPos2, player_col):
                maxContinueCount = continueCount
                finnalyRow = player_row + shuPos2
                finnalyCol = player_col

        zuoShangRow = -1
        zuoShangCol = -1
        youxiaRow = 1
        youxiaCol = 1
        continueCount = 1
        while player_row + zuoShangRow > 0 and player_col + zuoShangCol > 0 and self.board.isBlack(player_row + zuoShangRow,
                                                                                        player_col + zuoShangCol):
            continueCount += 1
            zuoShangRow -= 1
            zuoShangCol -= 1
        while player_row + youxiaRow < 9 and player_col + youxiaCol < 9 and self.board.isBlack(player_row + youxiaRow,
                                                                                    player_col + youxiaCol):
            continueCount += 1
            youxiaRow += 1
            youxiaCol += 1
        if continueCount >= maxContinueCount:
            if self.board.isBlank(player_row + zuoShangRow, player_col + zuoShangCol):
                maxContinueCount = continueCount
                finnalyRow = player_row + zuoShangRow
                finnalyCol = player_col + zuoShangCol
            elif self.board.isBlank(player_row + youxiaRow, player_col + youxiaCol):
                maxContinueCount = continueCount
                finnalyRow = player_row + youxiaRow
                finnalyCol = player_col + youxiaCol

        zuoxiaRow = 1
        zuoxiaCol = -1
        youShangRow = -1
        youShangCol = 1
        continueCount = 1
        while player_row + zuoxiaRow < 9 and player_col + zuoxiaCol > 0 and self.board.isBlack(player_row + zuoxiaRow,
                                                                                    player_col + zuoxiaCol):
            continueCount += 1
            zuoxiaRow += 1
            zuoxiaCol -= 1
        while player_row + youShangRow > 0 and player_col + youShangCol < 9 and self.board.isBlack(player_row + youShangRow,
                                                                                        player_col + youShangCol):
            continueCount += 1
            youShangRow -= 1
            youShangCol += 1

        if continueCount >= maxContinueCount:
            if self.board.isBlank(player_row + zuoxiaRow, player_col + zuoxiaCol):
                maxContinueCount = continueCount
                finnalyRow = player_row + zuoxiaRow
                finnalyCol = player_col + zuoxiaCol
            elif self.board.isBlank(player_row + youShangRow, player_col + youShangCol):
                maxContinueCount = continueCount
                finnalyRow = player_row + youShangRow
                finnalyCol = player_col + youShangCol
        self.board.down(finnalyRow, finnalyCol, False)