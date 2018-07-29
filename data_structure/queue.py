# coding:utf-8
class Queue(object):
    """队列"""
    def __init__(self):
        self.list = []
    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.list.append(item)
    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.list.pop(0)
    def is_empty(self):
        """判断一个队列是否为空"""
        return self.list == []
    def size(self):
        """返回队列的大小"""
        return len(self.list)

if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
