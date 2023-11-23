# Wait time of ith process = wt[i] =  ( at[i – 1] + wt[i – 1] + bt[i – 1] ) – at[i]
# Wait time = Current time - Arrival time
# Turnaround time = Completion time - Arrival Time
# Average Waiting Time of system = (sum of all waiting time)/(Number of processes)
# Average Turnaround Time of system = (sum of all turnaround time)/(Number of processes)

def fcfs(processes):

    processes.sort()
    count_process = len(processes)

    time = 0
    ct = []
    wt = []
    tt = []

    sum_wt = 0
    sum_tt = 0

    for arrival_time, burst_time in processes:
        ct.append(time+burst_time)
        wt.append(time-arrival_time)
        tt.append(time+burst_time-arrival_time)

        if arrival_time > time:
            time = arrival_time
            
        time+=burst_time

        sum_wt += wt[-1]
        sum_tt += tt[-1]

    avg_wt = sum_wt/count_process
    avg_tt = sum_tt/count_process

    return ct, wt, tt, avg_wt, avg_tt

# process, arrival time, burst time, completion time, waiting time, turnaround time

processes = [[4, 5], [0, 4], [1, 3], [3, 2], [2, 1]]    #[arrival time, burst time]
ct, wt, tt, avg_wt, avg_tt = fcfs(processes=processes)

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