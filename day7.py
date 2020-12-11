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

	to_examine = [(1, "shiny gold", 1)] #how many, name, multiplier from "above" layer
	total = 0
	while to_examine:
		print(to_examine)
		print(total)
		current = to_examine[0]
		to_examine = to_examine[1:]
		total += current[0] * current[2]
		print(total)
		for bag in rules[current[1]]:
			print(rules[current[1]])
			to_examine.append((bag[0], bag[1], current[0]))


	return total



def main(problem_input):
	# print(len(part_1(problem_input.split("\n")[:-1])))

	# print(part_2(problem_input.split("\n")[:-1]))

	print(part_2("""shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".split("\n")[:-1]))


if __name__ == '__main__':
	main(advent_helpers.get_problem_input(7, 1))
