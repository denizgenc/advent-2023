import adventinput
import string

word_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_calibration_val(line: str) -> int:
    digits = [c for c in line if c in string.digits]
    first_last = "".join((digits[0], digits[-1]))
    return int(first_last)

def get_real_cal_val(line: str) -> int:
    digits = []
    for i in range(len(line)):
        for word, digit in word_digits.items():
            if line.startswith(word, i):
                digits.append(digit)
        if line[i] in string.digits:
            digits.append(line[i])
    first_last = "".join((digits[0], digits[-1]))
    return int(first_last)



if __name__ == "__main__":
    lines = adventinput.get_data(1)
    calibration_values = [get_calibration_val(l) for l in lines]
    print(sum(calibration_values))

    real_vals = [get_real_cal_val(l) for l in lines]
    print(sum(real_vals))
