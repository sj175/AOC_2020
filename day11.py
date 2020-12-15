import advent_helpers
from typing import List


def get_adjacent_ords(row, col):
	return {(row-1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), 
	(row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)}

def part_1(problem_input: List[str]):
	for row in problem_input:
		for col in row:
			


def part_2(problem_input: List[str]):
	pass


def main(problem_input):
	print(part_1("""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split("\n")))

	# print(part_1(list(map(int, problem_input.split("\n")[:-1]))))

	# print(part_2(list(map(int, problem_input.split("\n")[:-1]))))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(11, 1))
