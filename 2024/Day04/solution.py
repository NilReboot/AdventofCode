def read_input(file_path: str) -> list[str]: 
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]

def extract_lines(data: list[str]) -> list[str]:
    col_list: list[str] = []
    for x in range(len(data)):
        line_str: str = ''
        for y in range(len(data[0])):
            line_str += data[y][x]
        col_list.append(line_str)
    return col_list + data

def find_word(extracted_line:str, lookup_word: str = 'XMAS') -> int:
    fwd_count: int = extracted_line.count(lookup_word)
    bck_count: int = extracted_line[::-1].count(lookup_word)
    return fwd_count + bck_count

def extract_diagonals(grid: list[str])-> list[str]:
    rows, cols = len(grid), len(grid[0])
    diagonals: list[str] = []

    def get_diagonal(start_row: int, start_col: int, row_step: int, col_step: int) -> str:
        diagonal: list[str] = []
        r, c = start_row, start_col
        while 0 <= r < rows and 0 <= c < cols:
            diagonal.append(grid[r][c])
            r += row_step
            c += col_step
        return ''.join(diagonal)

    patterns: list[list[tuple[int, int, int, int]]] = [
        # (start_row, start_col, row_step, col_step)
        # Right-down diagonals from left edge
        [(r, 0, 1, 1) for r in range(rows)] +
        # Right-down diagonals from top edge
        [(0, c, 1, 1) for c in range(1, cols)] +
        # Right-up diagonals from bottom edge
        [(rows-1, c, -1, 1) for c in range(cols)] +
        # Right-up diagonals from right edge
        [(r, 0, -1, 1) for r in range(rows-2, -1, -1)]
    ]

    for start_row, start_col, row_step, col_step in [item for sublist in patterns for item in sublist]:
        diagonal: str = get_diagonal(start_row, start_col, row_step, col_step)
        diagonals.append(diagonal)
    return diagonals


def part1(data: list[str]) -> int:
    results: int = 0
    for line in extract_lines(data=data):
        results += find_word(extracted_line=line)
    for line in extract_diagonals(grid=data):
        results += find_word(extracted_line=line)
    return results

def part2():
    return

def main():
    file_path = './2024/Day04/input.txt'  # Change this to the appropriate file path
    lines: list[str] = read_input(file_path=file_path)
    pt1_results: int = part1(data=lines)
    
    print(f'{pt1_results = }')
    #print(f'{pt1_results = }')

if __name__ == "__main__":
    main()
    