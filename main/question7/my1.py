class TreeNode:
    data = None
    left_child = None
    right_child = None

def create_tree(front_ergodic,mid_ergodic):
    """
        根据前序遍历或中序遍历创建树
    :param font_ergodic: list or tuple
        前序遍历
    :param mid_ergodic: list or tuple
        中序遍历
    :return: 树
    """
    #检查输入是否错误
    if len(front_ergodic) != len(mid_ergodic):
        raise IndexError("遍历长度不匹配")
    for i in front_ergodic:
        if i not in mid_ergodic:
            raise LookupError("序列匹配错误")

    if len(front_ergodic) == 0 and len(mid_ergodic) == 0:
        return None

    head = front_ergodic[0]
    left_subtree = mid_ergodic[ : mid_ergodic.index(head)]
    right_subtree = mid_ergodic[mid_ergodic.index(head) + 1 :]

    node = TreeNode()
    node.data = head

    #左子树
    front_left_subtree = []
    for i in front_ergodic :
        if i not in left_subtree:
            break
        front_left_subtree.append(i)
    node.left_child = create_tree(front_left_subtree,left_subtree)

    #右子树
    right_start  = 0 if len(front_left_subtree) == 0 else front_ergodic.index(front_left_subtree[-1])
    front_right_subtree = front_ergodic[right_start + 1:]

    node.right_child = create_tree(front_right_subtree,right_subtree)

    return node

front_display_list = []
def front_display(head):
    """
    前序遍历
    :param head: TreeNode
        树的根节点
    :return list
        前序遍历的list
    """
    if head is None:
        return
    global front_display_list
    front_display_list.append(head.data)
    front_display(head.left_child)
    front_display(head.right_child)

    return front_display_list