import advent_helpers
from typing import List
import copy



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


def count_seats(seat_grid: List[List[str]]):
	total = 0
	for row in seat_grid:
		for j in range(len(row)):
			if row[j] == "#":
				total += 1

	return total


def part_1(problem_input: List[List[str]]):
	max_iterations = 500
	current = 0
	while current < max_iterations:
		current += 1
		next_state = copy.deepcopy(problem_input)
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
						next_state[i][j] = "L"
					elif adjacent_seats == 0:
						next_state[i][j] = "#"
					else:
						next_state[i][j] = problem_input[i][j]

		if problem_input == next_state:
			print(f"stabilised after {current} iterations")
			break
		problem_input = copy.deepcopy(next_state)

	return count_seats(next_state)


def get_adjacent_ords_line_of_sight(row, col, current_state):
	units = [-1, 0, 1]
	i = j = 0
	while (row - i > 0) and (col - j > 0) and (current_state[row - i][col - j] not in {"L", "#"}):
		i += 1
		j += 1

	print(current_state[row - i][col - j])


def get_adj_los(row, col, current_state):
	units = [-1, 0, 1]
	for i in units:
		for j in units:
			if i == j == 0:
				continue
			x = i
			y = j
			while (0 < row + x < len(current_state)) and (0 < col + y < len(current_state[0])) and (current_state[row + x][col + y] not in {"L", "#"}):
				x += i
				y += j
			

def part_2(problem_input: List[str]):
	max_iterations = 500
	current = 0
	while current < max_iterations:
		current += 1
		next_state = copy.deepcopy(problem_input)
		for i, row in enumerate(problem_input):
			for j, seat in enumerate(row):
				if seat == ".":
					continue
				else:
					adjacent_seats = 0
					for surrounding in get_adjacent_ords_line_of_sight(i, j, problem_input):
						if (0 <= surrounding[0] < len(problem_input)) and (0 <= surrounding[1] < len(row)):
							if problem_input[surrounding[0]][surrounding[1]] == "#":
								adjacent_seats += 1
					if adjacent_seats >= 4:
						next_state[i][j] = "L"
					elif adjacent_seats == 0:
						next_state[i][j] = "#"
					else:
						next_state[i][j] = problem_input[i][j]

		if problem_input == next_state:
			print(f"stabilised after {current} iterations")
			break
		problem_input = copy.deepcopy(next_state)

	return count_seats(next_state)


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

	print(part_1(list(map(list, problem_input.split("\n")[:-1]))))

	print(part_2(list(map(list, problem_input.split("\n")[:-1]))))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(11, 1))
