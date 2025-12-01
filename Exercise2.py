def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 70, 100)")

def get_user_input():
    user_input = input()
    string_list = user_input.split(",")
    float_list = []
    for i in string_list:
        float_list.append(float(i))

    return float_list

display_main_menu()
number = get_user_input()
print(number)