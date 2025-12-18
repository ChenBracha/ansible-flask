# Snake and CogWheel - Ansible Playbook Runner
# Dockerfile for cross-platform deployment

FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies and Ansible
RUN apt-get update && apt-get install -y \
    openssh-client \
    sshpass \
    git \
    curl \
    && pip install --no-cache-dir ansible \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY templates/ templates/
COPY *.yml .
COPY README.md .

# Create directory for user playbooks and copy any existing ones
RUN mkdir -p /app/playbooks
COPY playbooks/ /app/playbooks/

# Expose Flask port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Run the application
CMD ["python", "app.py"]

