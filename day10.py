import advent_helpers
from typing import List


def part_1(problem_input: List[str]):
	the_input = sorted(problem_input)
	total_1 = 0
	total_3 = 1
	previous = 0
	for adaptor in the_input:
		diff = adaptor - previous
		previous = adaptor
		if diff == 1:
			total_1 += 1
		elif diff == 3:
			total_3 += 1

	return total_3 * total_1


def part_2(problem_input: List[str]):
	print(problem_input)


def main(problem_input):
	print(part_1(list(map(int, problem_input.split("\n")[:-1]))))

	print(part_2(list(map(int, problem_input.split("\n")[:-1]))))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(10, 1))
