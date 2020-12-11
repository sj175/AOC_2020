import advent_helpers
from typing import List


def part_1(problem_input: List[str]):
	seat_ids = calculate_seat_ids(problem_input)

	return max(seat_ids.keys())


def part_2(problem_input: List[str]):
	seat_ids = calculate_seat_ids(problem_input)
	min_seat_id = min(seat_ids.keys())
	max_seat_id = 855 # from part 1
	total = sum(seat_ids.keys())

	sum_one_to_max = (max_seat_id * (max_seat_id + 1)) / 2
	sum_one_to_min = ((min_seat_id - 1) * min_seat_id) / 2
	expected_total = sum_one_to_max - sum_one_to_min

	return expected_total - total



def calculate_seat_ids(problem_input: List[str]):
	seat_ids = {}
	for boarding_pass in problem_input:
		row_min = 0
		row_max = 127
		col_min = 0
		col_max = 7
		for character in boarding_pass:
			if character == "F":
				row_max = (row_max + row_min) // 2
			elif character == "B":
				row_min = math.ceil((row_max + row_min) / 2)
			elif character == "L":
				col_max = (col_max + col_min) // 2
			elif character == "R":
				col_min = math.ceil((col_max + col_min) / 2)
			else:
				print("ERROR")

		assert row_max == row_min
		assert col_max == col_min

		seat_id = row_max * 8 + col_max
		seat_ids[seat_id] = boarding_pass

	return seat_ids


def main(problem_input):
	print(part_1(problem_input.split("\n")[:-1]))

	print(part_2(problem_input.split("\n")[:-1]))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(5, 1))