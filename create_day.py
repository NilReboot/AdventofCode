import os
import argparse
from datetime import datetime

TEMPLATE = """def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def parse_input(lines: list[str]) -> list:
    # Implement your parsing logic here
    return [line.split() for line in lines]

def part1(data: list) -> int:
    # Implement part 1 solution here
    return 0

def part2(data: list) -> int:
    # Implement part 2 solution here
    return 0

def main():
    file_path = 'input.txt'  # Change this to the appropriate file path
    lines = read_input(file_path)
    data = parse_input(lines)
    
    result1 = part1(data)
    result2 = part2(data)
    
    print(f'Part 1: {result1}')
    print(f'Part 2: {result2}')

if __name__ == "__main__":
    main()
"""

def create_day_folder(year: int, day: int):
    folder_name: str = f"{year}/Day{day:02d}"
    os.makedirs(name=folder_name, exist_ok=True)
    
    # Create the Python template file
    with open(file=os.path.join(folder_name, "solution.py"), mode='w') as f:
        f.write(TEMPLATE)
    
    # Create the input text file
    open(os.path.join(folder_name, "input.txt"), mode='w').close()
    
    print(f"Created folder and files for Year {year}, Day {day}")

if __name__ == "__main__":
    current_year: int = datetime.now().year
    current_day: int = datetime.now().day 
    parser = argparse.ArgumentParser(description="Generate Advent of Code day folder and files.")
    parser.add_argument("day", type=int, default=current_day, help="Day of the Advent of Code")
    parser.add_argument("--year", type=int, default=current_year, help=f"Year of the Advent of Code (default: {current_year})")
    
    args: argparse.Namespace = parser.parse_args()
    
    create_day_folder(year=args.year, day=args.day)