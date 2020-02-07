import sys
print(sys.version_info)

def spiral_matrix(size):
	if size < 0 :
		raise Exception("size must be a positive integer")

	if size == 0 :
		coords = []
		return coords

#	if size == 1 :
#		print('Spiral matrix of size 1')
#		print('1')
#		coords = [[1]]	# I don't like this
#		return coords

	if size >= 0 :
		# Initialize count 
		count = 0;
		# Initialize multi-dimensional coords list to 0
		# 0s makes obvious when printing since 0s not used otherwise
		coords = [[0] * size for i in range(size)]

		# Fill values accross top row of matrix
		right = size
		print(f"right = {right}")
		for r1 in range (0, right) :
			count = count + 1
			print(f"count = {count}")
			coords[0][r1] = count;

		# start position tracking of each direction movement: d, l, u, r
		# relative starting positions
		dxstart = right - 1	# down x start
		dystart = 1 	# starts at row 1 ?only need xpos for down
		lxstart = size - 2	# left col pos
		lystart = size - 1	# left row pos
		uxstart = 0	# up starts at 0 
		uystart = size - 2
		rxstart = 1
		rystart = 1

		# the rest of the maxtrix follows a pattern
		# down, left, up, right, down, left, up, right...
		# until count = 1
		for i in range (size, 0, -1) :
			# Because the pattern runs in duplicates, meaning
			# down's length = right's length and
			# up's length = right's length
			# only need to check first cases, 
			# if right = 1, or left = 1 then reached end of matrix
			if right == 1 : 
				break
			# down col's length = preceding right row - 1
			down = right - 1
			print(f"down = {down}")
			# down y position is relative beginning at dystart
			dypos = dystart
			# using known down's column length, 
			# fill in coordinate cells with count values
			for d in range (0, down) :
				count = count + 1
				print(f"count = {count}")
				coords[dypos][dxstart] = count
				dypos = dypos + 1
			# set start position for next possible down col
			dystart = dystart + 1
			dxstart = dxstart - 1

			# from pattern we know
			# left row's length = preceding down col's length
			left = down
			print(f"left = {left}")
			lxpos = lxstart
			# using known left's row length
			# fill in coordinate cells with count values
			for l in range (0, down) :
				count = count + 1
				print(f"count = {count}")
				coords[lystart][lxpos] = count
				lxpos = lxpos - 1
			# set start position for next possible left row
			lystart = lystart - 1
			lxstart = lxstart - 1

			if left == 1 : 
				break
			# from pattern we know
			# up's col length = preceding left's row length - 1	
			up = left - 1
			print(f"up = {up}")
			uypos = uystart
			# using known up's column length
			# fill in coordinate cells with count values
			for u in range (0, up) :
				count = count + 1
				print(f"count = {count}")
				coords[uypos][uxstart] = count
				uypos = uypos - 1
			# set start position for next possible up col
			uystart = uystart - 1
			uxstart = uxstart + 1

			# from pattern we know
			# right's row length = preceding up's col length
			right = up
			print(f"right = {right}")
			rxpos = rxstart
			# using known right's row length
			# fill in coordinate cells with count values
			for r in range (0, right) :
				count = count + 1
				print(f"count = {count}")
				coords[rystart][rxpos] = count
				rxpos = rxpos + 1
			# set start position for next possible right row
			rystart = rystart + 1
			rxstart = rxstart + 1

			print(i)

#		for record in coords:
#			print(record)

		return coords

#print 2-dimensional list by row, individual cell by cell
def show_matrix(size, matrix) :
	for row in range(size) :
		for col in range(size) :
			print(matrix[row][col], end = ' ')
		print()


size = 7
matrix_filled = spiral_matrix(size)
show_matrix(size, matrix_filled)


