#!/usr/bin/env python3
import random
import sys
import time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
DIM = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"

FAKE_NETWORKS = [
    {"ssid": "TP-LINK_8A2F",   "bssid": "9C:A2:F4:1B:8A:2F", "sec": "WPA2", "sig": -42},
    {"ssid": "Baan_Suay_5G",   "bssid": "3C:84:6A:F0:12:9D", "sec": "WPA2", "sig": -55},
    {"ssid": "AIS_FIBER_2.4G", "bssid": "D4:6E:0E:77:4C:11", "sec": "WPA2", "sig": -61},
    {"ssid": "TRUE_HOME_WIFI", "bssid": "A0:B1:C2:D3:E4:F5", "sec": "WPA3", "sig": -70},
    {"ssid": "iPhone_ของแฟน",  "bssid": "88:66:5A:2C:9B:04", "sec": "WPA2", "sig": -48},
]

FAKE_WORDLIST_HITS = [
    "12345678", "P@ssw0rd123", "0812345678", "baansuay2024",
    "iloveyou99", "qwertyuiop", "changeme123"
]

def slow_print(text, delay=0.015, color=""):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_progress(label, seconds=2.0, color=GREEN):
    bar_len = 30
    steps = 40
    for i in range(steps + 1):
        pct = int(i / steps * 100)
        filled = int(bar_len * i / steps)
        bar = "█" * filled + "░" * (bar_len - filled)
        sys.stdout.write(f"\r{DIM}[{RESET}{color}{bar}{RESET}{DIM}]{RESET} {label} {pct}%")
        sys.stdout.flush()
        time.sleep(seconds / steps)
    print()

def banner():
    print(RED + BOLD + r"""
 _______  ___   _  _______  _______  ___   _  ___   __  __   ___
|       ||   | | ||       ||       ||   | | ||   | |  |/  | |  _|
|    ___||   |_| ||       ||   _   ||   |_| ||   | |     |  | |_
|   |___ |      _||       ||  | |  ||      _||   | |  |\  | |  _|
|    ___||     |_ |      _||  |_|  ||     |_ |   | |  | | | | |_
|   |    |    _  ||     |_ |       ||    _  ||   | |  |  | |  _|
|___|    |___| |_||_______||_______||___| |_||___| |__|__| |___|

""" + RESET)
    slow_print("  [ FAKE WIFI HACK SIMULATOR — เพื่อความบันเทิงเท่านั้น ]", 0.008, YELLOW)
    slow_print("  [ ไม่เชื่อมต่อเครือข่ายจริง ไม่เก็บข้อมูลจริง ]", 0.008, DIM)
    print()

def scan_networks():
    slow_print("[*] เริ่มสแกนเครือข่าย WiFi บริเวณใกล้เคียง (จำลอง)...", color=DIM)
    fake_progress("scanning", 2.2, GREEN)
    nets = random.sample(FAKE_NETWORKS, k=min(4, len(FAKE_NETWORKS)))
    print()
    print(f"{BOLD}{'#':<3}{'SSID':<20}{'BSSID':<20}{'SEC':<8}{'SIGNAL'}{RESET}")
    for idx, n in enumerate(nets, 1):
        print(f"{idx:<3}{n['ssid']:<20}{n['bssid']:<20}{n['sec']:<8}{n['sig']} dBm")
    print()
    return nets

def choose_target(nets):
    while True:
        try:
            choice = input(f"{YELLOW}[?] เลือกเป้าหมาย (1-{len(nets)}): {RESET}")
            i = int(choice) - 1
            if 0 <= i < len(nets):
                return nets[i]
        except ValueError:
            pass
        print(f"{RED}เลือกไม่ถูกต้อง ลองใหม่{RESET}")

def capture_handshake(target):
    slow_print(f"[*] เริ่ม deauth + จำลองดักจับ handshake จาก {target['ssid']}...", color=DIM)
    fake_progress("capturing handshake", 2.5, YELLOW)
    print(f"{GREEN}[+] จำลองว่าได้ handshake แล้ว (ไฟล์ปลอม: {target['ssid'].replace(' ','_')}.pcap){RESET}")
    print()

def crack_password(target):
    slow_print("[*] เริ่มจำลองการ crack password ด้วย wordlist (rockyou.txt)...", color=DIM)
    fake_progress("cracking", 3.5, RED)
    found = random.random() > 0.15
    if found:
        pwd = random.choice(FAKE_WORDLIST_HITS)
        print(f"{GREEN}{BOLD}[+] KEY FOUND (จำลอง): {pwd}{RESET}")
    else:
        print(f"{RED}[-] ไม่พบรหัสผ่านใน wordlist (จำลอง) — ลองขยาย wordlist{RESET}")
    print()

def outro():
    print(DIM + "-" * 55 + RESET)
    slow_print("หมายเหตุ: ผลลัพธ์ทั้งหมดข้างต้นเป็นข้อมูลสุ่ม/สมมติ", 0.01, YELLOW)
    slow_print("สคริปต์นี้ไม่ได้เชื่อมต่อฮาร์ดแวร์ WiFi จริงแต่อย่างใด", 0.01, YELLOW)
    slow_print("ถ้าอยากแฮก WiFi แบบได้ผลจริง ต้องทำกับ WiFi ของตัวเองเท่านั้น", 0.01, DIM)
    slow_print("และควรเรียนรู้ผ่านคอร์ส/lab ที่ถูกกฎหมาย เช่น TryHackMe, OSWP", 0.01, DIM)
    print(DIM + "-" * 55 + RESET)

def main():
    try:
        banner()
        time.sleep(0.4)
        nets = scan_networks()
        target = choose_target(nets)
        print()
        capture_handshake(target)
        crack_password(target)
        outro()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] ยกเลิกโดยผู้ใช้{RESET}")

if __name__ == "__main__":
    main()
