# NetDiscovery Local Network Telemetry Agent Container
# Multi-tenant network probe that scans local Wi-Fi & LAN subnets
FROM python:3.11-slim

LABEL maintainer="Vedant Singh <https://www.sshconnect.space/>"
LABEL description="Autonomous multi-tenant network discovery agent for Wi-Fi and LAN telemetry"

# Install network diagnostic binaries (arp, ping, iproute2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    iputils-ping \
    net-tools \
    iproute2 \
    procps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy daemon scripts and dependencies
COPY daemon/requirements.txt /app/daemon/requirements.txt
RUN pip install --no-cache-dir -r /app/daemon/requirements.txt

COPY daemon/ /app/daemon/

# Default environment variables
ENV SITE_ID="custom_network"
ENV SITE_NAME="Production Network"
ENV SCAN_INTERVAL="30"
ENV OUTPUT_FILE="/app/devices.json"

# Run scanner daemon continuously
ENTRYPOINT ["python", "daemon/scanner.py"]
CMD ["--interval", "30"]
