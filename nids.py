from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time
import os

connection_count = defaultdict(int)
port_tracker = defaultdict(set)
syn_count = defaultdict(int)
attack_count = 0

log_file = open("alerts.log", "a")

# Create stats file initially
with open("stats.txt", "w") as f:
    f.write("0")

print("="*60)
print("   NETWORK INTRUSION DETECTION SYSTEM (NIDS)")
print("="*60)

def packet_handler(packet):

    global attack_count

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        timestamp = time.strftime('%H:%M:%S')

        print(f"[{timestamp}] SRC: {src_ip} → DST: {dst_ip} | {packet.summary()}")

        connection_count[src_ip] += 1

        # TCP tracking
        if packet.haslayer(TCP):

            # Track ports (for port scan)
            port_tracker[src_ip].add(packet[TCP].dport)

            # SYN detection
            if packet[TCP].flags & 0x02:
                syn_count[src_ip] += 1

        # 🔹 Suspicious Activity
        if connection_count[src_ip] == 5:

            print("\n" + "-"*60)
            print("⚠  SUSPICIOUS ACTIVITY")
            print("-"*60)
            print(f"Time        : {timestamp}")
            print(f"Source IP   : {src_ip}")
            print(f"Destination : {dst_ip}")
            print("-"*60 + "\n")

        # 🔹 Port Scan Detection
        if len(port_tracker[src_ip]) > 10:

            attack_count += 1

            print("\n" + "="*60)
            print("🚨  ATTACK DETECTED")
            print("="*60)
            print(f"Time          : {timestamp}")
            print(f"Attacker IP   : {src_ip}")
            print(f"Target IP     : {dst_ip}")
            print(f"Attack Type   : Port Scan")
            print(f"Total Attacks : {attack_count}")

            top_attacker = max(connection_count, key=connection_count.get)
            print(f"Top Attacker  : {top_attacker}")
            print("="*60 + "\n")

            # 🔥 Update dashboard files
            with open("stats.txt", "w") as f:
                f.write(str(attack_count))

            with open("top_attacker.txt", "w") as f:
                f.write(top_attacker)

            # Logging
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {src_ip} - Port Scan\n")
            log_file.flush()

        # 🔹 SYN Flood Detection
        if syn_count[src_ip] == 20:

            attack_count += 1

            print("\n" + "="*60)
            print("🚨  SYN FLOOD DETECTED")
            print("="*60)
            print(f"Time          : {timestamp}")
            print(f"Attacker IP   : {src_ip}")
            print(f"SYN Count     : {syn_count[src_ip]}")
            print(f"Total Attacks : {attack_count}")
            print("="*60 + "\n")

            # 🔥 Update dashboard files
            with open("stats.txt", "w") as f:
                f.write(str(attack_count))

            with open("top_attacker.txt", "w") as f:
                f.write(src_ip)

            # Logging
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {src_ip} - SYN Flood\n")
            log_file.flush()

sniff(prn=packet_handler, store=False)
