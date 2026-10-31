# enterprise-resilience-testing
# Enterprise Infrastructure Testing & Disaster Recovery Portfolio

This repository demonstrates hands-on implementation of automated infrastructure testing, network security boundary verification, and disaster recovery simulation designed for enterprise-grade resilience.

 🛠️ Included Projects

 1. Automated Infrastructure Testing Pipeline (`/infrastructure-pipeline`)
 2. Core Concepts:** Infrastructure as Code (IaC), Programmatic Network Isolation Testing, Secure VPC Architecture.
 3. Tech Stack:** Terraform, Terratest (Go), GitHub Actions.
Objective:** Automatically provisions an enterprise VPC and executes integration tests to programmatically verify that high-risk perimeter entry points (like SSH Port 22) are isolated from public ingress.

2. Automated Disaster Recovery & Chaos Simulator (`/disaster-recovery-chaos`)
Core Concepts:** Business Continuity, RPO/RTO Enforcement, Containerized Resilience Testing.
Tech Stack:** Docker Compose, Python, PostgreSQL.
Objective:** Simulates localized infrastructure failure (Chaos Engineering) and measures automated failover to a secondary data recovery node, calculating state restoration speeds.

 3. Network Security & Intrusion Detection Validation (`/network-security-ids`)
Core Concepts:** Network Traffic Analysis, Zero-Trust Access Boundaries, Threat Signature Auditing.
Tech Stack:** Snort IDS, Python (Traffic Generator).
Objective:** Configures boundary traffic filtering rules via Snort and evaluates detection coverage by running synthetic malicious traffic signatures against the network stack.

