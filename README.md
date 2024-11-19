
# WiFi Analyzer

The **WiFi Analyzer** is a versatile tool designed to monitor WiFi networks and provide insights into network activity. It allows you to:
- Analyze WiFi traffic in real-time, capturing information about devices communicating on the network, including their source/destination addresses and the protocols/ports used.
- Identify vulnerabilities, such as unusually heavy traffic or passwords transmitted in non-encrypted formats.
- View saved WiFi passwords stored on your computer.
- Save captured data to a text file for future analysis.

---

## Features

### 🛠️ **Network Sniffer**
- Captures and logs real-time network traffic.
- Displays detailed information about packets, including:
  - Source and destination addresses.
  - Communication protocols and ports.
- Helps identify unusual activity or potential vulnerabilities.

### 🔑 **Saved Password Viewer**
- Lists all saved WiFi networks and their associated passwords stored on your device.

### 📁 **Export Data**
- Save network traffic logs to a text file for later use.
- Easy-to-read text format for analysis.

---

## Prerequisites

### Required Drivers
This tool requires either **WinPcap** or **Npcap** drivers to capture network traffic. Ensure you have one of these installed before using the application:
- [WinPcap Download](https://www.winpcap.org/install/default.htm)
- [Npcap Download](https://nmap.org/npcap/)

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/WiFi-Analyzer.git
   cd WiFi-Analyzer
   ```

2. **Install Required Python Libraries**
   Use the following command to install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Drivers**
   - Install [WinPcap](https://www.winpcap.org/install/default.htm) or [Npcap](https://nmap.org/npcap/).

4. **Run the Application**
   Start the tool by executing:
   ```bash
   python wifi_analyzer.py
   ```

---

## How to Use?

### Overview
The application has two primary sections, accessible through tabs:
1. **Network Sniffer:** Monitors and analyzes network traffic in real-time.
2. **Saved Passwords:** Displays saved WiFi networks and their passwords.

---

### 📡 **Network Sniffer**

1. Click the **Start** button to begin monitoring WiFi traffic.
2. Traffic data will populate in the log area, showing packet details.
3. Click the **Stop** button to end monitoring.
4. Optionally, click **Save as TXT** to export the logs to a text file. Ensure monitoring is stopped before saving.

### 🔑 **Saved Password Viewer**

- Navigate to the **Saved Passwords** tab to view all saved WiFi networks and their corresponding passwords.

---

### User Interface Preview

#### **Main Dashboard - Network Sniffer**
Start, stop, and save logs of network activity:
![Sniffer Tab]![Screenshot 2024-11-19 002107](https://github.com/user-attachments/assets/7653d213-95fd-4c58-8084-00af77468a9b)




---

## Important Notes

- Ensure that the **sniffer** is stopped before saving data to avoid errors.
- The tool operates under the assumption of proper permissions and driver support.
- The saved passwords feature is dependent on the network profiles available on your system.

---

## Disclaimer

This tool is intended for **educational and personal use only**. Unauthorized network monitoring is illegal and unethical. Use this tool responsibly and ensure you have permission to analyze the networks you monitor.

---

## Contributing

Contributions are welcome! If you'd like to enhance this project, feel free to:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
