from typing import List

class Node:
    def __init__(self, val, nextt=None, prev=None):
        self.val = val
        self.next=nextt
        self.prev = prev

class OS:

    def __init__(self, no_of_frames: int):

        self.no_of_frames = no_of_frames+2
        self.hashed = {}
        self.head = Node(-1)
        self.hashed[-1] = self.head
        self.tail = Node(-2)
        self.hashed[-2] = self.tail

        self.head.next = self.tail
        self.tail.prev = self.head

    def access_page(self, page: int):

        if page in self.hashed:
            # Page is present in frames

            node = self.hashed[page]

            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.head.next
            self.head.next.prev = node

            self.head.next = node
            node.prev = self.head

            return 'Hit', self.current_frames()
        else:
            if len(self.hashed) < self.no_of_frames:
                # Space is still available
                node = Node(page)
                self.hashed[page] = node

                node.next = self.head.next
                self.head.next.prev = node

                self.head.next = node
                node.prev = self.head

                return 'Miss', self.current_frames()
            else:
                # Space is not available so we evict a frame

                lru_node = self.tail.prev
                self.tail.prev = lru_node.prev
                lru_node.prev.next = self.tail
                lru_node.next = None
                lru_node.prev = None
                self.hashed.pop(lru_node.val)
                del lru_node

                node = Node(page)
                self.hashed[page] = node

                node.next = self.head.next
                self.head.next.prev = node

                self.head.next = node
                node.prev = self.head

                return 'Miss', self.current_frames()
            
    def current_frames(self):

        arr = []

        node = self.head.next

        while node != self.tail:
            arr.append(node.val)
            node = node.next

        return arr

no_of_frames = 4
os = OS(no_of_frames)

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]

hit_count = 0
miss_count = 0

print('No of frames in CPU:', no_of_frames)
print('Pages requested:', pages)
print('-------------------------------------------------------------')

for p in pages:

    hit_or_miss, frames = os.access_page(page=p)

    print(f'{p} was accessed. Status: {hit_or_miss}')
    print(f'Current frames in CPU: {frames}')
    print('-------------------------------------------------------------')

    if hit_or_miss == 'Hit':
        hit_count+=1
    else:
        miss_count+=1

print('Total Hit count:', hit_count)
print('Total Miss count:', miss_count)


