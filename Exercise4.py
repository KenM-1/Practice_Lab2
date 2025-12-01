def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 20, 70, 100)")

def get_user_input():
    user_input = input()
    string_list = user_input.split(",")
    float_list = []
    for num_str in string_list:
        float_list.append(float(num_str))
    return float_list

def calc_average_temperature(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

def calc_median_temperature(numbers):
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    median_index = n // 2
    if n % 2 == 1:
        median = sorted_numbers[median_index]
    else:
        median = (sorted_numbers[median_index -1] + sorted_numbers[median_index]) / 2
    return median

def calc_min_max_temperature(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return [smallest, largest]

def main():
    display_main_menu()
    numbers = get_user_input()
    average = calc_average_temperature(numbers)
    min_max = calc_min_max_temperature(numbers)
    median = calc_median_temperature(numbers)
    sorted_numbers = sorted(numbers)
    print("You entered: ", numbers)
    print(sorted_numbers)
    print("Average: ", average)
    print("Median: ", median)
    print("Minimum: ", min_max[0])
    print("Maxmimum: ", min_max[1])

if __name__ == "__main__":
    main()
