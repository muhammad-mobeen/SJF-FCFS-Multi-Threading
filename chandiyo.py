import threading

# Global variables to store the results of the SJF and FCFS algorithms
sjf_result = None
fcfs_result = None

def sjf_thread():
  global sjf_result
  # Perform the SJF algorithm and store the result in the global variable
  sjf_result = perform_sjf()

def fcfs_thread():
  global fcfs_result
  # Perform the FCFS algorithm and store the result in the global variable
  fcfs_result = perform_fcfs()

# Create the two threads
sjf_t = threading.Thread(target=sjf_thread)
fcfs_t = threading.Thread(target=fcfs_thread)

# Start the threads
sjf_t.start()
fcfs_t.start()

# Wait for the threads to finish
sjf_t.join()
fcfs_t.join()

# Print the results of both algorithms
print("SJF result:", sjf_result)
print("FCFS result:", fcfs_result)
