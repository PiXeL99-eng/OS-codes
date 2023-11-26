# LOOK Algorithm is similar to the SCAN disk scheduling algorithm except for the difference 
# that the disk arm in spite of going to the end of the disk goes only to the last request to be serviced in front of the head and then 
# reverses its direction from there only. Thus it prevents the extra delay which occurred due to unnecessary traversal to the end of the disk.

def look(requests, head, direction):

    start = head
    total = 0

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

        for i in right:
            seek_sequence.append(i)
            total += abs(i - start)
            start = i

    else:

        for i in right:
            seek_sequence.append(i)
            total += abs(i - start)
            start = i

        for i in left[::-1]:
            seek_sequence.append(i)
            total += abs(i - start)
            start = i

    return total, seek_sequence

requests = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
head = 50
direction = 'right'
total_seek_ops, seek_sequence = look(requests, head, direction)

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