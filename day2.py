import advent_helpers
from typing import List
import collections


def parse(to_parse):
	split = to_parse.split(" ")
	output = {}
	output['min'] = int(split[0].split("-")[0])
	output['max'] = int(split[0].split("-")[1])
	output['char'] = split[1].split(":")[0]
	output['password'] = split[2]

	return output


def part_1(problem_input: List[str]):
	total = 0
	for prob in problem_input:
		parsed = parse(prob)
		c = collections.Counter(parsed['password'])


		if parsed['min'] <= c[parsed['char']] <= parsed['max']:
			total += 1

	return total

def part_2(problem_input: List[str]):
	total = 0
	for prob in problem_input:
		parsed = parse(prob)
		if (parsed['password'][parsed['min'] - 1] == parsed['char']) ^ (parsed['password'][parsed['max'] - 1] == parsed['char']):
			total += 1

	return total


def main(problem_input):
	print(part_1(problem_input.split("\n")[:-1]))

	print(part_2(problem_input.split("\n")[:-1]))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(2, 1))