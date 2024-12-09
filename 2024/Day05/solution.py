def read_input(file_path: str) -> list[str]: 
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
        file_path = './2024/Day05/input.txt'  # Change this to the appropriate file path
        lines = read_input(file_path)
        data = parse_input(lines)
        
        result1 = part1(data)
        result2 = part2(data)
        
        print(f'Part 1: {result1}')
        print(f'Part 2: {result2}')

    if __name__ == "__main__":
        main()
    