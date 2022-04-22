# 49. Group Anagrames
# 그룹 애너그램
# 난이도 : ★★

# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:  # 내가 푼거 -> 시간복잡도에서 걸림 ㅠ

    word_dict ={}

    for str in strs:
        flag = True
        for key in list(word_dict.keys()):

            key_length = len(key)
            count = 0
            temp_key = key
            for word in str:
                if word in temp_key:
                    count += 1
                    temp_key = temp_key.replace(word, '', 1)

            if count == key_length and key_length != 0 and (key_length == len(str)):
                word_dict[key].append(str)
                flag = False
                break

            if str == '':
                try:
                    word_dict[str].append(str)
                except KeyError:
                    word_dict[str] = [str]
                
                flag = False
                break

        if flag:
            word_dict[str] = [str]
    

    answer = []

    for value in list(word_dict.values()):
        answer.append(value)

    return answer

["","b"]
# print(groupAnagrams( ["eat","tea","tan","ate","nat","bat"]))
# print(groupAnagrams( ["",""]))

# print(groupAnagrams( ["","b", '']))

# print(groupAnagrams(["ddddddddddg","dgggggggggg"]))
print(groupAnagrams(["eat","tea","tan","ate","nat","bat","ac","bd","aac","bbd","aacc","bbdd","acc","bdd"]))

# print(groupAnagrams(["ac","acc"]))


def groupAnagrams(strs: List[str]) -> List[List[str]]:  # 첫번째 풀이 sorted 하면 됨 ㅋㅋㅋ

    word_dict = {}

    for str in strs:
        sort_str = sorted(str) # 애너그램은 같은 문자로 다른 언어를 만드는 것이라서 정렬하면 모두 같아짐
        
        # 참고 sorted(list, key = fn) key에 함수(lambda)를 넣으면 해당 값을 기준으로 정렬해줌
        # lambda 는 함수를 반환해줌

        # 파이썬에서 정렬함수는 팀소트를 사용함 -> 최선 O(n) 평균 O(n log n)  최악 (n log n)
        # 팀소트는 파이썬뿐만 아니라 다른 언어에서도 사요됨 ex) java 7 의 array.sort() 

        join_str = ''.join(sort_str) # sorted는 리스트를 반환하기 때문에 join함수로 문자열로 합치기

        try:
            word_dict[join_str].append(str)
        except KeyError:
            word_dict[join_str] = [str]

    
    return list(word_dict.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat","ac","bd","aac","bbd","aacc","bbdd","acc","bdd"]))