# C-LOOK is similar to the C-SCAN disk scheduling algorithm. In C-LOOK, the disk arm in spite of going to the end 
# goes only to the last request to be serviced in front of the head and then from there goes to the other end’s last request. 
# Thus, it also prevents the extra delay which occurred due to unnecessary traversal to the end of the disk.

def c_look(requests, head, direction):

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

        if len(right) != 0:

            seek_sequence.append(right[-1])
            total += abs(right[-1] - start)
            start = right[-1]

        if len(right) > 1:
            for i in right[:-1:-1]:
                seek_sequence.append(i)
                total += abs(i - start)
                start = i

    else:

        for i in right:
            seek_sequence.append(i)
            total += abs(i - start)
            start = i

        if len(left) != 0:

            seek_sequence.append(left[0])
            total += abs(left[0] - start)
            start = left[0]

        if len(left) > 1:
            for i in left[1:]:
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

total_seek_ops, seek_sequence = c_look(requests, head, direction)

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