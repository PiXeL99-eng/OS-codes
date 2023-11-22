from typing import List
from collections import deque

class OS:

    def __init__(self, no_of_frames: int):

        self.no_of_frames = no_of_frames
        self.q = deque()
        self.hashed = set()

    def access_page(self, page: int):

        if page in self.hashed:
            # Page is present in frames

            return 'Hit', self.current_frames()
        else:
            if len(self.hashed) < self.no_of_frames:
                # Space is still available

                self.q.append(page)
                self.hashed.add(page)

                return 'Miss', self.current_frames()
            else:
                # Space is not available so we evict a frame

                evicted = self.q.popleft()
                self.hashed.remove(evicted)
                self.q.append(page)
                self.hashed.add(page)

                return 'Miss', self.current_frames()
            
    def current_frames(self):

        arr = []

        for i in self.q:
            arr.append(i)

        return arr

os = OS(no_of_frames=4)

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]

hit_count = 0
miss_count = 0

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


