import advent_helpers
from typing import List, Tuple


def taxi_distance(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> int:
	return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


def part_1(problem_input: List[str]):
	"""950 is too high"""
	heading = 90 # 0 is north, work clockwise
	location = (0, 0)
	for inst in problem_input:
		direction = inst[0]
		number = int(inst[1:])
		if direction == "L" or direction == "R":
			if not number % 90 == 0:
				print("complex turn detected")
			heading += number
			heading = heading % 360
		elif direction == "N":
			location = location[0] + number, location[1]
		elif direction == "S":
			location = location[0] - number, location[1]
		elif direction == "E":
			location = location[0], location[1] + number
		elif direction == "W":
			location = location[0], location[1] - number
		elif direction == "F":
			if heading == 0:
				location = location[0] + number, location[1]
			elif heading == 90:
				location = location[0], location[1] + number
			elif heading == 180:
				location = location[0] - number, location[1]
			elif heading == 270:
				location = location[0], location[1] - number
			else:
				print("bad heading")

	return taxi_distance(location, (0, 0))

			

def part_2(problem_input: List[str]):
	pass


def main(problem_input):
	print(part_1("""F10
N3
F7
R90
F11""".split("\n")))
	print(part_1(problem_input.split("\n")[:-1]))

	# print(part_2(list(map(list, problem_input.split("\n")[:-1]))))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(12, 1))
