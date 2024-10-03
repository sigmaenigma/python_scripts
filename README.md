# Adrian's CrapTOP

Adrian's CrapTOP is a simple Python script that mimics the functionality of system monitoring tools like `top` or `htop`. It displays real-time CPU and memory usage statistics, as well as a list of the top 20 running processes by CPU usage. I built this using 100% prompt engineering in ChatGPT to see if it could build me a useable tool without ever touching code.

## Features

- **CPU Usage**: Displays the CPU usage percentage for each core.
- **Memory Usage**: Shows the memory usage with a visual representation using colored hash signs.
- **Top Processes**: Lists the top 20 running processes by CPU usage.

## Requirements

- Python 3.x
- `psutil` library

You can install the `psutil` library using pip:

```bash
pip install psutil
```

## Usage

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed on your system.
3. Install the `psutil` library if you haven't already.
4. Run the script:

```bash
python craptop.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by system monitoring tools like `top` and `htop`.
- Developed by Adrian Sanabria-Diaz.
