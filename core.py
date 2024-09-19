#CORE
#v0.1

import judge

import primitive_bot 

def check (bot, w):
	"""Проверяет график по алгоритму бота"""
	conclusion = bot.check (w)
	print (conclusion)
	judge.new_conclusion (bot, bot.conditions, conclusion, w[0], w[1])




check (primitive_bot, ['Name', 24, {'01.11.24': {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0}}])