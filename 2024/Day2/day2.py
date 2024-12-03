def list_is_ordered(line: list[int]) -> bool:
    if line in (sorted(line), sorted(line, reverse=True)):
        return True
    else:
        return False

def levels_differ_small(line: list[int]) -> bool:
    list_len: int = len(line) - 1
    for i in range(list_len):
        if not (1 <= abs(line[i] - line[i + 1]) <= 3):
            return False
    return True

def pt2_eval(lst: list[int]) -> int:
    for i in range(len(lst)):
        new_lst: list[int] = lst[:i] + lst[i + 1:]
        if list_is_ordered(new_lst) and levels_differ_small(new_lst):
            return True
    return False
                    
def main():
    with open("2024/Day2/day2.txt") as f:
            data = [line.strip() for line in f.readlines()]
    data = [[int(num) for num in line.split()] for line in data]
    pt1_result: int = 0
    pt2_result: int = 0
    for line in data:
        if list_is_ordered(line) and levels_differ_small(line):
            pt1_result += 1
        elif pt2_eval(line):
            pt2_result += 1
        else:
            continue
    print(pt1_result)
    print(pt1_result + pt2_result)

if __name__ == "__main__":
    main()