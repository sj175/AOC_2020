import advent_helpers
from typing import List


def is_sum(building_blocks: List[int], number: int):
	seen = set()
	for x in building_blocks:
		if number - x in seen:
			return True
		
		seen.add(x)

	return False

def part_1(problem_input: List[str]):
	preamble_length = 25
	preamble_start = 0
	preamble_end = preamble_start + preamble_length
	current = preamble_length

	while preamble_end < len(problem_input):
		if not is_sum(map(int, problem_input[preamble_start:preamble_end]), int(problem_input[current])):
			return problem_input[current]

		current += 1
		preamble_start += 1
		preamble_end += 1




def part_2(problem_input: List[str]):
	total = int(part_1(problem_input))
	problem_input = list(map(int, problem_input))
	left = 0
	right = 0
	while sum(problem_input[left:right]) != total:
		current_sum = sum(problem_input[left:right])
		if current_sum < total:
			right += 1
		elif current_sum > total:
			left += 1

	return min(problem_input[left:right]) + max(problem_input[left:right])


def main(problem_input):
	print(part_1(problem_input.split("\n")[:-1]))

	print(part_2(problem_input.split("\n")[:-1]))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(9, 1))
