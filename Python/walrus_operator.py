def walrus():
    s = 'wzh'
    if (n := len(s)) > 0:
        print(f'Test walrus operator: {n}')

    while x := [1,2,3]:
        print(x)
        break

if __name__ == '__main__':
    walrus()
