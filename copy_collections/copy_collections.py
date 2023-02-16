import copy

machines = {'user1': 'booboo',
            'user2': 'rupert',
            'user3': 'teddy',
            'user4': 'care',
            'user5': 'winnie',
            'user6': 'sooty',
            'user7': 'padders',
            'user8': 'polar',
            'user9': 'grizzly',
            'user10': 'baloo'}

machines_copy = copy.deepcopy(machines)

machines['user1'] = None

print(machines)
print(machines_copy)
