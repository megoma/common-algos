# test_cases : 153(True); 1634(True); 92727(True)


def is_amstrong(num:int)->bool:
    return sum([int(i)**len(str(num)) for i in str(num)]) == num

print(is_amstrong(92727))