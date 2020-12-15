import advent_helpers
from typing import List


def get_adjacent_ords(row, col):
	return {(row-1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), 
	(row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)}


def list_to_str(arr: List[List[str]]):
	output = ""
	for s in arr:
		for x in s:
			output += x
		output += "\n"

	return output


def part_1(problem_input: List[str]):
	for i, row in enumerate(problem_input):
		for j, seat in enumerate(row):
			if seat == ".":
				continue
			else:
				adjacent_seats = 0
				for surrounding in get_adjacent_ords(i, j):
					if (0 <= surrounding[0] < len(problem_input)) and (0 <= surrounding[1] < len(row)):
						if problem_input[surrounding[0]][surrounding[1]] == "#":
							adjacent_seats += 1
				if adjacent_seats >= 4:
					problem_input[i][j] = "L"
				elif adjacent_seats == 0:
					problem_input[i][j] = "#"

	print(list_to_str(problem_input))



def part_2(problem_input: List[str]):
	pass


def main(problem_input):
	print(part_1(list(map(list, """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split("\n")))))

	# print(part_1(list(map(int, problem_input.split("\n")[:-1]))))

	# print(part_2(list(map(int, problem_input.split("\n")[:-1]))))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(11, 1))
