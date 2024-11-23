def check_age(age):
    assert age >= 18, "You may be 18 years old or more"
    print("You can use this service")


try:
    check_age(20)
    check_age(16)
except AssertionError as e:
    print(e)

def process_list(input_list):
    assert len(input_list) >= 3, "The list must contain at least 3 elements"
    print(f"The list contains {len(input_list)} elements")


try:
    process_list([1, 2, 3])
    process_list([1])
except AssertionError as e:
    print(e)



try:
    check_age(25)
    check_age(17)
except AssertionError as e:
    print(e)


try:
    process_list([1, 2, 3, 4])
    process_list([1, 2])
except AssertionError as e:
    print(e)
