def solution(phone_book):
    # 문자열 정렬하면 앞에 숫자로 정렬됨
    phone_book.sort()

    # zip하면 한꺼번에 가져오기 가능함
    for a, b in zip(phone_book, phone_book[1:]):
        # a.startswith(b) : a리스트에 b라는 문자열이 포함되는지 
        if b.startswith(a):
            return False

    return True

list1 = ["119", "97674223", "1195524421"]
list2 = ["123","456","789"]
list3 = ["12","123","1235","567","88"]
# print(solution(list2))

