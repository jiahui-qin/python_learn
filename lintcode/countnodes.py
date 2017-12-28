def countnodes(self, root):
    num = 0
    a = root
    while a:
        num = num + 1
        a = a.next
    return num