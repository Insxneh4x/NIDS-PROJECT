# 🚨 Network Intrusion Detection System (NIDS)

## 📌 Overview

This project is a Python-based **Network Intrusion Detection System (NIDS)** designed to monitor network traffic in real-time and identify potential security threats.

It uses packet sniffing techniques to analyze network behavior and detect malicious or suspicious activities such as abnormal traffic patterns and scanning attempts.

The system also includes a lightweight **web-based dashboard** for live monitoring and visualization of detected attacks.

---

## 🧠 What is NIDS?

A Network Intrusion Detection System (NIDS) is a security tool that monitors network traffic to identify unauthorized access, misuse, or attacks.

This project demonstrates how intrusion detection works by analyzing packet-level data using Python.

---

## 🚀 Features

### 🔍 Real-Time Packet Monitoring

* Captures live network packets using Scapy
* Displays source and destination IP addresses
* Continuously analyzes traffic

---

### ⚠️ Suspicious Activity Detection

* Detects sudden burst of packets
* Helps identify abnormal behavior

---

### 🚨 Port Scan Detection

* Tracks multiple ports accessed by a single IP
* Detects scanning attempts

---

### 💣 SYN Flood Detection

* Monitors TCP SYN packets
* Detects incomplete handshakes (DoS attack pattern)

---

### 📊 Live Dashboard

* Shows total attacks detected
* Displays top attacker
* Updates automatically

---

### 📝 Logging System

* Saves attack data in `alerts.log`
* Useful for analysis

---

## ⚙️ Requirements

Install required libraries:

```bash
pip install scapy flask --break-system-packages
```

---

## 🚀 How to Run

### Step 1: Open terminal and go to project folder

```bash
cd NIDS_Project
```

### Step 2: Run the NIDS

```bash
python3 nids.py
```

### Step 3: Open new terminal and run dashboard

```bash
python3 dashboard.py
```

### Step 4: Open browser

```
http://localhost:5000
```

---

## 🧪 How to Test

Run any of the following:

```bash
nmap -sS localhost
```

or

```bash
ping -c 10 127.0.0.1
```

---

## 🎯 Purpose of the Project

* Understand network attacks
* Learn intrusion detection concepts
* Simulate real-world monitoring system

---

## ⚡ Technologies Used

* Python
* Scapy
* Flask
* Nmap

---

## 👨‍💻 Author
Jashan Deep Singh
