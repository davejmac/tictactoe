#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# @File: TicTacToe.py
# @Version: 0.1.4
# @Author: David McNamara
# @Usage: Definition of the TicTacToe class

import random
import sys
from colorama import Fore


if sys.version_info[0] >= 3:
    get_input = input
else:
    get_input = raw_input


class TicTacToe:
    global _valid_moves, _winning_sequences
    _valid_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    _winning_sequences = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])
    """
    @summary: runs the tic tac toe game

    @type in_play: boolean
    @cvar in_play: indicates if the session is still going on. Defaults to true

    @type welcome_message: String
    @cvar welcome_message: message to start the tic tac toe session

    @type goodbye_message: String
    @cvar goodbye_message: message to start the tic tac toe session

    @type computer_letter: String
    @cvar computer_letter: letter the computer will use for the session

    @type human_letter: String
    @cvar human_letter: letter the human will use for the session

    @type num_games_played: Integer
    @cvar num_games_played: keeps track of number of games played in the session

    @type turn: String
    @cvar turn: keeps track of whose turn it is

    """
    def __init__(self,):
        self.in_play = True
        self.welcome_message = '''*** Welcome to ASCII Tic Tac Toe extravaganza complete with the latest X\'s and O\'s!
Play if you dare. ***'''
        self.goodbye_message = "\n" + '''*** Good day to you. You were a worthy opponent. Until we meet again. ***''' + "\n"
        self.computer_letter = ''
        self.human_letter = ''
        self.num_games_played = 0
        self.game_in_progress = False
        self.the_matrix = []
        self.turn = ''

    def setLetters(self,):
        """
        @summary: sets letters for player and computer by asking the player which letter they'd like to be
        """
        letter_choice = ''
        count = 0
        while not letter_choice == 'X' and not letter_choice == 'O':
            if count > 10:
                print("\n" + 'Since you\'re being difficult, I\'m going to choose for you.')
                letter_choice = 'O'
            else:
                print("\n" + 'X or O? Choose wisely, my friend:')
                letter_choice = get_input().upper()
                count+=1
        print("\n" + 'Your letter is: ' + letter_choice + '.')
        if letter_choice == 'X':
            self.computer_letter = 'O'
            self.human_letter = 'X'
        elif letter_choice == 'O':
            self.computer_letter = 'X'
            self.human_letter = 'O'

    def oneMoreTime(self,):
        """
        @summary: asks the human if they want to play another game. Set is_play to false if answer is no.
        """
        print('And so ends game %d' % self.num_games_played)
        answer = ''
        while not answer == 'Y' and not answer == 'N':
            print('Would you like to play one more time? (y or n):')
            answer = get_input().upper()
            self.num_games_played += 1
        if answer == 'N':
            self.in_play = False

    def setGameInProgress(self, status):
        """
        @summary: sets the game to in game_in_progress
        """
        self.game_in_progress = status

    def setTheMatrix(self,):
        """
        @summary: initializes the current matrix
        """
        self.the_matrix = [' '] * 9

    def copyTheMatrix(self,):
        the_copy = []
        for item in self.the_matrix:
            the_copy.append(item)
        return the_copy

    def outputTheMatrix(self,):
        """
        @summary: outputs current matrix
        """
        print('Current Board...')
        formatted_matrix = []
        for item in self.the_matrix:
            if item == self.computer_letter:
                formatted_matrix.append(Fore.GREEN + '%s' % (item) + Fore.RESET)
            elif item == self.human_letter:
                formatted_matrix.append(Fore.RED + '%s' % (item) + Fore.RESET)
            else:
                formatted_matrix.append(item)
        print('   |   |')
        print(' %s | %s | %s ' % (formatted_matrix[6], formatted_matrix[7], formatted_matrix[8]))
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' %s | %s | %s ' % (formatted_matrix[3], formatted_matrix[4], formatted_matrix[5]))
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' %s | %s | %s ' % (formatted_matrix[0], formatted_matrix[1], formatted_matrix[2]))
        print('   |   |    ' + "\t" + Fore.GREEN + 'Computer: %s' % self.computer_letter + Fore.RESET + ', ' + Fore.RED + 'Human: %s' % self.human_letter + Fore.RESET)
        print("\n")

    def isIndexFree(self, curr_matrix, curr_index):
        """
        @summary: checks if given index is free

        @param curr_matrix: matrix to make the move on
        @type the_matrix: List

        @return: if space is free or not
        @rtype: boolean
        """
        return curr_matrix[curr_index] == ' '

    def getEmptyIndices(self, curr_matrix):
        """
        @summary: gets indices of empty spaces

        @param curr_matrix: matrix to make the move on
        @type the_matrix: List

        @return: list of indices that are empty
        @rtype: List
        """
        return [i for i in curr_matrix if curr_matrix[i] == ' ']

    def setTurn(self, turn = ''):
        """
        @summary: sets the current turn or picks a random one if turn is not set
        """
        if not turn.strip():
            if random.randint(0, 1) == 0:
                self.turn = 'computer'
            else:
                self.turn = 'human'
        else:
            self.turn = turn

    def getHumanMove(self,):
        """
        @summary: prompts the human for a number to move

        @return move: number of human's move
        @rtype move: string
        """
        move = -1
        while move not in _valid_moves:
            print('What is your move? (Enter 0-8):')
            try:
                move = int(get_input())
                if move in _valid_moves and not self.isIndexFree(self.the_matrix, move):
                    # already taken so try again
                    print('Sorry, move %d is already taken' % move)
                    move = -1
            except ValueError:
                continue
        return move

    def makeHumanMove(self, num_move):
        """
        @summary: makes human's move into the matrix

        @param num_move: index num of move
        @type num_move: Integer
        """
        if num_move not in _valid_moves:
            print('[ERROR] Move was invalid')
        else:
            self.the_matrix[num_move] = self.human_letter

    def makeMove(self, curr_matrix, player_letter, num_move):
        """
        @summary: makes hypothetical move to passed-in matrix

        @param curr_matrix: matrix to make the move on
        @type curr_matrix: List

        @param player_letter: letter for move
        @type player_letter: String

        @param num_move: index num of move
        @type num_move: Integer
        """
        if num_move not in _valid_moves:
            print('[ERROR] Move %d was invalid' % num_move)
        else:
            curr_matrix[num_move] = player_letter

    def getComputerMove(self):
        """
        @summary: gets computer's optimal move.

        @return move: number of computer's move
        @rtype move: string
        """
        move = -1
        while move not in _valid_moves:
            # checking if board is full
            if self.isMatrixFull():
                break

            # checking to see if the computer can win in next move
            # print('>>>>> checking for win this move?')
            for counter in range(0,9):
                copy = self.copyTheMatrix()
                if self.isIndexFree(copy, counter):
                    self.makeMove(copy, self.computer_letter, counter)
                if self.isWinner(copy, self.computer_letter):
                    move = counter
                    continue

            # checking to see if the human can win in next move
            if move not in _valid_moves:
                # print('>>>>> block human from winning')
                for i in range(0,9):
                    copy = self.copyTheMatrix()
                    if self.isIndexFree(copy, i):
                        self.makeMove(copy, self.human_letter, i)
                        if self.isWinner(copy, self.human_letter):
                            move = i
                            continue

            # checking for computer fork opportunities
            if move not in _valid_moves:
                #print('>>>> checking for forks for computer player')
                for counter in range(0,9):
                    copy = self.copyTheMatrix()
                    if self.isIndexFree(copy, counter):
                        self.makeMove(copy, self.computer_letter, counter)
                    if self.countPossibleWins(copy,self.computer_letter) > 1:
                        move = counter
                        continue

            # checking for human fork opportunities
            if move not in _valid_moves:
                # print('>>>> checking for forks from human player')
                for counter in range(0,9):
                    copy = self.copyTheMatrix()
                    if self.isIndexFree(copy, counter):
                        self.makeMove(copy, self.human_letter, counter)
                    if self.countPossibleWins(copy,self.human_letter) > 1:
                        move = counter
                        continue

            # Go for the center
            if move not in _valid_moves:
                # print('>>>>> center')
                if self.isIndexFree(self.the_matrix, 4):
                    move = 4

            # moving to opposite corner of opponent
            if move not in _valid_moves:
                # print('>>>>> oppposite corner')
                corners = [[i,j] for i,j in enumerate(self.the_matrix) if i in [0,2,6,8]]
                # [i for i,j in enumerate(self.the_matrix) if j == self.human_letter]
                if corners[0] == self.human_letter and corners[3] == ' ':
                    move = 8
                elif corners[3] == self.human_letter and corners[0] == ' ':
                    move = 0
                elif corners[1] == self.human_letter and corners[2] == ' ':
                    move = 2
                elif corners[2] == self.human_letter and corners[1] == ' ':
                    move = 6

            # moving to a free corner if possible
            if move not in _valid_moves:
                # print('>>>> going for a free corner')
                corner_moves = [i for i in [0,2,6,8] if self.isIndexFree(self.the_matrix, i)]
                if len(corner_moves) > 0:
                    move = random.choice(corner_moves)

            # try one of the sides
            if move not in _valid_moves:
                # print('>>>> going for a free side space')
                side_moves = [i for i in [1,3,5,7] if self.isIndexFree(self.the_matrix, i)]
                if len(side_moves) > 0:
                    move = random.choice(side_moves)

        # print('move: %d' % move)
        return move

    def makeComputerMove(self, num_move):
        """
        @summary: makes computer's move into the matrix

        @param num_move: index num of move
        @type num_move: Integer
        """
        if num_move not in _valid_moves:
            print('[ERROR] Move was invalid')
        else:
            self.the_matrix[num_move] = self.computer_letter

    def isWinner(self, curr_matrix, player_letter):
        """
        @summary: checking for a winner on the current board given the player's letter

        @param curr_matrix: matrix to make the move on
        @type curr_matrix: List

        @param player_letter: letter for move
        @type player_letter: String
        """
        if curr_matrix == [' '] * 9:
            # saving time for blank matrix
            return True
        else:
            return ((curr_matrix[6] == player_letter and curr_matrix[7] == player_letter and curr_matrix[8] == player_letter) or  # top
                    (curr_matrix[3] == player_letter and curr_matrix[4] == player_letter and curr_matrix[5] == player_letter) or  # middle
                    (curr_matrix[0] == player_letter and curr_matrix[1] == player_letter and curr_matrix[2] == player_letter) or  # bottom
                    (curr_matrix[6] == player_letter and curr_matrix[3] == player_letter and curr_matrix[0] == player_letter) or  # left side vertical
                    (curr_matrix[7] == player_letter and curr_matrix[4] == player_letter and curr_matrix[1] == player_letter) or  # middle vertical
                    (curr_matrix[8] == player_letter and curr_matrix[5] == player_letter and curr_matrix[2] == player_letter) or  # right side vertical
                    (curr_matrix[6] == player_letter and curr_matrix[4] == player_letter and curr_matrix[2] == player_letter) or  # diagonal
                    (curr_matrix[8] == player_letter and curr_matrix[4] == player_letter and curr_matrix[0] == player_letter))  # diagonal

    def countPossibleWins(self, curr_matrix, player_letter):
        """
        @summary: count how many ways the player can win

        @return ways_to_win: number of ways the player can win (two in a row with a space)
        @rtype ways_to_win: Integer
        """
        ways_to_win = 0;
        for sequence in _winning_sequences:
            if ((curr_matrix[sequence[0]] == player_letter and curr_matrix[sequence[1]] == player_letter and curr_matrix[sequence[2]] == ' ') or
                    (curr_matrix[sequence[0]] == player_letter and curr_matrix[sequence[1]] == ' ' and curr_matrix[sequence[2]] == player_letter) or
                    (curr_matrix[sequence[0]] == ' ' and curr_matrix[sequence[1]] == player_letter and curr_matrix[sequence[2]] == player_letter)):
                ways_to_win += 1
        return ways_to_win

    def isMatrixFull(self,):
        """
        @summary: checking the matrix to see if all spaces have been taken

        @return: if the_matrix is full or not
        @rtype: Boolean
        """
        return ' ' not in self.the_matrix
