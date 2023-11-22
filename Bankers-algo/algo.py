# Banker's algo is a Deadlock avoidance algo, also used for Deadlock detection in a system.
# Safety algo checks if a process is safe to be executed.

class OS:

    def __init__(self, available, allocated, max_need):

        self.count_resources = len(available)
        self.count_processes = len(allocated)
        self.available = available
        self.allocated = allocated
        self.max_need = max_need
        self.finished = [False for i in range(self.count_processes)]
    
    def safety_algo(self, pid):

        for i in range(self.count_resources):
            if self.max_need[pid][i] - self.allocated[pid][i] > self.available[i]:
                return False    # process is not safe to execute now
            
        return True     # process is safe to execute now
    
    def release_resources(self, pid):
        for i in range(self.count_resources):
            self.available[i]+=self.allocated[pid][i]   #resources that were allocated got released
            self.allocated[pid][i] = 0
            self.max_need[pid][i] = 0

    def print_state(self, pid):
        print('------------------------------------------------------------')
        print(f'✔ Process # {pid} executed and resources freed')
        print('Current Available Resources')
        print(self.available)
        print('Current Allocated Resources')
        print(self.allocated)
        print('Max Need of Processes')
        print(self.max_need)

    def bankers_algo(self):

        sequence = []

        while True:

            ran = False
            for pid in range(self.count_processes):
                if self.finished[pid] == False and self.safety_algo(pid):
                    self.finished[pid] = True
                    sequence.append(pid+1)
                    self.release_resources(pid)
                    ran = True
                    self.print_state(pid+1)

            if len(sequence) == self.count_processes:
                return True, sequence
            
            if ran == False:
                return False, sequence

# available[NUMBER OF RESOURCES] => no of available resources of each type
available = [3, 3, 2] 

# max_need[NUMBER OF PROCESSES][NUMBER OF RESOURCES] => maximum need of each type of resource for each process
max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
       ]

# allocated[NUMBER OF PROCESSES][NUMBER OF RESOURCES] => number of resources of each type currently allocated to each process
allocated = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
        ]

print('Current Available Resources')
print(available)
print('Current Allocated Resources')
print(allocated)
print('Max Need of Processes')
print(max_need)

os = OS(available = available, allocated = allocated, max_need = max_need)

is_safe, sequence = os.bankers_algo()


print('------------------------------------------------------------')

if is_safe:
    print('Safe sequence exists')
    seq = []

    for i in sequence:
        seq.append('P' + str(i))

    print('Process execution order is: ' + " -> ".join(seq))
else:
    print('Safe sequence does not exist. Deadlock may occur.')