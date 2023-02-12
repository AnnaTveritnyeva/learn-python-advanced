def get_filter_by1(num):
    def divide_by_num(container):
        divided_container = []
        for i in container:
            if i % num == 0:
                divided_container.append(i)
        return divided_container

    return divide_by_num


def get_filter_by2(num):
    def divide_by_num(container):
        return list(filter(lambda i: i % num == 0, container))

    return divide_by_num


def get_filter_by3(num):
    return lambda ls: list(filter(lambda i: i % num == 0, ls))


fil1 = get_filter_by1(3)
fil2 = get_filter_by2(3)
fil3 = get_filter_by3(3)
z = [2, 3, 4, 5, 6, 7, 8]
print(fil1(z), fil2(z), fil3(z))
