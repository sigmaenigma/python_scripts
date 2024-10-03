import psutil
import time
import heapq
import os

# Title (displayed only once)
print("Adrian's CrapTOP")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        # Get CPU usage percentages for each core
        cpu_usage = psutil.cpu_percent(interval=1, percpu=True)

        # Get memory usage statistics
        memory_info = psutil.virtual_memory()

        # Get a list of the top 20 running processes by CPU usage
        top_processes = heapq.nlargest(20, psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']),
                                       key=lambda x: x.info['cpu_percent'])

        # Clear the terminal
        clear_terminal()

        # Print CPU usage for each core in a row
        print("CPU Cores:", end=' ')
        for i, core_usage in enumerate(cpu_usage):
            if i != 0:
                print("|", end=' ')
            print(f"Core {i}: {core_usage}%", end=' ')
        print()  # Newline after printing CPU cores

        # Calculate used and unused memory
        total_hashes = 100
        used_percent = memory_info.percent
        used_hashes_count = int(total_hashes * (used_percent / 100))
        unused_hashes_count = total_hashes - used_hashes_count
        used_hashes = "\033[31m" + "#" * used_hashes_count + "\033[0m"  # Red color for used memory
        unused_hashes = "#" * unused_hashes_count  # White # signs for unused memory

        # Print memory usage with percentage, red # signs for used memory, and white # signs for unused memory
        memory_usage = f"{used_percent}% {used_hashes}{unused_hashes}"
        print(f"\nMemory Usage: {memory_usage}")

        # Print top 20 running processes by CPU usage
        print("\nTop 20 Running Processes:")
        for process in top_processes:
            print(f"PID: {process.info['pid']} - Name: {process.info['name']} - CPU Usage: {process.info['cpu_percent']}%")

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        print(f"Error retrieving process information: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Sleep for 1 second before refreshing
    time.sleep(1)
