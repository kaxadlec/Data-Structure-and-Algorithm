# 함수 선언 부분
def print_poly(px):
    """
    다항식을 포멧에 맞게 출력하는 함수
    :param px: 계수를 원소로 가지는 리스트
    :return: 다항식 문자열
    """
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수

        # code 03-05.py
        # if coef >= 0 :
        #     poly_str = poly_str + "+"

        # self study 3-2
        if i > 0 and coef > 0:
            poly_str = poly_str + "+"
        elif coef == 0:
            term = term -1
            continue

        poly_str = poly_str + f'{coef}x^{term} '
        term = term - 1

    return poly_str


def calc_poly(x_val, p_x):
    """
    다항식의 산술연산을 하는 함수
    :param x_val: x값 integer
    :param p_x: 계수를 원소로 가지는 리스트
    :return: 다항식 계산 결과값 integer
    """
    return_val = 0
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = p_x[i]  # 계수
        return_val = return_val + coef * x_val ** term
        term = term - 1

    return return_val


# 전역 변수 선언 부분
px = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0


# 메인 코드 부분
if __name__ == "__main__":
    p_str = print_poly(px)
    print(p_str)
    x_val = int(input("X 값-->"))
    print(calc_poly(x_val, px))
