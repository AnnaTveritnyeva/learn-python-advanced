def get_filter_by(num):
    def divide_all(container):
        divided_by_num = []
        for i in range(len(container)):
            if container[i] % num == 0:
                divided_by_num.append(container[i])
        return divided_by_num

    return divide_all


fil = get_filter_by(3)
z = [2, 3, 4, 5, 6, 7, 8]

print(fil(z))
