def main():
    s = input()
    letters = 0
    digits = 0
    spaces = 0
    others = 0
    
    for char in s:
        # 检查是否为英文字母
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            letters += 1
        # 检查是否为数字
        elif '0' <= char <= '9':
            digits += 1
        # 检查是否为空格
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
