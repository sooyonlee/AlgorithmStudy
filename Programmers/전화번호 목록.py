# zip 이용하기
def solution(phone_book):
    # string의 경우 사전식 비교 1->2->10(x), 1-> 10->2(o)
    # 모든 요소를 방문할 필요 없이 다음 문자열과 비교만 하면 됨.
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True