import re
from functools import reduce

bad_code_test = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

def extract_equations(code_str: str) -> list[str]:
    return re.findall(pattern=r'mul\(\d{1,3},\d{1,3}\)', string=code_str)

def extract_product(string_line: str) -> int:
    return reduce(lambda x, y: x * y, map(int, string_line[4:-1].split(sep=",")))

def main(bad_code: str) -> None:
    result = 0
    list_of_strings: list[str] = extract_equations(bad_code)
    for code_line in list_of_strings:
        result += extract_product(code_line)
    print(result)
    


if __name__ == "__main__":
    #main(bad_code_test)
    with open("./2024/Day3/day3.txt","r") as f:
        bad_code_pt1 = f.read()
    main(bad_code_pt1)