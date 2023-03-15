# 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 길 찾기 게임


import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, x: int, y: int, number: int) -> None:
        self.number = number
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def set_left(self, left: object) -> None:
        self.left = left

    def set_right(self, right: object) -> None:
        self.right = right


class Tree:
    def __init__(self, root) -> None:
        self.root = root

    def insert(self, node: object) -> None:
        temp_node = self.root
        while True:
            if temp_node.x < node.x:
                if temp_node.right != None:
                    temp_node = temp_node.right
                    continue

                temp_node.set_right(node)
                return
            else:
                if temp_node.left != None:
                    temp_node = temp_node.left
                    continue

                temp_node.set_left(node)
                return


def pretraversal(node: Node, answer: list) -> None:
    answer.append(node.number)

    if node.left != None:
        pretraversal(node.left, answer)

    if node.right != None:
        pretraversal(node.right, answer)

    return


def posttraversal(node: Node, answer: list) -> None:
    if node.left != None:
        posttraversal(node.left, answer)

    if node.right != None:
        posttraversal(node.right, answer)

    answer.append(node.number)

    return


def solution(nodeinfo: list):
    preanswer = []
    postanswer = []

    for i in range((len(nodeinfo))):
        nodeinfo[i].append(i + 1)

    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    root = Node(*nodeinfo[0])
    tree = Tree(root)

    for index in range(1, len(nodeinfo)):
        node = Node(*nodeinfo[index])
        tree.insert(node)

    pretraversal(tree.root, preanswer)
    posttraversal(tree.root, postanswer)

    return [preanswer, postanswer]
