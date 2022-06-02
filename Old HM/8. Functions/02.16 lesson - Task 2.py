def nested_parentheses(str1):
    lst_1, dict_1 = [], {"(": ")"}
    for parenthese in str1:
        if parenthese in dict_1:
            lst_1.append(parenthese)
        elif len(lst_1) == 0 or dict_1[lst_1.pop()] != parenthese:
            return False
    return len(lst_1) == 0

if __name__ == '__main__':
    print(nested_parentheses("(()()(())"))