from sys import stdin

n = int(stdin.readline())
tree = {}

for _ in range(n):
    c, l, r = map(str, stdin.readline().split())
    tree[c] = [l, r]

#전위 순회: c->l->r
def preorder(c):
    if c=='.':
        return ''
    else:
        l = tree[c][0]
        r = tree[c][1]
        print(c, end='')
        preorder(l)
        preorder(r)
        
#중위 순회: l->c->r
def inorder(c):
    if c=='.':
        return ''
    else:
        l = tree[c][0]
        r = tree[c][1] 
        inorder(l)
        print(c, end='')
        inorder(r)

#후위 순회: l->r->c
def postorder(c):
    if c=='.':
        return ''
    else:
        l = tree[c][0]
        r = tree[c][1]
        postorder(l)
        postorder(r)
        print(c, end='')
        
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
   