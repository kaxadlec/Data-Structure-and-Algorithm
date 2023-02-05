def find_insert(mon, defen):
    find_pos = -1
    for i in range(len(pokemon)):
        str_list = list(pokemon[i].values())
        int_list = list(map(int, str_list))
        if defen > int_list:
            find_pos = i
            break

    if find_pos == -1:
        find_pos = len(pokemon)

    insert(find_pos, (mon, defen))


def insert(pos, info):
    if pos < 0 or pos > len(pokemon):
        print("out of range")
        return

    pokemon.append(None)  # len(chelsea) = 6

    for i in range(len(pokemon) - 1, pos, -1):
        pokemon[i] = pokemon[i - 1]
        pokemon[i - 1] = None

    pokemon[pos] = info



# list - dictionary
pokemon = [{'피카츄': '262'}, {'모부기': '187'}, {'팽도리': '135'}, {'브케인': '119'}, {'치코리타': '105'}]


if __name__ == "__main__":
    while True:
        data = input("추가할 포켓몬을 입력하시오: ")
        count = list(map(int, input("방어력를 입력하시오: ").split()))
        find_insert(data, count)
        print(pokemon)
