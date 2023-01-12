from graphviz import Digraph
class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

class BinTree:
    def __init__(self):
        self.root =  None
        self.last = None
        self.len = 0
    def insert(self , data):
        add = Node(data , Node)
        add.next = None
        if self.root == None:
            self.root = self.last = add
            self.len = self.len  + 1
        else:
            self.last.next = add
            self.last = add
            self.len = self.len + 1
    def getLeftChild(self , i):
        '''
            this function is aim to get left child of node of index  i
        :param i: index of node
        :return: parent of node index i
        '''
        return self.getNode(i * 2 + 1)
    def getRightChild(self , i):
        '''
            this function is aim to get right child of node of index  i
        :param i: index of node
        :return: parent of node index i
        '''
        return self.getNode((i + 1) * 2)
    def getParent(self , i):
        '''
            this function is aim to get node parent of i
        :param i: index of node
        :return: parent of node index i
        '''
        if i == 0 :
            return None
        return self.getNode( int(i / 2) )
    def getNode(self , i):
        '''
            this function is aim to get node of index i
        :param i: index of node
        :return: node of index i
        '''
        p = self.root
        while(i != 0):
            p = p.next
            i = i - 1
        return p
    def setNode(self , i , data):
        self.getNode(i).data = data

    def swap(self):
        '''
            Swap the values of the head node and tail node, and delete the tail node
        :return:
        '''
        if self.len !=0:
            p = self.root
            self.root.data = self.last.data
            while p.next != self.last:
                p = p.next
            p.next = None
            self.len = self.len - 1
            self.last = p


class Priority:
    def __init__(self):
        self.data = BinTree()

    def insert(self, data):
        self.data.insert(data) # insert data in to BTree
        self.adjustUp(data)

    def adjustUp(self , data):
        index = int((self.data.len - 1) / 2)
        k = self.data.len - 1
        while(index > 0 and data < self.data.getNode(index).data):
            self.data.setNode(k , self.data.getNode(index).data)
            k = index
            index = int((k - 1) / 2)

        self.data.setNode(k , data)

    def adjustDown(self, k , len):
        temp = self.data.getNode(0).data
        i = 2 * k + 1
        while i < self.data.len:
            if i < len - 1 and self.data.getNode(i).data > self.data.getNode(i + 1).data:
                i = i + 1
            if temp <= self.data.getNode(i).data :
                break
            else:
                self.data.setNode(k , self.data.getNode(i).data)
                k = i
            i = i * 2 + 1
        self.data.setNode(k , temp)

    def delMin(self):
        # Remove the first element, put the last element in the position of the first element, and then sink and adjust
        self.data.swap()
        self.adjustDown(0 , self.data.len)

    def showPriority(self , filename):
        dot = Digraph()
        # Add node
        p = self.data.root
        i = 0
        while p != None:
            dot.node(str(i) , str(p.data))
            p = p.next
            i = i + 1
        #Add Edge
        for i in range(0 , int(self.data.len / 2)):
            if (2 * i + 1) < self.data.len:
                dot.edge(str(i) , str(2 * i + 1)  )
            if (2 * i + 2) < self.data.len:
                dot.edge(str(i), str(2 * i + 2))
        dot.view(filename)

if __name__ == '__main__':
    priority = Priority()
    priority.insert(1)
    priority.insert(3)
    priority.insert(5)
    priority.insert(2)
    priority.insert(7)
    priority.insert(8)
    priority.insert(6)
    priority.showPriority("befor_tree.png")
    priority.delMin()
    priority.showPriority("after_del_tree.png")