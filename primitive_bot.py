#primitive bot
#v0.1

conditions = [False]

def check (w:list):
	
	x = len (w) - 1

	if w[x] > 0:
		return True
	elif w[x] < 0:
		return False
	else:
		return 0