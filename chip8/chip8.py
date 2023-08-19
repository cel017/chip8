from time import perf_counter
from chip8.config import DELAY


timer = 0
startTime = perf_counter()

while True:
	endTime = perf_counter()
	deltaTime = min(endTime-startTime, DELAY)
	timer += deltaTime
	startTime = endTime

	if timer >= DELAY:
		###
		# CPU CYCLE HERE
		###
		
		# decrement insead of reset:
		# accumulates extra milliseconds
		timer-=DELAY