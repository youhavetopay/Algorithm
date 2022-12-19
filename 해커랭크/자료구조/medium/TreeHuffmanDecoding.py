def decodeHuff(root, s):
	#Enter Your Code Here

    decoding_word = ''

    now_index = 0
    s_length = len(s)
    
    while now_index < s_length:
        word_data, now_index = findWord(root, s, now_index)

        decoding_word += word_data


    print(decoding_word)


def findWord(node, s, pre_index):

    data = node.data
    now_index = pre_index

    if now_index < len(s):
        if s[now_index] == '0':
            if node.left:
                data, now_index = findWord(node.left, s, now_index + 1)
            else:
                return data, now_index
                
        elif s[now_index] == '1':
            if node.right:
                data, now_index = findWord(node.right, s, now_index + 1)
            else:
                return data, now_index

    return data, now_index
