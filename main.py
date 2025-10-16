def characters():
    text = input()

    char_len = 0
    digits = 0
    spaces= 0
    others = 0

    min_text = "abcdefghijklmnopqrstuvwxyz"
    max_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    space_text = " "

    for char in text:
        if char in min_text or char in max_text:
            char_len += 1
        elif char in numbers:
            digits += 1
        elif char in space_text:
            spaces += 1
        else:
            others += 1
    
    print(f"英文字符个数：{char_len}")
    print(f"数字个数：{digits}")
    print(f"空格个数：{spaces}")
    print(f"其他字符个数：{others}")

if __name__ == "__main__":
    characters()
