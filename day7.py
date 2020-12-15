import advent_helpers
from typing import List
import collections


def parse(line):
	output = collections.defaultdict(list)
	split = line.split("bags contain")

	for bag in split[1].split(","):
		normalised_bag = bag.strip().strip(".")[2:]
		if normalised_bag.endswith("s"):
			normalised_bag = normalised_bag[:-5]
		else:
			normalised_bag = normalised_bag[:-4]
		output[split[0].strip()].append(normalised_bag)

	return output

def parse_with_numbers(problem_input):
	output = collections.defaultdict(list)

	for line in problem_input:
		split = line.split("bags contain")
		for bag in split[1].split(","):
			normalised_bag = bag.strip().strip(".")
			if normalised_bag.endswith("s"):
				normalised_bag = normalised_bag[:-5]
			else:
				normalised_bag = normalised_bag[:-4]
			if normalised_bag[0] == "n":
				number = 0
			else:
				number = int(normalised_bag[0])
			output[split[0].strip()].append((number, normalised_bag[2:]))

	return output


def part_1(problem_input: List[str]):
	rules = []
	for line in problem_input:
		rules.append(parse(line))

	to_examine = ["shiny gold"]
	seen = set()
	bag_can_lead_to_gold = set()
	while to_examine:
		current = to_examine[0]
		to_examine = to_examine[1:]		
		seen.add(current)
		for rule in rules:
			for k, v in rule.items():
				if current in v:
					bag_can_lead_to_gold.add(k)
					if k not in seen:
						to_examine.append(k)

	return bag_can_lead_to_gold


def part_2(problem_input: List[str]):
	rules = parse_with_numbers(problem_input)

	to_examine = 0
	bags = ["shiny gold"]
	while to_examine < len(bags):
		current = bags[to_examine]
		to_examine += 1
		for bag in rules[current]:
			bags.extend([bag[1]]*bag[0])


	return len(bags) - 1 # don't include the shiny gold bag



def main(problem_input):
	print(len(part_1(problem_input.split("\n")[:-1])))

	print(part_2(problem_input.split("\n")[:-1]))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(7, 1))
