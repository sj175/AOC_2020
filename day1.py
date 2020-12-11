import advent_helpers
from typing import List


def part_1(problem_input: List[str]):
	my_map = {}
	for x in problem_input:
		if not my_map.get(x):
			my_map[2020 - x] = x
		else:
			return x * my_map[x]

	return my_map

def part_2(problem_input: List[str]):
	for x in problem_input:
		for y in problem_input:
			for z in problem_input:
				if x + y + z == 2020:
					return x*y*z

def main(problem_input):
	print(part_1([int(x) for x in problem_input.split("\n")[:-1]]))

	print(part_2([int(x) for x in problem_input.split("\n")[:-1]]))

if __name__ == '__main__':
	main(advent_helpers.get_problem_input(1, 1))