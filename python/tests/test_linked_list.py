import pytest 
from linked_list.linked_list import LinkedList, Node


def test_import():
    node = Node ('apples, none')
    actual = node.value
    expected = 'apples'
    assert actual == expected
    assert node.next == None
    # assert LinkedList

# def test_two_nodes():
#     node2 = Node('orange', None)
#     node1 = Node('apples', node2)

#     actual = node1.next.value
#     expected = 'orange'
#     assert actual == expected

# def test_empty_11():
#     11 = LinkedList()
#     assert 11