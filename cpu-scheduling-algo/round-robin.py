# Wait time =  The time for which process was in ready queue, but was not executing
# Arrival time = The time when the process arrived in the ready queue
# Completion time = The time when the process got completed
# Turnaround time = Time passed from when the process arrived till it got completed
# Burst time = The amount of cpu execution time that the process needs 
# Average Waiting Time of system = (sum of all waiting time)/(Number of processes)
# Average Turnaround Time of system = (sum of all turnaround time)/(Number of processes)

from collections import deque

def rr(processes):

    q = deque()
    processes.sort()
    count_process = len(processes)
    output = []
    gantt_chart = [] # (pid, start, end)

    quantum = 2

    time = 0

    sum_wt = 0
    sum_tt = 0

    cnt = 1
    q.append((processes[0][0], processes[0][1], processes[0][1], processes[0][2]))    # (arrival time, burst time, rem burst time, processID)

    while q:

        arrival_time, burst_time, rem_burst_time, pid = q.popleft()

        if arrival_time > time:
            time = arrival_time

        if rem_burst_time <= quantum:

            ct = time + rem_burst_time
            tt = ct - arrival_time
            wt = tt - burst_time

            output.append([pid, arrival_time, burst_time, ct, wt, tt])

            sum_wt += wt
            sum_tt += tt

            time+=rem_burst_time
            gantt_chart.append((pid, time))

            if len(q) == 0 and cnt < len(processes):
                q.append((processes[cnt][0], processes[cnt][1], processes[cnt][1], processes[cnt][2]))
                cnt+=1
        else:

            time += quantum
            gantt_chart.append((pid, time))
            
            while cnt < len(processes) and processes[cnt][0] <= time:
                q.append((processes[cnt][0], processes[cnt][1], processes[cnt][1], processes[cnt][2]))
                cnt+=1

            q.append((arrival_time, burst_time, rem_burst_time-quantum, pid))


    avg_wt = sum_wt/count_process
    avg_tt = sum_tt/count_process

    return output, gantt_chart, avg_wt, avg_tt

# process, arrival time, burst time, completion time, waiting time, turnaround time

processes = [[0, 5, 1], [1, 4, 2], [2, 2, 3], [4, 1, 4]]    # [arrival time, burst time, processID]
output, gantt_chart, avg_wt, avg_tt = rr(processes=processes)

print("Process ID\t Arrival Time\t Burst Time\t Completion Time\t Waiting Time\t Turnaround Time")
print('---------------------------------------------------------------------------------------------------------')

for i in range(len(processes)):
    print(f"P{output[i][0]}\t\t {output[i][1]} ms\t\t {output[i][2]} ms\t\t {output[i][3]} ms\t\t\t {output[i][4]} ms\t\t {output[i][5]} ms\n")

print('Average Waiting Time:', avg_wt)
print('Average Turnaround Time:', avg_tt)

print('\nGantt chart:')

print('\n0_____', end='')

for i in range(len(gantt_chart)):

    print(f'P{gantt_chart[i][0]}_____{gantt_chart[i][1]}', end='')
    if i != len(gantt_chart)-1:
        print('_____', end='')

print('\n')