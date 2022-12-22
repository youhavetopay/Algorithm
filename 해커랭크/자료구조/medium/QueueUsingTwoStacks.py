# Enter your code here. Read input from STDIN. Print output to STDOUT

def twoStackQueue(q_list):

    max_length = len(q_list)

    main_stack = [-1] * max_length
    main_stack_top = -1
    sub_stack = [-1] * max_length
    sub_stack_top = -1

    for query in q_list:

        if query[0] == '1':
            value = list(map(int, query.split(' ')))[1]
            main_stack_top += 1
            main_stack[main_stack_top] = value

        elif query[0] == '2':
            if sub_stack_top == -1:
                while main_stack_top > -1:
                    sub_stack_top += 1
                    sub_stack[sub_stack_top] = main_stack[main_stack_top]
                    main_stack_top -= 1
                
            sub_stack[sub_stack_top] = -1
            sub_stack_top -= 1

        else:
            if sub_stack_top == -1:
                print(main_stack[0])
            else:
                print(sub_stack[sub_stack_top])

        # print(main_stack, main_stack_top)
        # print(sub_stack, sub_stack_top)
        # print()
    return

# q_count = int(input())

# q_list = []

# for _ in range(q_count):
#     q_list.append(input())

q_list = [
    '1 42',
    '2',
    '1 14',
    '3',
    '1 28',
    '3',
    '1 60',
    '1 78',
    '2',
    '2'
    ]

twoStackQueue(q_list)