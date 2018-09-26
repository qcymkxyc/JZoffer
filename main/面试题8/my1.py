class TreeNode:
    """
        树的节点
    """
    data = None

    parent = None
    left_child = None
    right_child = None


def create_tree(front_ergodic,mid_ergodic,parent_node = None):
    """
        根据前序遍历和中序遍历创建树
    :param front_ergodic: list or tuple
        前序遍历的顺序
    :param mid_ergodic: list or tuple
        中序遍历的顺序
    :param parent_node : TreeNode or None,default None
        父节点，None表示没有父节点，即根节点
    :return: TreeNode
        根节点
    """
    #边缘检测
    if set(front_ergodic) != set(mid_ergodic):
        print(front_ergodic)
        print(mid_ergodic)
        raise ValueError("元素不匹配")

    if len(front_ergodic) == len(mid_ergodic) == 0:
        return None

    current_data = front_ergodic[0]
    #获取左右子树的前序和中序遍历节点
    left_mid_nodes = mid_ergodic[ : mid_ergodic.index(current_data)]
    right_mid_nodes = mid_ergodic[mid_ergodic.index(current_data) + 1 :]
    left_front_nodes = front_ergodic[1: len(left_mid_nodes) + 1]
    right_front_nodes = (front_ergodic[1:] if len(left_front_nodes) == 0
                         else front_ergodic[front_ergodic.index(left_front_nodes[-1]) + 1:])

    #创建当前节点
    current_node = TreeNode()
    current_node.data = current_data
    current_node.parent = parent_node

    #创建左子树
    current_node.left_child = create_tree(left_front_nodes,left_mid_nodes,current_node)
    #创建右子树
    current_node.right_child = create_tree(right_front_nodes,right_mid_nodes,current_node)

    return  current_node

front_display_list = list()
def front_display(current_node):
    """
        前序遍历
    :param current_node:TreeNode or None
        当前节点，None表示空节点
    :return:list
        前序遍历序列
    """
    if not current_node:
        return
    global front_display_list
    front_display_list.append(current_node.data)

    #遍历左右子树
    front_display(current_node.left_child)
    front_display(current_node.right_child)

    return front_display_list



def find_mid_next(current_node):
    """
    查找中序遍历的下一个节点

    通常情况下分几种情况：
        1. 该节点为叶子节点
            1.1 左叶子节点：
                此情况下一个节点就是他的父节点
            1.2 右叶子节点
                这种情况较为麻烦，因为父节点已经访问过了，这种情况下就
                要不断的往上迭代，直到子节点为父节点的左节点，如若找不到左节点，则其为最后一个
        2. 该节点不为叶子节点
            2.1 仅有左子树：
                2.1.1 该节点为父节点的左节点
                    同左叶子节点的情况，下一个就是父节点
                2.1.2 该节点为父节点的右节点
                    同右叶子节点的情况
            2.2 仅有右子树
                下一个即为右子树的最左叶子节点
            2.3 左右均有
                同仅有右子树
    :param current_node:TreeNode
        当前节点
    :return: TreeNode or None
        如果有下一个节点则返回TreeNode,否则返回None
    """
    if (not isinstance(current_node,TreeNode)):
        raise TypeError("节点类型错误")
    if not current_node:
        pass
        # raise N

    #叶子节点的情况
    if current_node.left_child is None and current_node.right_child is None:
        #左叶子节点的情况
        if current_node.parent.left_child == current_node:
            return current_node.parent
        #右叶子节点的情况
        else:
            parent_node = current_node.parent
            temp_node = current_node
            while(parent_node != None):
                if parent_node.left_child == temp_node:
                    return parent_node
                temp_node = parent_node
                parent_node = parent_node.parent
            #如果为最后一个,则返回None
            return parent_node

    #非叶子节点
    else:
        #仅有左子树
        if current_node.right_child is None:
            #父节点的左节点为当前节点
            if current_node.parent.left_child == current_node:
                return current_node.parent
            #父节点的右节点为当前节点
            else:
                parent_node = current_node.parent
                temp_node = current_node
                while (parent_node != None):
                    if parent_node.left_child == temp_node:
                        return parent_node
                    temp_node = parent_node
                    parent_node = parent_node.parent
                # 如果为最后一个,则返回None
                return parent_node


        #仅有右子树和左右子树均有的情况
        else:
            right_root_node = current_node.right_child
            left_child_node = right_root_node
            #查找右子树的最左节点
            while left_child_node.left_child:
                left_child_node = left_child_node.left_child
            return left_child_node

