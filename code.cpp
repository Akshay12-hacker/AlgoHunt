
#include <iostream>
using namespace std;

int main()
{
    int n, at[10],bt[10], wt[10], tat[10], ct[10], sum = 0, i, j, k;
    float totaltat = 0, totalwt = 0;
    
    cout << "Enter the total number of process: ";
    cin >> n;
    
    cout << "\nEnter the arrival time and burst time of each Process ";
    for(i=0; i < n; i++){
        cout << "Enter arrival time of process["<< i + 1 <<"]:";
        cin >> at[i];
        
        cout << "Enter burst time of process["<<i + 1 <<"]";
        cin>>bt[i];
    }
    
    sum = at[0];
    for(j = 0; j < n; j++){
        sum = sum+bt[j];
        ct[j] = sum;
        
    }
    for(k = 0; k < n; k++){
        tat[k] = ct[k] - at[k];
        totalwt += wt[k];
    }
    cout  << "\nProcess\t\tAT\tBT\tCT\tTAT\tWT\n";
    for(i = 0; i < n; i++){
        cout << "p" << i +1 << "\t" << at[i] << "\t" << bt[i] << "\t" << ct[i] << "\t" << tat[i] << "\t" << wt[i] << endl;
        
    }
    cout << "\n Average Turn Around Time " << totaltat /n << endl;
    cout << "Average Waiting Time" << totalwt /n << endl;
    return 0;
}
