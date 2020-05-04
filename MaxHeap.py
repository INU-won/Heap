# 최대 힙
class Heap:
    def __init__(self, num):
        self.heap_list = list()
        self.heap_list.append(None)
        self.heap_list.append(num)

    def switch(self, num_index):
        if num_index == 1:
            return False  # root node 일때

        parent_index = num_index // 2
        if self.heap_list[num_index] > self.heap_list[parent_index]:
            return True

        return False

    # 데이터 삽입

    def insert(self, num):
        if len(self.heap_list) == 0:
            self.heap_array.append(None)
            self.heap_list.append(num)
            return True
        self.heap_list.append(num)

        # 추가한 num이 부모 노드보다 크면 자리바꾸기 위한 코드
        num_index = len(self.heap_list) - 1

        while self.switch(num_index):
            parent_index = num_index // 2
            self.heap_list[num_index], self.heap_list[parent_index] \
                = self.heap_list[parent_index], self.heap_list[num_index]
            num_index = parent_index
        return True