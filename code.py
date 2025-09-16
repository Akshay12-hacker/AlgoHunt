def main():
    n = int(input("Enter the total number of processes: "))
    
    at = [0] * n
    bt = [0] * n
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n
    sum_time = 0
    totaltat = 0
    totalwt = 0
    
    print("\nEnter the arrival time and burst time of each Process")
    for i in range(n):
        at[i] = int(input(f"Enter arrival time of process[{i + 1}]: "))
        bt[i] = int(input(f"Enter burst time of process[{i + 1}]: "))
    
    sum_time = at[0]
    for j in range(n):
        sum_time += bt[j]
        ct[j] = sum_time
        
    for k in range(n):
        tat[k] = ct[k] - at[k]
        wt[k] = tat[k] - bt[k]
        totalwt += wt[k]
    
    print("\nProcess\t\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"p{i + 1}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
        
    print(f"\nAverage Turn Around Time: {sum(tat) / n}")
    print(f"Average Waiting Time: {totalwt / n}")

if __name__ == "__main__":
    main()
