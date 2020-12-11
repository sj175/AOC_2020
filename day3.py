import advent_helpers
from typing import List


def part_1(problem_input: List[str]):
	ords = (0, 0)
	trees = 0
	while ords[0] < len(problem_input):
		if problem_input[ords[0]][ords[1] % len(problem_input[ords[0]])] == "#":
			trees += 1
		ords = (ords[0] + 1, ords[1] + 3)

	return trees

def part_1_generalised(problem_input: List[str], down: int, right: int):
	ords = (0, 0)
	trees = 0
	while ords[0] < len(problem_input):
		if problem_input[ords[0]][ords[1] % len(problem_input[ords[0]])] == "#":
			trees += 1
		ords = (ords[0] + down, ords[1] + right)

	return trees


def part_2(problem_input: List[str]):
	partial = lambda down, right: part_1_generalised(problem_input, down, right)
	return partial(1, 1) * partial(1, 3) * partial(1, 5) * partial(1, 7) * partial(2, 1)


def main(problem_input):
	print(part_1(problem_input.split("\n")[:-1]))

	print(part_2(problem_input.split("\n")[:-1]))

if __name__ == '__main__':
	main(advent_helpers.get_problem_input(3, 1))