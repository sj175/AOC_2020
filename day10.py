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

def get_run_lengths(arr, target):
	output = []
	current_total = 0
	for element in arr:
		if element == target:
			current_total += 1
		else:
			output.append(current_total)
			current_total = 0

	return output


def part_2(problem_input: List[str]):
	"""I was pleased when I came up with this, but look at the one below"""
	problem_input = sorted(problem_input)
	problem_input = [0] + problem_input + [problem_input[-1] + 3]
	diffs = [x - problem_input[i - 1] for i, x in enumerate(problem_input) if i > 0]
	run_lengths = get_run_lengths(diffs, 1)

	total = 1
	for x in run_lengths:
		if x == 4:
			total *= 7
		elif x == 3:
			total *= 4
		elif x == 2:
			total *= 2
		else:
			continue

	return total


def wtf(problem_input):
	"""this is pure genius (not my code, but I can explain it for those interested)"""
	problem_input = sorted(problem_input)
	problem_input.append(problem_input[-1] + 3)

	memo = {0: 1}
	for r in problem_input:
		memo[r] = memo.get(r-3,0) + memo.get(r-2,0) + memo.get(r-1,0)

	return memo[problem_input[-1]]


def main(problem_input):
	print(part_1(list(map(int, problem_input.split("\n")[:-1]))))

	print(part_2(list(map(int, problem_input.split("\n")[:-1]))))

	print(wtf(list(map(int, problem_input.split("\n")[:-1]))))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(10, 1))
