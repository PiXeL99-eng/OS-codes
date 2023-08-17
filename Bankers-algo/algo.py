# Banker's algo is a Deadlock avoidance algo, also used for Deadlock detection in a system.

class OS:

    def __init__(self, avail: int):

        self.count = len(avail)
        self.avail = avail

    @staticmethod
    def can_be_executed(free, need):

        for i in range(len(free)):
            if need[i] > free[i]:
                return False
            
        return True

    def bankers_algo(self, allocated, maxx_need):

        safe_order = []
        processes = len(allocated)
        executed = [False for i in range(processes)]
        total_executed = 0

        while total_executed<processes:

            change = False

            for i in range(processes):

                if executed[i] == False:

                    need = [maxx_need[i][j] - allocated[i][j] for j in range(self.count)]

                    if self.can_be_executed(self.avail, need):
                        self.avail[:] = [self.avail[j] + allocated[i][j] for j in range(self.count)]
                        executed[i] = True
                        safe_order.append(i)
                        total_executed+=1
                        change = True

            if change == False:
                return False, []

        return True, safe_order


os = OS([3, 3, 2])

allocated = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
        ]

maxx_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
       ]

is_safe, sequence = os.bankers_algo(allocated=allocated, maxx_need=maxx_need)

if is_safe:
    print('Sequence is safe.')
    seq = []

    for i in sequence:
        seq.append('P' + str(i))

    print('Process order is: ' + " -> ".join(seq))
else:
    print('Process is not safe. Deadlock exists.')
    


