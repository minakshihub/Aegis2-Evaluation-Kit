# Aegis Phase 2: Bare-Metal Swarm Governance Engine (Evaluation Kit)
**Pagma Dimensions | B2B Public Evaluation Repository**
**Chief Architect:** Minakshi Aggarwal

Welcome to the Aegis Phase 2 Evaluation Kit. This repository provides the architecture blueprints and synthetic simulators required to evaluate the industry's first zero-trust, bare-metal C++ governance firewall for AI agent swarms.

---

## 1. The Swarm Governance Crisis
The industry is scaling AI agentic flows without bare-metal governance. Standard API gateways blindly route traffic, failing to comprehend context hemorrhages, oscillation streaks, or swarm deadlocks. When an agent hallucinates, thousands of logs are vomited into a central database, creating a "needle in a haystack" crisis that takes engineers hours to debug while system memory crashes.

## 2. The Architectural Solution
Aegis Phase 2 operates physically orthogonal to your AI models. It natively monitors up to 65,536 concurrent agents at sub-millisecond speeds. 

### The Tri-Array Memory Layout
To achieve extreme density without CPU drag, Aegis decouples memory into three strict arrays:
* The Hot Core: A half-cache-line array tracking active math and the 3-strike LLM counter. 65,536 agents consume just 2.09 MB of L1 cache.
* The Cold Governance Pool: A dormant background array holding 30-minute timers and IP addresses, accessed only when an agent is paused.
* The Flight Data Recorder: The write-only Black Box history.

### The Lock-Free Clutch
When an anomaly trips, Aegis pauses the specific TCP socket in RAM without halting the CPU thread or affecting the other 65,535 agents.

## 3. Precision Telemetry (The "Rolling Pin")
Aegis completely solves the observability crisis by isolating a 16-event history for every single agent in RAM.
* The Rolling Pin: Agent 402 constantly overwrites its own oldest memory in a 16-slot ring buffer. 
* The Precision Dump: When Agent 402 hallucinates, Aegis disengages the clutch and executes a direct O(1) memory read. The human operator sees exactly the 16 steps Agent 402 took right before going rogue, with zero noise from the other 65,535 agents.

## 4. 24/7 Human-In-The-Loop (HITL) Governance
The core USP is the mathematically undeniable Dual-Authorization SLA Pipeline.
* The 30-Minute Watchdog: If an agent is paused awaiting human input and 30 minutes expire, Aegis safely executes a terminal kill to prevent permanent memory hangs.
* Anti-Collusion Physical Gate (No Double-Dipping): Aegis mandates two human signatures. It actively interrogates the incoming UDP packets and mathematically rejects them if both signatures come from the same physical IP machine (Sybil Attack prevention).
* Cryptographic Replay Protection: Remote UDP override packets must contain the 64-bit secret token and a monotonic timestamp, rendering network sniffing completely useless.

## 5. Global Network Shields
* 5-Second Circuit Breaker with Jitter: If the upstream LLM crashes, Aegis blocks outgoing TLS handshakes. It serves Python agents a synthetic HTTP 429 from RAM, embedded with a microsecond-randomized Retry-After header for a smooth recovery.
* 3-Strike Upstream Failsafe: If an agent bounces against a broken LLM three times, Aegis executes a hard kill to preserve system resources.

---

## 6. Running the Evaluation Simulator
This kit contains a 72-hour `aegis2_trial` binary compiled specifically for your evaluation window. You may test this against the included synthetic simulator or wire it directly to your own host agents.

**Evaluation Trial Policy:**
* Free 72-Hour Evaluation Binaries are strictly limited to **3 free requests per company**.
* Contact minakshi.architech@gmail.com or visit pagmadimensions.com to request your initial trial refresh.

1. Boot the firewall in your terminal:
   chmod +x aegis2_trial
   ./aegis2_trial
2. In a second terminal, execute the synthetic swarm (or route your host agents to 127.0.0.1:8080):
   python3 aegis_synthetic_swarm.py
3. Observe the terminal as Aegis halts the rogue agent and requests Dual-Authorization via UDP.

## 7. Commercial Enterprise Licensing

**Tier 1: Extended 72-Hour Paid Trial ($2,000 USD)**
* After a company exhausts their 3 free evaluation trials, any additional 72-hour binary extensions require a $2,000 USD payment per issuance.
* The secure download link for the paid 72-hour binary will be delivered directly via email.

**Tier 2: Full Enterprise Acquisition (Unlimited Binary & Source Code)**
* The unrestricted, perpetual C++ compiled binary AND the unredacted bare-metal source code are exclusively available upon execution of a Corporate Non-Disclosure Agreement (NDA) and strict commercial legal compliance.
