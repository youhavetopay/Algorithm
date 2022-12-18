def has_cycle(head):

    nodes = []

    pointer = head
    nodes.append(pointer)

    while pointer:
        pointer = pointer.next
        if pointer in nodes:
            break
        nodes.append(pointer)

    
    if pointer:
        return 1
    
    return 0