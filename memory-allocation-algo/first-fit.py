class Partition:
    # The memory partition class
    def __init__(self, size):
        self.size = size
        self.next = None

head = Partition(300)
tail = head

node = Partition(600)
tail.next = node
tail = tail.next

node = Partition(350)
tail.next = node
tail = tail.next

node = Partition(200)
tail.next = node
tail = tail.next

node = Partition(750)
tail.next = node
tail = tail.next

node = Partition(125)
tail.next = node
tail = tail.next

def first_fit(node, process_size):

    while node:
        if node.size >= process_size:
            node.size -= process_size
            return True
        
        node = node.next
        
    return False

def print_partitions(node):

    while node:

        print(node.size, 'KB', end='')

        if node.next != None:
            print(' -> ', end='')

        node = node.next

    print()


processes = [115, 500, 358, 200, 375]   # each of these are processes with size in KB

print('Incoming processes are:')

for i in processes:
    print(i, 'KB, ', end='')

print('\n')

print('Inital free memory partitions:')
print_partitions(head)

for i in range(len(processes)):

    print('-------------------------------------------------------------')

    print(f'Allocating memory for a {processes[i]} KB process')
    check = first_fit(head, processes[i])

    if check:
        print('✅ Successfully allocated memory to the process')
    else:
        print('❌ Could not allocate memory to the process')

    print('Memory partitions available are:')
    print_partitions(head)
    

