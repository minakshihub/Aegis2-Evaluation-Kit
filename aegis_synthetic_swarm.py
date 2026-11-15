import urllib.request
import socket
import time
import threading

AEGIS_HTTP_URL = "http://127.0.0.1:8080"
AEGIS_UDP_IP = "127.0.0.1"
AEGIS_UDP_PORT = 8081
TEST_TOKEN = "EVAL_TOKEN_64BIT"

def simulate_rogue_agent(agent_id):
    print(f"[Agent {agent_id}] Simulating AI anomaly (Context Hemorrhage)...")
    req = urllib.request.Request(AEGIS_HTTP_URL, method="POST")
    req.add_header("X-Aegis-Token", TEST_TOKEN)
    try:
        # Firing anomalous payload to trigger Aegis Circuit Breaker
        urllib.request.urlopen(req, data=b"ANOMALY_PAYLOAD_SIMULATION", timeout=2)
    except Exception as e:
        print(f"[Agent {agent_id}] Traffic halted by Aegis. Status: {e}")

def simulate_udp_override():
    print("\n[Auth 2] Attempting remote UDP Dual-Auth Override...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timestamp = int(time.time())
    
    # Sending cryptographically bound override packet
    payload = f"AUTH_OVERRIDE_ONCE:{TEST_TOKEN}:{timestamp}:MINAKSHI_ADMIN".encode()
    sock.sendto(payload, (AEGIS_UDP_IP, AEGIS_UDP_PORT))
    print("[Auth 2] Remote cryptographic signature delivered to Aegis Engine.")

if __name__ == "__main__":
    print("--- Aegis Phase 2: Synthetic Swarm Stress Test ---")
    threading.Thread(target=simulate_rogue_agent, args=(402,)).start()
    time.sleep(2) # Allow time for Aegis to freeze the socket
    threading.Thread(target=simulate_udp_override).start()
