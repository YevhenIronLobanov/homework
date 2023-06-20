import pytest
from tree_tst import Tree

@pytest.fixture
def binary_tree():
    tree = Tree(5)
    tree.add_elements([3, 8, 2, 4, 7, 9])
    return tree

def test_insert(binary_tree):
    assert binary_tree.find_min() == 2
    assert binary_tree.find_max() == 9

def test_find_min(binary_tree):
    assert binary_tree.find_min() == 2

def test_find_max(binary_tree):
    assert binary_tree.find_max() == 9

def test_delete(binary_tree):
    binary_tree.delete(2)
    assert binary_tree.find_min() == 3

    binary_tree.delete(9)
    assert binary_tree.find_max() == 8