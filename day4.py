import advent_helpers
from typing import List
import re


def part_1(problem_input: List[str]):
	total = 0
	for passport in problem_input:
		if all_fields_present(passport):
			total += 1

	return total

def all_fields_present(passport):
	required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	keys = {x.split(":")[0] for x in passport.split()}
	return all([req in keys for req in required])

def part_2(problem_input: List[str]):
	total = 0
	for passport in problem_input:
		if all_fields_present(passport):
			key_value = {x.split(":")[0]:x.split(":")[1] for x in passport.split()}
			if all([validate(key, value) for key, value in key_value.items()]):
				total += 1

	return total

def validate(key, value):
	if key == "byr":
		if re.match(r"[0-9]{4}", value):
			return 1920 <= int(value) <= 2002
	elif key == "iyr":
		if re.match(r"[0-9]{4}", value):
			return 2010 <= int(value) <= 2020
	elif key == "eyr":
		if re.match(r"[0-9]{4}", value):
			return 2020 <= int(value) <= 2030
	elif key == "hgt":
		if re.match(r"[0-9]{2,3}(cm|in)$", value):
			if value.endswith("cm"):
				return 150 <= int(value.split("cm")[0]) <= 193
			elif value.endswith("in"):
				return 59 <= int(value.split("in")[0]) <= 76
			else:
				print("this should never happen.")
	elif key == "hcl":
		return bool(re.match(r"#(([0-9]|[a-f]){6})$", value))
	elif key == "ecl":
		return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
	elif key == "pid":
		return bool(re.match(r"[0-9]{9}$", value))

	elif key == "cid":
		return True

	else:
		print("shouldn't have got here")


def main(problem_input):
	print(part_1(problem_input.split("\n\n")))

	print(part_2(problem_input.split("\n\n")))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(4, 1))