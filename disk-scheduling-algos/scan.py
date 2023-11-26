# In the SCAN algorithm the disk arm moves in a particular direction and services the requests coming in its path and
# after reaching the end of the disk, it reverses its direction and again services the request arriving in its path. 
# So, this algorithm works as an elevator and is hence also known as an elevator algorithm.

def scan(requests, head, direction):

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

        for i in right:
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

        for i in left[::-1]:
            seek_sequence.append(i)
            total += abs(i - start)
            start = i

    return total, seek_sequence

requests = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
head = 50
direction = 'left'
total_seek_ops, seek_sequence = scan(requests, head, direction)

print('\n')
print('Initial position of head:', head)
print('Total number of seek operations:', total_seek_ops)
print('Seek sequence is: ', end='')

for i in range(len(seek_sequence)):

    if i == len(seek_sequence)-1:
        print(seek_sequence[i], end='')
    else:
        print(seek_sequence[i], end=' -> ')

print('\n')