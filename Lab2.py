def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()                  # 1. receive
    str_list = user_input.split(",")      # 2. cut at commas
    num_list = []                         # empty list to fill
    for item in str_list:                 # 3. for each piece...
        num_list.append(float(item))      #    ...convert and add to the list
    return num_list            

def calc_average(temp_list):
    average = sum(temp_list) / len(temp_list)
    return average

def find_min_max(temp_list):
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    return [min_temp, max_temp]

def sort_temperature(temp_list):
    print("sort_temperature")

def calc_median_temperature(temp_list):
    print("calc_median_temperature")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

    average = calc_average(num_list)
    print(f"Average: {average}")

    min_max = find_min_max(num_list)
    print(f"Min: {min_max[0]}, Max: {min_max[1]}")

if __name__ == "__main__":
    main()