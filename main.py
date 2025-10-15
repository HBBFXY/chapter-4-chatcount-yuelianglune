def main():
    input_string = input()
    filtered_string = ''
    for char in input_string:
        if char != "'":
            filtered_string += char
            
    letters = 0
    digits = 0
    spaces = 0
    others = 0
    
    for char in filtered_string:
        # 英文字符（包括大小写字母）
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            letters += 1
        # 数字
        elif '0' <= char <= '9':
            digits += 1
        # 空格
        elif char == ' ':
            spaces += 1
        # 其他字符
        else:
            others += 1
            
    print(f"英文字符: {letters}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {others}")

if __name__ == "__main__":
    main()
