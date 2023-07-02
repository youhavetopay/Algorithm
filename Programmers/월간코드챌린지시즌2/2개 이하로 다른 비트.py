def solution(numbers):

    '''
        나의 풀이
        10진수 숫자가 주어지면 2진수 비트가 다른개 1 ~ 2개인
        제일 작은 수를 찾아주는 문제

        나의 접근법
        일단 수를 2진수로 바꾼다음
        뒤에서부터 0인걸 찾고 해당 자리수를 1로 바꿔주고
        해당 자리수 + 1부터 다시 뒤로 가면서 1을 0으로 바꿔주는 방식으로 품

        이렇게 하니까 시간복잡도는 안걸림 ㅋㅋ

        근데 나의 실수 때문에
        질문하기에 있는 테스트케이스를 보고 풀 수 있었음 ㅠㅠ
        반복문을 끝까지 가야하는데 길이 -1 까지만 가서 실패했던거였음 ㅋㅋㅋ

        꼼꼼히 잘 확인하자.. 
    '''

    answer = []

    for num in numbers:

        bin_num = list(bin(num)[2:])
        print(bin_num)
        length = len(bin_num) - 1
        i = length
        
        while i >= 0:

            if bin_num[i] == '0':
                bin_num[i] = '1'
                j = i + 1
                while j <= length:
                    if bin_num[j] == '1':
                        bin_num[j] = '0'
                        break
                    j += 1
                break
        
            i -= 1
        else:
            bin_num = ['1'] + bin_num
            bin_num[1] = '0'
        
        print(bin_num)
        print()
        f_x = int(''.join(bin_num), 2)
        answer.append(f_x)

    return answer

# print(solution([2,7, 61, 123, 11, 31743, 63486]))
print(solution([1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]))
print(int('111101111111111', 2))


def firstSolu(numbers):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/77885/solution_groups?language=python3

        뭔가 이럴 것 같았음 ㅋㅋ
        왠지모르게 비트연산하면 쉽게 풀릴 것이라고 생각했었는데
        내가 비트연산에 대해 잘 몰라서 포기했었음..

        음... 저는 처음에 수를 이진법으로 바꾸고 일일이 확인하는 방식으로 작성하였는데 시간초과가 발생해서 질문하기에서 짝수와 홀수로 나누어서 접근하는 글을 보고 규칙성을 발견해서 풀었는데요. 이 코드를 처음 볼 땐 다른 접근 방식인 줄 알았는데, 가만 보니 if else 문으로 풀었던 제 코드가 결국 이거랑 같은 논리여서 혹시 도움이 될 분들이 있을까봐 나름의 해석을 올립니다.
        짝수를 이진수로 나타내면 무조건 끝의 자리는 0으로 끝나게 됩니다. 그러므로 짝수의 경우에는 비트 1~2개 차이가 나면 되니까, 해당 수에 1을 더하기만 하면 됩니다. 홀수의 경우에는 몇가지 수를 대입해서 확인해보시면 알겠지만, 결국에는 오른쪽에서부터 왼쪽으로 연속해서 1이 이어지다가 처음으로 0이 나온 위치를 파악하여, 해당 위치의 두칸 뒤의 자리까지 1로 채운 수 + 1만큼 더하면 됩니다. 예를 들어, 1001111이면, 1010111이 답이 되는데요.
        어차피 여기서 원래의 값에 (원래의 값 + 1)을 XOR 연산을 하면, 최초로 0이 나온 자리까지 1이 연속으로 된 숫자만 나오게 됩니다(그 이상은 무조건 같은 수니까 다 씹히고, 이하의 수는 1이 한 번만 등장하니까 1이 되어서).
        그런데 짝수는 무조건 오른쪽에서 첫번째 자리에서 처음으로 0이 나오니까 (val ^ (val + 1)) >> 2 값은 무조건 0으로 됩니다. 그러면 나머지 val + 1만 남게되어, 결국 제가 처음에 말한대로 짝수의 경우는 무조건 해당 수에 1을 더하기만 하는 규칙대로 나오게 됩니다.
        홀수의 경우는 원래의 값에서 + 1 한 숫자인 val + 1에, 처음으로 0이 나온 위치-2 한만큼까지 1이 연속된 수를 더하기만 하면 되는데요. 아까의 예시로 보았을 때 1001111과 1010111을 XOR 연산을 하면 11111이 나오는데 >> 2를 하면 111이 됩니다(0이 오른쪽에서 5번째에 등장하는데, 2를 빼니까 3번째까지 1이 연속된 숫자인 111이 나오는 것). 방금 더한 과정을 식으로 나타내면 (val ^ (val + 1)) >> 2이 되는 것입니다.

        대충 이런 원리라고 함..
        ㅋㅋㅋㅋ 나 몰라.. ㅋㅋ
    '''

    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val + 1)) >> 2) + val + 1)

    return answer