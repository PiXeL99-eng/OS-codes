# FCFS is the simplest of all Disk Scheduling Algorithms. In FCFS, the requests are addressed in the order they arrive in the disk queue.

def fcfs(requests, head):

    start = head
    total = 0
    seek_sequence = [start]

    for i in requests:
        total += abs(start - i)
        start = i


    for i in requests:
        seek_sequence.append(i)

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

total_seek_ops, seek_sequence = fcfs(requests, head)

print('Initial position of head:', head)
print('Total number of seek operations:', total_seek_ops)
print('Seek sequence is: ', end='')

for i in range(len(seek_sequence)):

    if i == len(seek_sequence)-1:
        print(seek_sequence[i], end='')
    else:
        print(seek_sequence[i], end=' -> ')

print('\n')