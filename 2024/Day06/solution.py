import os
from time import sleep
from typing import Any, Literal
from typing import TypeAlias

MapDirection: TypeAlias = Literal['^', '>', '<', 'v']

class GuardMap:
    def __init__(self, map_data: list[str]) -> None:
        self.map_data: list[str] = map_data
        self.guard_loc: list[int] = self.find_guard()
        self.guard_dir: MapDirection = self.get_guard_dir()

    def find_guard(self) -> list[int]:
        guard: list[MapDirection] = ['^','>','<','v']
        for y, row in enumerate(iterable=self.map_data):
            for x, spot in enumerate(iterable=row):
                if spot in guard:
                    return [x,y]
        raise Exception("Unable to locate guard.")
    
    def get_guard_dir(self) -> MapDirection:
            x, y = self.guard_loc
            return self.map_data[y][x]

    def move_direction(self) -> list[int]:
        match self.guard_dir:
            case 'v':
                return [1,0]
            case '^':
                return [-1,0]
            case '>':
                return [0,1]
            case '<':
                return [0, -1]
            case _:
                  raise Exception(f'Incorrect guard location: {self.guard_dir} @ {self.guard_loc}')
             
    def get_next_move(self) -> list[int]:
        x, y = self.move_direction()
        return [self.guard_loc[0] + y, self.guard_loc[1] + x]
    
    def change_direction(self) -> MapDirection:
        match self.guard_dir:
            case 'v':
                return '<'
            case '^':
                return '>'
            case '>':
                return 'v'
            case '<':
                return '^'

    def off_map(self, x: int,y: int) -> bool:
         if 0 <= x < len(self.map_data[0]) and 0 <= y < len(self.map_data):
              return False
         else:
              return True

    def replace_value(self, x: int, y: int, new_char: str):
             row = list(self.map_data[y])
             row[x] = new_char
             self.map_data[y] = ''.join(row)
             return

    def evaluate_move(self, next_x:int, next_y:int) -> None:
        curr_x: int = self.guard_loc[0]
        curr_y: int = self.guard_loc[1]
        #exit() if input(f"{curr_x = } | {curr_y = }\n{next_x = } | {next_y = }\n") == 'x' else None
        next_space: str = self.map_data[next_y][next_x]
        if next_space == '#':
            self.guard_dir = self.change_direction()
        else:
            self.replace_value(x=curr_x,y=curr_y, new_char='o')
            self.replace_value(x=next_x,y=next_y, new_char=self.guard_dir)
            self.guard_loc = [next_x, next_y]

    def move_guard(self) -> None:
        while True:
            # clprint('\n'.join(self.map_data))
            x,y = self.get_next_move()
            if self.off_map(x=x,y=y):
                 self.replace_value(x=self.guard_loc[0],y=self.guard_loc[1],new_char='o')
                 break
            self.evaluate_move(x,y)

        # evaluate next spot
        # - if spot off map - end
        # - if spot is # - rotate
        # - if spot is . or x - continue
        # move to spot
        # update old spot
        self.guard_loc = self.get_next_move()

def read_input(file_path: str) -> list[str]: 
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]

def part1(guard_map: GuardMap) -> int:
        total_spaces: int = 0
        guard_map.move_guard()
        for line in guard_map.map_data:
             line_spaces: int = line.count('o')
             total_spaces += line_spaces
        return total_spaces

def part2(data: list) -> int:
        # Implement part 2 solution here
        return 0

def clear_screen() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

def clprint(*args: Any, sleep_val: float = 0.01, **kwargs: Any) -> Any:
        clear_screen()
        print(*args, **kwargs)
        sleep(sleep_val)
        return

def main():
    file_path = './2024/Day06/input.txt'  # Change this to the appropriate file path
    lines: list[str] = read_input(file_path)
    guard_map: GuardMap = GuardMap(lines)
    result1: int = part1(guard_map)
    #data = parse_input(lines)
    
    #result1 = part1(lines)
    #result2 = part2(data)
    
    print(f'Part 1: {result1}')
    #print(f'Part 2: {result2}')

if __name__ == "__main__":
    main()
    