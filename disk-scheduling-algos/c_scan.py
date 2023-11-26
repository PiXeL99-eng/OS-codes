# In the CSCAN algorithm in which the disk arm instead of reversing its direction goes to the other end of the disk and 
# starts servicing the requests from there. So, the disk arm moves in a circular fashion and 
# this algorithm is also similar to the SCAN algorithm hence it is known as C-SCAN (Circular SCAN).

def c_scan(requests, head, direction):

    start = head
    total = 0
    disk_end = 199

    left = []
    right = []
    seek_sequence = [start]

    for i in requests:
        if i<=start:
            left.append(i)
        else:
            right.append(i)

    left.sort()
    right.sort()

    if direction == 'left':
        for i in left[::-1]:
            seek_sequence.append(i)
            total += abs(i - start)
            start = i

        if seek_sequence[-1] != 0:
            total += abs(seek_sequence[-1])
            seek_sequence.append(0)
            start = 0

        seek_sequence.append(disk_end)
        start = disk_end
        total += abs(disk_end)

        for i in right[::-1]:
            seek_sequence.append(i)
            total += abs(i - start)
            start = i

    else:

        for i in right:
            seek_sequence.append(i)
            total += abs(i - start)
            start = i

        if seek_sequence[-1] != disk_end:
            total += abs(seek_sequence[-1] - disk_end)
            seek_sequence.append(disk_end)
            start = disk_end

        seek_sequence.append(0)
        start = 0
        total += abs(disk_end)

        for i in left:
            seek_sequence.append(i)
            total += abs(i - start)
            start = i

    return total, seek_sequence

requests = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
head = 50
direction = 'right'

print()
print('Disk Requests: ', end='')
for i in range(len(requests)):

    if i == len(requests)-1:
        print(requests[i])
    else:
        print(requests[i], end=', ')

total_seek_ops, seek_sequence = c_scan(requests, head, direction)

print('Initial position of head:', head)
print('Initial direction:', direction)
print('Total number of seek operations:', total_seek_ops)
print('Seek sequence is: ', end='')

for i in range(len(seek_sequence)):

    if i == len(seek_sequence)-1:
        print(seek_sequence[i], end='')
    else:
        print(seek_sequence[i], end=' -> ')

print('\n')