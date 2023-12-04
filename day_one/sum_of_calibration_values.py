def sum_calibration_values():
    calibration_vals = []
    with open("input_file.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        tmp = []
        for char in line:
            if char.isdigit():
                tmp.append(char)
        # line only contains one digit
        if len(tmp) == 1:
            num = int(''.join(tmp * 2))
            calibration_vals.append(num)
        else:
            first = tmp[0]
            second = tmp[len(tmp) - 1]
            num = int(first + second)
            calibration_vals.append(num)
    return sum(calibration_vals)

if __name__ == "__main__":
  print(sum_calibration_values())
