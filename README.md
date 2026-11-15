# Aegis Phase 2: Swarm Governance Engine (Evaluation Kit)
**Pagma Dimensions | B2B Public Evaluation Repository**
**Chief Architect:** Minakshi Aggarwal

Welcome to the Aegis Phase 2 Evaluation Kit. This repository contains the tools required to evaluate the industry's first zero-trust, bare-metal C++ governance firewall for AI agent swarms.

## The Governance Problem
Standard API gateways blindly route AI traffic. They fail to detect context hemorrhages, oscillation streaks, or swarm deadlocks until system memory crashes. 

## The Aegis Solution
Aegis Phase 2 operates physically orthogonal to your AI models. It natively monitors up to 65,536 concurrent agents at sub-millisecond speeds. The microsecond an anomaly is detected, Aegis drops the network clutch, halts the AI thread, and enforces a cryptographic Human-In-The-Loop (HITL) override.

### Key Enterprise Features
* Dual-Authorization Pipeline: Requires two distinct, vetted human signatures from physically different IP addresses to override a blocked agent.
* 30-Minute SLA Watchdog: A mathematically bound global clock that safely executes a terminal kill if an agent is left pending without human authorization.
* Precision Telemetry (The "Rolling Pin"): No more digging through central log databases. Aegis isolates a 16-event Black Box history for every individual agent and dumps it instantly upon anomaly detection.
* WORM-Compliant Audit Ledger: Cryptographically chained logs ensure total accountability for all human overrides.

## Running the Evaluation
This kit provides the aegis_synthetic_swarm.py script to simulate rogue AI agents hitting the firewall. 

1. Request a 72-Hour Evaluation Binary from Pagma Dimensions.
2. Boot the binary: ./aegis2_trial
3. Run the synthetic swarm: python3 aegis_synthetic_swarm.py
4. Observe the terminal as Aegis halts the rogue agents and requests Dual-Authorization.

## Commercial Licensing
The unlimited, unrestricted C++ source code is available for enterprise acquisition. 
* Price: $2,000 USD
* Includes: Full unredacted Source Code, Tri-Array L1 Cache Blueprints, and Corporate NDA execution.
