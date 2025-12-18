# 🚀 Setup Guide - Snake and CogWheel

## Choose Your Method

You have **two options** to run this application:

| Method | Best For | Requirements |
|--------|----------|--------------|
| **🐳 Docker** | Teachers, Evaluators, Production | Just Docker |
| **💻 Local** | Development, Your Own Machine | Python, Ansible |

**Note:** Both use port 5000, so you can only run ONE at a time.

---

## 🐳 Option 1: Docker (Recommended for Teachers)

### Why Docker?
- ✅ Works on **ANY** Linux distribution
- ✅ No need to install Python or Ansible
- ✅ Consistent environment everywhere
- ✅ Easy cleanup

### Quick Start

```bash
# Start the application
./start.sh

# Or manually:
docker-compose up -d
```

**Access:** http://localhost:5000

### Stop the Application

```bash
# Stop the application
./stop.sh

# Or manually:
docker-compose down
```

### Rebuild After Changes

```bash
docker-compose down
docker-compose up --build -d
```

---

## 💻 Option 2: Local Installation

### Why Local?
- ✅ Faster for development
- ✅ Easier to debug
- ✅ Direct access to your machine
- ✅ No Docker overhead

### Prerequisites

1. **Python 3.7+**
   ```bash
   python3 --version
   ```

2. **Ansible**
   ```bash
   # macOS
   brew install ansible
   
   # Ubuntu/Debian
   sudo apt install ansible
   
   # Or via pip
   pip3 install ansible
   ```

### Installation

```bash
# 1. Install Python dependencies
pip3 install -r requirements.txt

# 2. Run the application
python3 app.py
```

**Access:** http://localhost:5000

### Stop the Application

Press `Ctrl+C` in the terminal where it's running.

---

## 🔄 Switching Between Methods

### From Docker to Local

```bash
# 1. Stop Docker
docker-compose down

# 2. Run locally
python3 app.py
```

### From Local to Docker

```bash
# 1. Stop local (Ctrl+C)

# 2. Run Docker
docker-compose up -d
```

---

## 📊 Quick Comparison

### Docker Method
```
✅ Universal compatibility
✅ Isolated environment
✅ No manual dependency installation
✅ Production-ready
❌ Slightly slower startup
❌ Requires Docker installed
```

### Local Method
```
✅ Faster execution
✅ Easier debugging
✅ Direct file access
✅ No container overhead
❌ Requires Ansible installed
❌ Environment-dependent
```

---

## 🎓 For Teachers/Evaluators

**Use Docker!** It's the easiest:

```bash
./start.sh
# Open: http://localhost:5000
```

That's it! Everything works out of the box.

---

## 👨‍💻 For Developers

**Use Local!** It's faster for development:

```bash
pip3 install -r requirements.txt
python3 app.py
# Open: http://localhost:5000
```

---

## 🐛 Troubleshooting

### Port 5000 Already in Use

**Check what's using it:**
```bash
# macOS/Linux
lsof -i :5000

# Kill the process
kill -9 <PID>
```

**Or use a different port:**

**Docker:**
```bash
# Edit docker-compose.yml
ports:
  - "8080:5000"  # Change 5000 to 8080
```

**Local:**
```bash
# Edit app.py, last line:
app.run(debug=True, host='0.0.0.0', port=8080)
```

### Docker Not Starting

```bash
# Check if Docker is running
docker ps

# Check logs
docker logs snake-cogwheel

# Rebuild from scratch
docker-compose down -v
docker-compose up --build
```

### Local Ansible Not Found

```bash
# Verify installation
ansible --version

# If not found, install:
pip3 install ansible
```

---

## 📁 Project Structure

```
flask-ansible/
├── app.py                    # Main Flask application
├── templates/
│   └── index.html           # Web UI
├── default_ping.yml         # Default playbook
├── system_info.yml          # System diagnostics
├── create_workspace.yml     # Workspace creator
├── playbooks/               # Custom playbooks directory
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker compose config
├── start.sh               # Quick start script
└── stop.sh                # Quick stop script
```

---

## ✅ Verification

After starting (either method):

```bash
# Check if it's running
curl http://localhost:5000

# Should return HTML content
```

---

## 🎯 Quick Decision Guide

**Ask yourself:**

1. **"I need to show this to someone on a different computer"**
   → Use Docker 🐳

2. **"I'm developing and testing frequently"**
   → Use Local 💻

3. **"I don't want to install Ansible"**
   → Use Docker 🐳

4. **"I need it to work on any Linux distribution"**
   → Use Docker 🐳

5. **"I'm running it on my own Mac"**
   → Use Local 💻 (faster)

---

## 📝 Summary

**For quick evaluation/demo:**
```bash
./start.sh
```

**For development:**
```bash
python3 app.py
```

**Both work perfectly - choose what fits your needs!** 🚀

