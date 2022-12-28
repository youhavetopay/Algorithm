def largestRectangle(h):
    # Write your code here

    stack = [-1]
    max_area = 0
    for i, height in enumerate(h):
        while stack[-1] != -1 and h[stack[-1]] >= h[i]:
            now_height = h[stack.pop()]
            now_width = i - stack[-1] - 1
            max_area = max(max_area, now_height * now_width)
        stack.append(i)
    
    h_length = len(h)

    while stack[-1] != -1:
        now_height = h[stack.pop()]
        now_width = h_length - stack[-1] - 1
        max_area = max(max_area, now_height * now_width)
                    
    return max_area

print(largestRectangle(list(map(int, '1 2 3 4 5'.split(' ')))))