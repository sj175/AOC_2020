def get_problem_input(day: int, part: int):
	with open(f"day{day}_part{part}.txt", "r") as f:
		return f.read()