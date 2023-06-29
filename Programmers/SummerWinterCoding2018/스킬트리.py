def solution(skill, skill_trees):

    '''
        나의 풀이
        정해진 스킬트리가 있을때
        주어지는 스킬트리가 가능한 건지 체크하는 문제

        나의 접근법
        스킬 개수가 많지 않고 주어지는 스킬트리의 개수도 적고
        스킬트리에 스킬이 중복되지 않는다고 했기 때문에 그냥 품 ㅋㅋ
        현재 체크하는 스킬트리의 스킬이 정해진 스킬트리에 포함된 스킬이라면
        현재 배워야 하는 스킬트리의 스킬과 비교해서 체크하는 방법으로 품

        꽤 쉬운 문제였는데
        answer의 초기값이 -1 였어서 왜 자꾸 틀리지? 이 생각함 ㅋㅋㅋㅋㅋㅋ 
    '''

    answer = 0

    for skill_tree in skill_trees:

        # 스킬트리 index 초기화
        skill_idx = 0

        for skill_name in skill_tree:

            # 현재 스킬이 스킬트리에 포함되어 있을 때
            if skill_idx < len(skill) and skill_name in skill:

                # 현재 배워야 하는 스킬인지 체크
                if skill_name == skill[skill_idx]:
                    skill_idx += 1
                else:
                    # 현재 배워야하는 스킬이 아닌 경우엔 끝내기
                    break
        else:
            answer += 1
                


    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))