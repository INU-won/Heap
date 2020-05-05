# 힙 클래스 구현
class Heap:
    def __init__(self, num):
        self.heap_list = list()
        self.heap_list.append(None) # root node의 인덱스를 1로 하기 위함
        self.heap_list.append(num)

    def switch(self, num_index):
        if num_index == 1:
            return False # root node 일때

        parent_index = num_index // 2
        if self.heap_list[num_index] > self.heap_list[parent_index]:
            return True

        return False

    def switch_child(self, switch_index): # 자식 노드와 비교하여 작으면 자리 바꾸기 위함
        left_child_index = switch_index * 2
        right_child_index = switch_index * 2 + 1

        # 왼쪽 차일드 노드가 없을 때
        if left_child_index >= len(self.heap_list):
            return False

        # 왼쪽 차일드 노드만 있을 때
        elif right_child_index >= len(self.heap_list):
            if self.heap_list[switch_index] < self.heap_list[left_child_index]:
                return True
            else:
                return False

        #왼쪽 오른쪽 모두 있을 때
        else:
            if self.heap_list[left_child_index] > self.heap_list[right_child_index]:
                if self.heap_list[switch_index] < self.heap_list[left_child_index]:
                    return True
                else:
                    return False
            else:
                if self.heap_list[switch_index] < self.heap_list[right_child_index]:
                    return True
                else:
                    return False

    # 데이터 삽입
    def insert(self, num):
        if len(self.heap_list) == 0:
            self.heap_array.append(None)
            self.heap_list.append(num)
            return True
        self.heap_list.append(num)

        #추가한 num이 부모 노드보다 크면 자리바꾸기 위한 코드
        num_index = len(self.heap_list) - 1

        while self.switch(num_index):
            parent_index = num_index // 2
            self.heap_list[num_index], self.heap_list[parent_index]\
            = self.heap_list[parent_index], self.heap_list[num_index]
            num_index = parent_index
        return True

    # 데이터 삭제
    def delete_new(self):
        if len(self.heap_list) <= 1:
            return None

        pop_num = self.heap_list[1] # root node 출력
        self.heap_list[1] = self.heap_list[-1] # root node에 가장 마지막 데이터 바꿔 줌
        del self.heap_list[-1]
        switch_index = 1

        while self.switch_child(switch_index):
            left_child_index = switch_index * 2
            right_child_index = switch_index * 2 + 1

            # 왼쪽 차일드 노드만 있을 때
            if right_child_index >= len(self.heap_list):
                if self.heap_list[switch_index] < self.heap_list[left_child_index]:
                    self.heap_list[switch_index], self.heap_list[left_child_index]\
                    = self.heap_list[left_child_index], self.heap_list[switch_index]
                    switch_index = left_child_index

            #왼쪽 오른쪽 모두 있을 때
            else:
                if self.heap_list[left_child_index] > self.heap_list[right_child_index]:
                    if self.heap_list[switch_index] < self.heap_list[left_child_index]:
                        self.heap_list[switch_index], self.heap_list[left_child_index]\
                        = self.heap_list[left_child_index], self.heap_list[switch_index]
                        switch_index = left_child_index
                else:
                    if self.heap_list[switch_index] < self.heap_list[right_child_index]:
                        self.heap_list[switch_index], self.heap_list[right_child_index]\
                        = self.heap_list[right_child_index], self.heap_list[switch_index]
                        switch_index = right_child_index

        return pop_num