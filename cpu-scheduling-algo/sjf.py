# Wait time =  The time for which process was in ready queue, but was not executing
# Arrival time = The time when the process arrived in the ready queue
# Completion time = The time when the process got completed
# Turnaround time = Time passed from when the process arrived till it got completed
# Burst time = The amount of cpu execution time that the process needs 
# Average Waiting Time of system = (sum of all waiting time)/(Number of processes)
# Average Turnaround Time of system = (sum of all turnaround time)/(Number of processes)

from heapq import heappop, heappush

def sjf(processes):

    h = []
    processes.sort()
    count_process = len(processes)
    output = []

    time = 0

    sum_wt = 0
    sum_tt = 0

    cnt = 1
    heappush(h, (processes[0][1], processes[0][0], processes[0][2]))    # (burst time, arrival time, processID)

    while h:

        burst_time, arrival_time, pid = heappop(h)

        if arrival_time > time:
            time = arrival_time

        wt = time - arrival_time
        ct = time + burst_time
        tt = time + burst_time - arrival_time

        output.append([pid, arrival_time, burst_time, ct, wt, tt])

        sum_wt += wt
        sum_tt += tt

        time += burst_time

        while cnt < len(processes) and processes[cnt][0] <= time:
            heappush(h, (processes[cnt][1], processes[cnt][0], processes[cnt][2]))
            cnt+=1

        if len(h) == 0 and cnt < len(processes):
            heappush(h, (processes[cnt][1], processes[cnt][0], processes[cnt][2]))
            cnt+=1

    avg_wt = sum_wt/count_process
    avg_tt = sum_tt/count_process

    return output, avg_wt, avg_tt

# process, arrival time, burst time, completion time, waiting time, turnaround time

processes = [[2, 6, 1], [5, 2, 2], [1, 8, 3], [0, 3, 4], [4, 4, 5]]    # [arrival time, burst time, processID]
output, avg_wt, avg_tt = sjf(processes=processes)

print("Process ID\t Arrival Time\t Burst Time\t Completion Time\t Waiting Time\t Turnaround Time")
print('---------------------------------------------------------------------------------------------------------')

for i in range(len(processes)):
    print(f"P{output[i][0]}\t\t {output[i][1]} ms\t\t {output[i][2]} ms\t\t {output[i][3]} ms\t\t\t {output[i][4]} ms\t\t {output[i][5]} ms\n")

print('Average Waiting Time:', avg_wt)
print('Average Turnaround Time:', avg_tt)

print('\nGantt chart:')

print('\n0_____', end='')

for i in range(len(processes)):

    if i == len(processes)-1:
        print(f'P{output[i][0]}_____{output[i][3]}', end='')
    else:    
        print(f'P{output[i][0]}_____{output[i][3]}_____', end='')

print('\n')