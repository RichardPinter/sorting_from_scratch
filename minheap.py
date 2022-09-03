# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:

    id1 = 0
    id2 = 0

    def __init__(self, array,color):
        # Do not edit the line below.
        print('this is array',array)
        self.heap = self.buildHeap(array,color)
        self.color = color

    def buildHeap(self, array,color):
        firstParent = (len(array) - 1) // 2
        for element in reversed(range(firstParent + 1)):
            print('SiftDown', element,len(array)-1)
            self.siftDown(element, len(array) - 1, array,color)
        return array

    def siftDown(self, index, last_index, heap,color):
        childNodeOne = index * 2 + 1
        print('ChildNodeOne index',childNodeOne, 'Last Index',last_index)
        while childNodeOne <= last_index:

            childIndexTwo = index * 2 + 2 if index * 2 + 2 <= last_index else -1
            if childIndexTwo != -1 and heap[childIndexTwo] < heap[childNodeOne]:
                idxToSwap = childIndexTwo
                print('compare child nodes', heap[childIndexTwo],heap[childNodeOne])
            else:
                idxToSwap = childNodeOne
                print('swap', heap[idxToSwap])
            if heap[idxToSwap] < heap[index]:
                self.swap(index, idxToSwap, heap,color)
                index = idxToSwap
                childNodeOne = index * 2 + 1
                if  childNodeOne <= last_index:
                    print('update node', heap[childNodeOne])
            else:
                break

    def siftUp(self, index, heap):
        parent = (index - 1) // 2
        while parent > 0 and heap[index] < heap[parent]:
            self.swap(index, parent, heap)
            index = parent
            parent = (index - 1) // 2
        return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap,self.color)
        value = self.heap.pop(-1)
        self.color.pop(-1)
        print(len(self.color),'pop')
        self.siftDown(0, len(self.heap) - 1, self.heap,self.color)
        return value

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
        return

    def swap(self, index1, index2, heap,color):
        print('Swapping the following', heap[index1], heap[index2])
        heap[index1], heap[index2] = heap[index2], heap[index1]
        m = len(color)
        color = ['red'] * m
        color[index1]='blue'
        self.id1 = index1
        self.id2 = index2
        return
