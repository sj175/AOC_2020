import advent_helpers
from typing import List
import collections

def part_1(problem_input: List[str]):
	total = 0
	for group in problem_input:
		questions = set()
		for person in group.split("\n"):
			for char in person:
				questions.add(char)
		total += len(questions)

	return total

def part_2(problem_input: List[str]):
	total = 0
	for group in problem_input:
		total_for_group = 0
		questions = collections.defaultdict(int)
		for person in group.split("\n"):
			for char in person:
				questions[char] += 1

		for key, value in questions.items():
			if value == len(group.split("\n")):
				total_for_group += 1

		total += total_for_group

	return total


def main(problem_input):
	print(part_1(problem_input.split("\n\n")))

	print(part_2(problem_input.split("\n\n")))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(6, 1))