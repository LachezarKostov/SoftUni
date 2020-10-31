def loading_bar(percent):

    progression = percent // 10
    loadingbar = "["+progression*"%"+(10-progression)*"."+"]"

    if progression < 10:

        print(f"""{percent}% {loadingbar}
Still loading...""")

    else:
        print("""100% Complete!
[%%%%%%%%%%]""")


num = int(input())
loading_bar(num)

