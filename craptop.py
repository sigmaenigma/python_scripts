"""
MIT License

Copyright (c) 2023 Adrian Sanabria-Diaz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
""" This is a crappy attempt at a worse TOP or HTOP running in Python """
import psutil
import time

# Title (displayed only once)
print("Adrian's CrapTOP")

while True:
    # Get CPU usage percentages for each core
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)

    # Get memory usage statistics
    memory_info = psutil.virtual_memory()

    # Get a list of the top 20 running processes by CPU usage
    top_processes = sorted(
        psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']),
        key=lambda x: x.info['cpu_percent'],
        reverse=True)[:20]

    # Clear the terminal (works on Unix-like systems, modify for Windows)
    print("\033c", end='')

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

    # Sleep for 1 second before refreshing
    time.sleep(1)
