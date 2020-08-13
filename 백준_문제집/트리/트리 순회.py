import sys

n=int(input())
tree={}

#전위순회(뿌리=item -> 왼쪽자식=lchild -> 오른쪽자식=rchild)
def preorder(node):
    print(node.item,end='')
    if node.lchild!='.':
        preorder(tree[node.lchild])
    if node.rchild!='.':
        preorder(tree[node.rchild])

#중위순회(왼쪽자식=lchild -> 뿌리=item -> 오른쪽자식=rchild)
def inorder(node):
    if node.lchild!='.':
        inorder(tree[node.lchild])
    print(node.item,end='')
    if node.rchild!='.':
        inorder(tree[node.rchild])

#후위순회(왼쪽자식=lchild -> 오른쪽자식=rchild -> 뿌리=item)
def postorder(node):
    if node.lchild!='.':
        postorder(tree[node.lchild])
    if node.rchild!='.':
        postorder(tree[node.rchild])
    print(node.item,end='')

#node객체선언
class node:
    def __init__(self,item,lchild,rchild):
        self.item=item
        self.lchild=lchild
        self.rchild=rchild

#입력받은 이진트리 노드를 객체로 넣기
for i in range(n):
    data=input().split()
    tree[data[0]]=node(item=data[0],lchild=data[1],rchild=data[2])

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

