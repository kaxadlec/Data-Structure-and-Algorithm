# data structure_algorithm #day01-2

def insert_data(idx, pokemon):
    """
    선형 리스트의 idx위치에 원소 삽입
    :param idx: int
    :param pokemon:str
    :return: void
    """
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


def delete_data(idx):
    """
    선형 리스트 idx 위치의 원소 삭제
    :param idx: int
    :return: str
    """
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None  # 데이터 삭제

    for i in range(idx + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    pokemons.pop()
    # del (pokemons[len_pokemons - 1])

    # self 3-1 professor
    # for _ in range(len_pokemons - idx):
    #     pokemons.pop()

    # self 3-1 my code
    # for n in range(1, len_pokemons):
    #     del (pokemons[len_pokemons - n])


def add_data(pokemon):
    """
    선형 리스트의 맨 뒤에 원소 삽입
    :param pokemon:
    :return:
    """
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon


if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]
    print(pokemons)
    # insert_data(2, '야도란')
    delete_data(1)
    print(pokemons)
    # insert_data(6, '피죤투')
    delete_data(3)
    print(pokemons)
    add_data('꼬링크')
    print(pokemons)


