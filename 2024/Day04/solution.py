from gettext import find


def read_input(file_path: str) -> list[str]: 
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]

def parse_input(lines: list[str]) -> list[str]:
    new_lol: list[str] = []
    for x, line in enumerate(lines[0]):
         new_line: str = ''
         for y,letter in enumerate(line):
              new_line += letter[x]
         new_lol[y] = new_line
    return new_lol #[line.split() for line in lines]

def part1(data: list) -> int:
    results: int = 0
    lookup_word = 'XMAS'
    for line in data:
        fwd_count: int = line.count(lookup_word)
        bck_count: int = line[::-1].count(lookup_word)
        results += (fwd_count + bck_count)
    return results

def part2(data: list) -> int:
    # Implement part 2 solution here
    return data

def main():
    file_path = './2024/Day04/test.txt'  # Change this to the appropriate file path
    lines = read_input(file_path)
    print(lines)
    #exit() if input() == 'x' else None
    data = parse_input(lines)
    
    result1 = part1(lines)
    result2 = part2(data)
    
    print(f'Part 1: {result1}')
    print(f'Part 2: {result2}')

if __name__ == "__main__":
    main()
    