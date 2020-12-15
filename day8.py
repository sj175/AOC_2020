import advent_helpers
from typing import List


def part_1(problem_input: List[str]):
	return run_code(problem_input)[1]


def run_code(problem_input: List[str]):
	accumulator = 0
	pointer = 0
	seen = []
	while True:
		if pointer < len(problem_input):
			current = tuple(problem_input[pointer].split(" ") + [pointer])
		else:
			return "halt", accumulator
		if current in seen:
			return "infinite loop", accumulator
		else:
			seen.append(current)
			if current[0] == "nop":
				pointer += 1
			elif current[0] == "acc":
				accumulator += int(current[1])
				pointer += 1
			elif current[0] == "jmp":
				pointer += int(current[1])


def part_2(problem_input: List[str]):
	for i, instruction in enumerate(problem_input):
		if instruction.split(" ")[0] == "nop":
			x = run_code(problem_input[:i] + [f"jmp {instruction.split(' ')[1]}"] + problem_input[i+1:])
			if x[0] == "halt":
				return x[1]
		elif instruction.split(" ")[0] == "jmp":
			x = run_code(problem_input[:i] + [f"nop {instruction.split(' ')[1]}"] + problem_input[i+1:])
			if x[0] == "halt":
				return x[1]

	return ""


def main(problem_input):
	print(part_1(problem_input.split("\n")[:-1]))

	print(part_2(problem_input.split("\n")[:-1]))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(8, 1))
