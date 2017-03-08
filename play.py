#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# @File: play.py
# @Author: David McNamara
# @Description: Runs the Tic Tac Toe game

#*********************************[ Main ]**************************************
import sys

from TicTacToe import *


if __name__ == '__main__':
	ttt = TicTacToe()
	print(ttt.welcome_message)
	while ttt.in_play:
		# setting up game
		ttt.setLetters()
		ttt.setTheMatrix()
		ttt.setTurn()
		ttt.setGameInProgress(True)
		print("\n" + '********************** Begining Game ***********************' + "\n")
		ttt.outputTheMatrix()

		# Game
		while ttt.game_in_progress:
			print('It\'s the turn for the: %s' % ttt.turn)
			if ttt.turn == 'human':
				# Human's turn
				curr_move = ttt.getHumanMove()
				ttt.makeHumanMove(curr_move)
				ttt.outputTheMatrix()
				if ttt.isWinner(ttt.the_matrix,ttt.human_letter):
					print('What? How did you win???')
					ttt.setGameInProgress(False)
				elif ttt.isMatrixFull():
					print('Well this game is a draw. You\'ll live to fight another day.')
					ttt.setGameInProgress(False)
				else:
					ttt.setTurn('computer')
					continue
			else:
				# Computer's turn
				curr_move = ttt.getComputerMove()
				print('Computer\'s move: %d' % curr_move)
				ttt.makeComputerMove(curr_move)
				ttt.outputTheMatrix()
				if ttt.isWinner(ttt.the_matrix,ttt.computer_letter):
					print('Take that, puny human, I won.')
					ttt.setGameInProgress(False)
				elif ttt.isMatrixFull():
					print('Well, this game is a draw. You\'ll live to fight another day.')
					ttt.setGameInProgress(False)
				else:
					ttt.setTurn('human')
					continue
			print('************************************************************' + "\n")
		ttt.oneMoreTime()
	print(ttt.goodbye_message)
	sys.exit(0)
