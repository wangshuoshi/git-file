# coding:utf-8
class Stack(object):
    """栈"""
    def __init__(self):
        self.list = []
    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.list.append(item)
    def pop(self):
        """弹出栈顶元素"""
        return self.list.pop()
    def peek(self):
        """返回栈顶元素"""
        if self.list:
            return self.list[-1]
        else:
            return None
    def is_empty(self):
        """判断栈是否为空"""
        return self.list == []
        # return not self.list
    def size(self):
        """返回栈的元素个数"""
        return len(self.list)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

