# In SSTF (Shortest Seek Time First), requests having the shortest seek time are executed first. 
# So, the seek time of every request is calculated in advance in the queue and then they are scheduled according to their calculated seek time. 
# As a result, the request near the disk arm will get executed first.

def sstf(requests, head):

    start = head
    total = 0
    visited = set()
    seek_sequence = [start]

    for i in range(len(requests)):

        target = None
        diff = float('inf')

        for i in range(len(requests)):
            if i not in visited:
                if abs(requests[i] - start) < diff:
                    diff = abs(requests[i] - start)
                    target = i

        visited.add(target)
        seek_sequence.append(requests[target])
        total += abs(start - requests[target])
        start = requests[target]

    return total, seek_sequence

requests = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
head = 50

print()
print('Disk Requests: ', end='')
for i in range(len(requests)):

    if i == len(requests)-1:
        print(requests[i])
    else:
        print(requests[i], end=', ')

total_seek_ops, seek_sequence = sstf(requests, head)

print('Initial position of head:', head)
print('Total number of seek operations:', total_seek_ops)
print('Seek sequence is: ', end='')

for i in range(len(seek_sequence)):

    if i == len(seek_sequence)-1:
        print(seek_sequence[i], end='')
    else:
        print(seek_sequence[i], end=' -> ')

print('\n')