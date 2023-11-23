# Wait time of ith process = wt[i] =  ( at[i – 1] + wt[i – 1] + bt[i – 1] ) – at[i]
# Wait time = Current time - Arrival time
# Turnaround time = Completion time - Arrival Time
# Average Waiting Time of system = (sum of all waiting time)/(Number of processes)
# Average Turnaround Time of system = (sum of all turnaround time)/(Number of processes)

from heapq import heappop, heappush

def sjf(processes):

    h = []
    processes.sort()
    count_process = len(processes)

    time = 0
    ct = []
    wt = []
    tt = []

    sum_wt = 0
    sum_tt = 0

    cnt = 1
    heappush(h, (processes[0][1], processes[0][0]))

    while h:

        burst_time, arrival_time = heappop(h)

        if arrival_time > time:
            time = arrival_time

        wt.append(time - arrival_time)
        ct.append(time+burst_time)
        tt.append(time+burst_time-arrival_time)

        sum_wt += wt[-1]
        sum_tt += tt[-1]

        time+=burst_time

        while cnt < len(processes) and processes[cnt][0] <= time:
            heappush(h, (processes[cnt][1], processes[cnt][0]))
            cnt+=1

        if len(h) == 0 and cnt < len(processes):
            heappush(h, (processes[cnt][1], processes[cnt][0]))
            cnt+=1

    avg_wt = sum_wt/count_process
    avg_tt = sum_tt/count_process

    return ct, wt, tt, avg_wt, avg_tt

# process, arrival time, burst time, completion time, waiting time, turnaround time

processes = [[0, 4, 1], [1, 3, 2], [2, 1, 3], [3, 2, 4], [4, 5, 5]]    #[arrival time, burst time]................note added process id at end
ct, wt, tt, avg_wt, avg_tt = sjf(processes=processes)

print("Process ID\t Arrival Time\t Burst Time\t Completion Time\t Waiting Time\t Turnaround Time")
print('---------------------------------------------------------------------------------------------------------')

for i in range(len(processes)):
    print(f"P{i+1}\t\t {processes[i][0]} ms\t\t {processes[i][1]} ms\t\t {ct[i]} ms\t\t\t {wt[i]} ms\t\t {tt[i]} ms\n")

print('Average Waiting Time:', avg_wt)
print('Average Turnaround Time:', avg_tt)

print('\nGantt chart:\n')

for i in range(len(processes)):
    print(f'   P{i+1}   ', end='')

print('\n0______', end='')

for i in range(len(processes)):

    if i == len(processes)-1:
        print(f'{ct[i]}', end='')
    else:    
        print(f'{ct[i]}_______', end='')

print('\n')