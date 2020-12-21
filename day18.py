import advent_helpers
from typing import List
import copy


def try_int(maybe_int: str):
	try:
		return int(maybe_int)
	except ValueError:
		return 0

def evaluate(expr: str):
	if x := try_int(expr):
		return x

	split = expr.split(" ")
	print(split)

def part_1(problem_input: List[List[str]]):
	total = 0
	for line in problem_input:
		total += evaluate(line)

	return total
			

def part_2(problem_input: List[str]):
	pass


def main(problem_input):
	print(part_1("""2 * 3 + (4 * 5)""".split("\n")))

	# print(part_1(list(map(list, problem_input.split("\n")[:-1]))))

	# print(part_2(list(map(list, problem_input.split("\n")[:-1]))))


if __name__ == '__main__':
	main(None)
	# main(advent_helpers.get_problem_input(18, 1))
