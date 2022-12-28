'''
Author: Muhammad Mobeen
Reg No: 200901097
BS-CS-01  (B)
Lab Task [7 DEC 2022]
Submitted to Mam Reeda Saeed

Explaination of Task:-
I have made a list of Processes and each process is made up of an individual list that contains the attributes
to specify that spacific list. This was done to simplify the class/functions structure for the SJF Algorithm.

                       Process = [at,bt,ct,tat,wt]
'''

class FCFS:
    def __init__(self):
        self.process_list = None
        self.AvgTAT = 0
        self.AvgWT = 0
        self.Gantt_Chart = 0

    def findCompletionTime(self):
        for i,p in enumerate(self.process_list):
            self.Gantt_Chart += p[1]
            self.process_list[i].append(self.Gantt_Chart)

    def findTAT(self):
        for i,p in enumerate(self.process_list):
            self.process_list[i].append(p[2]-p[0])

    def findWT(self):
        for i,p in enumerate(self.process_list):
            self.process_list[i].append(p[3]-p[1])

    def findAvgTAT(self):
        for i,p in enumerate(self.process_list):
            self.AvgTAT += p[3]
        self.AvgTAT /= len(self.process_list)

    def findAvgWT(self):
        for i,p in enumerate(self.process_list):
            self.AvgWT += p[4]
        self.AvgWT /= len(self.process_list)

    def showData(self):
        print("____________________________________________________________________________")
        print("Processes Ran from 0 --> {}".format(self.Gantt_Chart))
        print("Average Turn-around Time = ", self.AvgTAT)
        print("Average Wait Time = ", self.AvgWT)

        for i,p in enumerate(self.process_list,1):
            print("\n-----------------------------------------------------------------")
            print("Process #{}:-".format(i))
            print("Arrival Time: ", p[0])
            print("Burst Time: ", p[1])
            print("Completion Time: ", p[2])
            print("Turn-around Time: ", p[3])
            print("Wait Time: ", p[4])

class SJF:
    def __init__(self):
        self.process_list = None
        self.AvgTAT = 0
        self.AvgWT = 0
        self.Gantt_Chart = 0

    def sort_process_list(self):
        n = len(self.process_list) - 1
        # Within the unsorted portion, except the last number
        for unsorted in range(n, 0, -1):
            swapped = False
            for i in range(unsorted):
                # If curr > next, swap
                if self.process_list[i][1] > self.process_list[i+1][1]:
                    self.process_list[i], self.process_list[i+1] = self.process_list[i+1], self.process_list[i]
                    swapped = True

            # Check if its sorted by this time
            if not swapped:
                break
        print("Processesses Sorted!")
        # print(self.process_list)
        # return self.process_list # for easy testing

    def findCompletionTime(self):
        total_processes = len(self.process_list)
        processes_done = []
        while True:
            if len(processes_done) != total_processes:
                arrived_processes = []  # Stores index of arrived processes
                for it,p in enumerate(self.process_list, 0):
                    if len(processes_done) > 0:
                        if p[0] <= self.Gantt_Chart and it > processes_done[-1]:
                            arrived_processes.append(it)
                    else:
                        if p[0] <= self.Gantt_Chart:
                            arrived_processes.append(it)
                if len(arrived_processes) > 0:
                    for ap in arrived_processes:
                        self.Gantt_Chart += self.process_list[ap][1]
                        self.process_list[ap].append(self.Gantt_Chart)
                    processes_done = processes_done + arrived_processes
                else:
                    self.Gantt_Chart += 1
            else:
                break
                    
    def findTAT(self):
        for i,p in enumerate(self.process_list):
            self.process_list[i].append(p[2]-p[0])

    def findWT(self):
        for i,p in enumerate(self.process_list):
            self.process_list[i].append(p[3]-p[1])

    def findAvgTAT(self):
        for i,p in enumerate(self.process_list):
            self.AvgTAT += p[3]
        self.AvgTAT /= len(self.process_list)

    def findAvgWT(self):
        for i,p in enumerate(self.process_list):
            self.AvgWT += p[4]
        self.AvgWT /= len(self.process_list)

    def showData(self, original_list):
        print("____________________________________________________________________________")
        print("Processes Ran from 0 --> {}".format(self.Gantt_Chart))
        print("Processes Sequence: ",end="")
        for x,p in enumerate(self.process_list):
            if x == len(self.process_list)-1:
                for t,op in enumerate(original_list,1):
                    if op == p:
                        print("{}".format(t))
            else:
                for t,op in enumerate(original_list,1):
                    if op == p:
                        print("{}".format(t),end="-->")
        print("Average Turn-around Time = ", self.AvgTAT)
        print("Average Wait Time = ", self.AvgWT)

        for i,p in enumerate(self.process_list,1):
            pn = None
            for t,op in enumerate(original_list):
                if op == p:
                    pn = t+1
            print("\n-----------------------------------------------------------------")
            print("Process #{}:-".format(pn))
            print("Arrival Time: ", p[0])
            print("Burst Time: ", p[1])
            print("Completion Time: ", p[2])
            print("Turn-around Time: ", p[3])
            print("Wait Time: ", p[4])

if __name__ == "__main__":
    sjf_scheduler = SJF()

    # Processes |  Arrival Time  |  Burst Time |
    P1          = [     1       ,       3     ]
    P2          = [     2       ,       4     ]
    P3          = [     1       ,       2     ]
    P4          = [     4       ,       4     ]
    sjf_scheduler.process_list = [P1, P2, P3, P4]

    sjf_scheduler.sort_process_list()  # Sorts processes according to Burst Time
    sjf_scheduler.findCompletionTime()
    sjf_scheduler.findTAT()
    sjf_scheduler.findWT()
    sjf_scheduler.findAvgTAT()
    sjf_scheduler.findAvgWT()
    sjf_scheduler.showData([P1, P2, P3, P4])


    fcfs_scheduler = FCFS()

    # Processes |  Arrival Time  |  Burst Time |
    P1          = [     0       ,       5     ]
    P2          = [     5       ,       7     ]
    P3          = [     7       ,       3     ]
    fcfs_scheduler.process_list = [P1, P2, P3]

    fcfs_scheduler.findCompletionTime()
    fcfs_scheduler.findTAT()
    fcfs_scheduler.findWT()
    fcfs_scheduler.findAvgTAT()
    fcfs_scheduler.findAvgWT()
    fcfs_scheduler.showData()
    
