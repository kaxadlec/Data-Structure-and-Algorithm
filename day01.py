# data structure_algorithm #day01-2

def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]
    print(pokemons)
    insert_data(2, '야도란')
    print(pokemons)
    insert_data(6, '피죤투')
    print(pokemons)


