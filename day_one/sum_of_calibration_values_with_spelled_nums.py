import re

def translate_to_int_str(num):
    nums = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    return nums[num]

def sum_calibration_values():
    total = 0
    with open("input_file.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
        pattern = re.compile(regex)
        numbers = pattern.findall(line)

        for i in range(len(numbers)):
            if numbers[i].isdigit():
                continue
            else:
                numbers[i] = translate_to_int_str(numbers[i])
        print(numbers)
        # line only contains one digit
        if len(numbers) == 1:
            num = int(''.join(numbers * 2))
            total += num
        else:
            first = numbers[0]
            second = numbers[-1]
            num = int(first + second)
            total += num
    return total

if __name__ == "__main__":
  print(sum_calibration_values())
