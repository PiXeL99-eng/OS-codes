from typing import List

class OS:

    def __init__(self, no_of_frames: int):

        self.no_of_frames = no_of_frames
        self.frames = set()

    def access_page(self, index: int, reference_string: List[int]):

        page = reference_string[index]

        if page in self.frames:
            # Page is present in frames
            return 'Hit', self.frames
        else:
            if len(self.frames) < self.no_of_frames:
                # Space is still available
                self.frames.add(page)
                return 'Miss', self.frames
            else:
                # Space is not available so we evict a frame
                farthest_frame = self.search(index, reference_string)
                self.frames.remove(farthest_frame)
                self.frames.add(page)
                # The farthest accessed frame is evicted and new page is stored

                return 'Miss', self.frames
            
    def search(self, index: int, reference_string: List[int]):

        if len(self.frames) == 1:
            for i in self.frames:
                return i

        temp = set([i for i in self.frames])

        for page in reference_string[index+1:]:

            if page in temp:
                temp.remove(page)

            if len(temp) == 1:
                return temp.pop()
            
        return temp.pop()

os = OS(no_of_frames=3)

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]

hit_count = 0
miss_count = 0

for i in range(len(pages)):

    hit_or_miss, frames = os.access_page(index=i, reference_string=pages)

    print(f'{pages[i]} was accessed. Status: {hit_or_miss}')
    print(f'Current frames in CPU: {frames}')
    print('-------------------------------------------------------------')

    if hit_or_miss == 'Hit':
        hit_count+=1
    else:
        miss_count+=1

print('Total Hit count:', hit_count)
print('Total Miss count:', miss_count)


