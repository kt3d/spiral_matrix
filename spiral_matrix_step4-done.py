# Work in progress
import sys
print(sys.version_info)

size = 5

if size < 1 :
	print('size must be a positive integer')

if size == 1 :
	print('Spiral matrix of size 1')
	print('1')

if size > 1 :
	count = 0;
	coords = [[0] * size for i in range(size)]
	#print(f"nums = ")
	#for nums in coords[0] :
	#	print(f"{nums}", end = ' ')
	right = size
	print(f"right = {right}")
	for r1 in range (0, right) :
		count = count + 1
		print(f"count = {count}")
		coords[0][r1] = count;
	dxstart = right - 1
	dystart = 1 # starts at row 1 ?only need xpos for down
	lxstart = size - 2	# col pos
	lystart = size - 1	# row pos
	uxstart = 0
	uystart = size - 2
	rxstart = 1
	rystart = 1
	for i in range (size, 0, -1) :
		if right == 1 : 
			break
		down = right - 1
		print(f"down = {down}")
		dypos = dystart
		for d in range (0, down) :
			count = count + 1
			print(f"count = {count}")
			coords[dypos][dxstart] = count
			dypos = dypos + 1
		dystart = dystart + 1
		dxstart = dxstart - 1
		print(f"nums = ")
		for nums in coords[3] :
			print(f"{nums}", end = ' ')
		print(' ')
		print(f"nums = ")
		for nums in coords[4] :
			print(f"{nums}", end = ' ')
		print(' ')

		left = down
		print(f"left = {left}")
		lxpos = lxstart
		for l in range (0, down) :
			count = count + 1
			print(f"count = {count}")
			coords[lystart][lxpos] = count
			lxpos = lxpos - 1
		lystart = lystart - 1
		lxstart = lxstart - 1
#		print(f"numsL = ")
#		for nums in coords[5] :
#			print(f"{nums}", end = ' ')
#		print(' ')

		if left == 1 : 
			break	
		up = left - 1
		print(f"up = {up}")
		uypos = uystart
		for u in range (0, up) :
			count = count + 1
			print(f"count = {count}")
			coords[uypos][uxstart] = count
			uypos = uypos - 1
		uystart = uystart - 1
		uxstart = uxstart + 1

		right = up
		print(f"right = {right}")
		rxpos = rxstart
		for r in range (0, right) :
			count = count + 1
			print(f"count = {count}")
			coords[rystart][rxpos] = count
			rxpos = rxpos + 1
		rystart = rystart + 1
		rxstart = rxstart + 1

		print(i)
	print(f"nums = ")
	for nums in coords[1] :
		print(f"{nums}", end = ' ')
	print(' ')
	print(f"nums = ")
	for nums in coords[2] :
		print(f"{nums}", end = ' ')
	print(' ')
	print(f"nums = ")
	for nums in coords[3] :
		print(f"{nums}", end = ' ')
	print(' ')
	print(f"nums = ")
	for nums in coords[4] :
		print(f"{nums}", end = ' ')
	print(' ')




