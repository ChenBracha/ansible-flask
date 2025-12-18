# 🐳 Docker Deployment Guide

## For Teachers/Evaluators - Quick Start

This application is containerized and will work on **any Linux distribution, macOS, or Windows** with Docker installed.

---

## 📋 Prerequisites

Only Docker is required. No need to install Python, Ansible, or any dependencies.

### Install Docker

**Linux (any distribution):**
```bash
# Ubuntu/Debian
sudo apt-get update && sudo apt-get install -y docker.io docker-compose

# RHEL/CentOS/Fedora
sudo yum install -y docker docker-compose

# Arch
sudo pacman -S docker docker-compose

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker
```

**macOS:**
```bash
brew install docker docker-compose
# Or download Docker Desktop from https://docker.com
```

**Windows:**
Download Docker Desktop from https://docker.com

---

## 🚀 Quick Start (3 Commands)

### Option 1: Using Docker Compose (Recommended)

```bash
# 1. Navigate to the project directory
cd flask-ansible

# 2. Build and start the container
docker-compose up -d

# 3. Access the application
# Open browser: http://localhost:5000
```

**That's it!** The app is now running in a container.

---

### Option 2: Using Docker CLI

```bash
# 1. Build the image
docker build -t snake-cogwheel .

# 2. Run the container
docker run -d -p 5000:5000 --name snake-cogwheel snake-cogwheel

# 3. Access the application
# Open browser: http://localhost:5000
```

---

## 🎯 Verification

Once running, verify the application:

```bash
# Check if container is running
docker ps

# View application logs
docker logs snake-cogwheel

# Test the web interface
curl http://localhost:5000
```

**Expected output:** HTML content of the Snake and CogWheel UI

---

## 📱 Using the Application

1. **Open browser:** `http://localhost:5000`
2. **Leave both fields empty** to run the default playbook on localhost
3. **Click "▶️ RUN PLAYBOOK"**
4. **View results** - the playbook executes inside the container

### Example Playbooks Included

- **`default_ping.yml`** - Connectivity test (default)
- **`system_info.yml`** - System diagnostics and health check
- **`create_workspace.yml`** - Creates a development workspace

### Running Different Playbooks

1. Type playbook name in "Playbook Path" field:
   - `system_info.yml`
   - `create_workspace.yml`
2. Leave "Target Hosts" empty (runs on localhost inside container)
3. Click "▶️ RUN PLAYBOOK"

---

## 🔧 Management Commands

### View Logs
```bash
docker logs -f snake-cogwheel
```

### Stop the Application
```bash
docker-compose down
# or
docker stop snake-cogwheel
```

### Restart the Application
```bash
docker-compose restart
# or
docker restart snake-cogwheel
```

### Remove Everything
```bash
docker-compose down -v
docker rmi snake-cogwheel
```

---

## 🌐 Accessing from Another Machine

If you want to access the app from another computer on your network:

1. **Find your IP address:**
   ```bash
   hostname -I  # Linux
   ipconfig getifaddr en0  # macOS
   ```

2. **Access from another machine:**
   ```
   http://YOUR_IP:5000
   ```

3. **Firewall:** Ensure port 5000 is open
   ```bash
   # Ubuntu/Debian
   sudo ufw allow 5000
   
   # RHEL/CentOS
   sudo firewall-cmd --add-port=5000/tcp --permanent
   sudo firewall-cmd --reload
   ```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find what's using port 5000
sudo lsof -i :5000

# Use a different port
docker run -d -p 8080:5000 --name snake-cogwheel snake-cogwheel
# Then access: http://localhost:8080
```

### Permission Denied
```bash
# Add your user to docker group (Linux)
sudo usermod -aG docker $USER
# Log out and back in
```

### Container Won't Start
```bash
# Check logs
docker logs snake-cogwheel

# Remove and rebuild
docker-compose down
docker-compose up --build
```

### Can't Access Web Interface
```bash
# Check if container is running
docker ps

# Check container health
docker inspect snake-cogwheel | grep -A 5 Health

# Test from inside container
docker exec snake-cogwheel curl http://localhost:5000
```

---

## 📊 System Requirements

- **RAM:** 512 MB minimum (1 GB recommended)
- **Disk:** 500 MB for image + playbooks
- **CPU:** Any modern processor
- **OS:** Any Linux distribution, macOS 10.14+, Windows 10+

---

## 🔒 Security Notes

### For Evaluation/Testing
- Default configuration is suitable for local testing
- Runs on localhost:5000 by default

### For Production Use
- Add authentication (not included in demo)
- Use HTTPS/TLS (reverse proxy recommended)
- Restrict network access
- Review and audit all playbooks before execution

---

## 📝 Architecture

```
┌─────────────────────────────────────┐
│   Docker Container                  │
│  ┌───────────────────────────────┐  │
│  │  Python 3.11 + Flask          │  │
│  │  Ansible 2.x                  │  │
│  │  Snake and CogWheel App       │  │
│  └───────────────────────────────┘  │
│         ↓ Port 5000                 │
└─────────────────────────────────────┘
              ↓
      http://localhost:5000
```

---

## ✅ Advantages of Docker Deployment

1. **Universal Compatibility** - Works on any Linux distribution
2. **Zero Configuration** - All dependencies included
3. **Isolated Environment** - Won't conflict with system packages
4. **Reproducible** - Same behavior everywhere
5. **Easy Cleanup** - Remove everything with one command
6. **Version Locked** - Ansible and Python versions are consistent

---

## 🎓 For Evaluation

### Quick Demo Steps

1. **Start the application:**
   ```bash
   docker-compose up -d
   ```

2. **Open browser to http://localhost:5000**

3. **Run default playbook:**
   - Leave both fields empty
   - Click "▶️ RUN PLAYBOOK"
   - View connectivity test results

4. **Run system info playbook:**
   - Enter `system_info.yml` in Playbook Path
   - Click "▶️ RUN PLAYBOOK"
   - View comprehensive system information

5. **Run workspace creator:**
   - Enter `create_workspace.yml` in Playbook Path
   - Click "▶️ RUN PLAYBOOK"
   - Workspace created at `/root/ansible_workspace` in container

6. **View logs:**
   ```bash
   docker logs snake-cogwheel
   ```

7. **Cleanup:**
   ```bash
   docker-compose down
   ```

---

## 📚 Additional Resources

- **GitHub Repository:** [Include your repo URL]
- **Docker Documentation:** https://docs.docker.com
- **Ansible Documentation:** https://docs.ansible.com
- **Flask Documentation:** https://flask.palletsprojects.com

---

## 🆘 Support

If you encounter any issues:

1. Check this troubleshooting section
2. Review container logs: `docker logs snake-cogwheel`
3. Ensure Docker is running: `docker ps`
4. Verify port availability: `sudo lsof -i :5000`

---

**Built with ❤️ using Flask, Ansible, and Docker**

**Snake and CogWheel © 2025**

