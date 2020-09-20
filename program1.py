string = input("enter a string with special characters : ")

string_list = list(string)

right_side = len(string)-1
left_side = 0

while left_side < right_side:
    if string_list[left_side].isalpha() and string_list[right_side].isalpha():
        string_list[left_side],string_list[right_side] = string_list[right_side],string_list[left_side]
        right_side -=1
        left_side +=1
    elif string_list[left_side].isalpha() and (string_list[right_side].isalpha() == False):
        right_side -= 1
    elif (string_list[left_side].isalpha() == False) and string_list[right_side].isalpha():
        left_side += 1
    else:
        right_side -= 1
        left_side += 1
print(''.join(string_list))







