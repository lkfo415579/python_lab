
class TreeNode:
    Key = 0
    Left = None
    Right = None

    def __init__(self, key):
        self.Key = key


def create_new_node(key):
    # case 1 left and right is empty, choose left
    # case 2 only right is empty, choose right
    return TreeNode(key)


def complete_adding(root, num):
    if num == 0:
        return
    global global_key
    global_key += 1
    root.Left = create_new_node(global_key)
    global_key += 1
    root.Right = create_new_node(global_key)
    complete_adding(root.Left, num - 1)
    complete_adding(root.Right, num - 1)


def display_tree(root):
    left_K = -1
    right_K = -1
    if root.Left is not None:
        left_K = root.Left.Key
    if root.Right is not None:
        right_K = root.Right.Key
    if left_K == -1 and right_K == -1:
        return
    print "root:%d,left:%d,right:%d" % (root.Key, left_K, right_K)
    if left_K != -1:
        display_tree(root.Left)
    if right_K != -1:
        display_tree(root.Right)


def find_node(root, target_key, level=0):
    if root is None:
        return -1
    if root.Key == target_key:
        return (root, level)
    # case left has no target_key
    result = find_node(root.Left, target_key, level + 1)
    if result == -1:
        return find_node(root.Right, target_key, level + 1)
    else:
        return result


def find_lca(root, n1, n2):
    if root is None:
        return None
    if root.Key == n1 or root.Key == n2:
        return root
    found_left = find_lca(root.Left, n1, n2)
    found_right = find_lca(root.Right, n1, n2)
    # case 1 they are in both side.
    if found_left and found_right:
        return root
    # case 2 they are in the same side.
    if found_right is None:
        # in left side
        return found_left
    elif found_left is None:
        # in right side
        return found_right


def distance(root, n1, n2):
    _, n1_level = find_node(root, n1)
    _, n2_level = find_node(root, n2)
    lca = find_lca(root, n1, n2)
    _, lca_level = find_node(root, lca.Key)
    return n1_level + n2_level - 2 * lca_level


global_key = 0
root = TreeNode(0)
# root.Left = create_new_node(1)
# root.Right = create_new_node(2)
complete_adding(root, 3)
display_tree(root)
print "---"
target, level = find_node(root, 10)
print "LEVEL:", level
print "KEY:", target.Key
print "Removed its left!"
target.Left = None
target.Right.Right = create_new_node(15)
display_tree(root)
print "---"
lca = find_lca(root, 15, 7)
print "TEST LCA:", lca.Key
print "---"
n1 = 8
n2 = 7
dis = distance(root, n1, n2)
print "Distance between %d, %d : %d" % (n1, n2, dis)
