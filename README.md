# 🐍 Snake and CogWheel ⚙️

**Ansible Playbook Web Runner**

A Flask-based web application that provides a simple and intuitive UI for executing Ansible playbooks with dynamic inventory and playbook selection.

---

## 📋 Project Overview

**Snake and CogWheel** is a lightweight web interface for running Ansible playbooks. It enables users to:

- Execute Ansible playbooks through a web browser
- Specify custom target hosts (inventory) or default to `localhost`
- Choose a playbook file or use the default ping playbook
- View real-time output from playbook execution
- Handle both successful runs and error scenarios

### Key Features

- **Default Localhost Execution**: If no hosts are specified, playbooks run on `localhost` automatically
- **Default Playbook**: A built-in `default_ping.yml` playbook for quick connectivity testing
- **Real-time Output**: Captures and displays both `stdout` and `stderr` from Ansible runs
- **Simple UI**: Clean, modern interface built with Jinja2 templates
- **Error Handling**: Comprehensive error messages for missing files, timeouts, and execution failures

### Technology Stack

- **Backend**: Python 3 + Flask
- **Frontend**: HTML5, CSS3, Jinja2 templating
- **Automation**: Ansible (executed via subprocess)
- **Execution Model**: Direct `ansible-playbook` command invocation

---

## 🚀 Quick Start

### Choose Your Method

You can run this application in **two ways**:

| Method | Command | Best For |
|--------|---------|----------|
| **🐳 Docker** | `./start.sh` | Teachers, Evaluators, Production |
| **💻 Local** | `python3 app.py` | Development, Your Own Machine |

**Both use port 5000** - choose one!

---

### 🐳 Docker

**Quick Start:**
```bash
./start.sh
# Open: http://localhost:5000
```

**Stop:**
```bash
./stop.sh
```

**Why Docker?**
- ✅ Works on ANY Linux distribution
- ✅ No dependencies to install
- ✅ Consistent everywhere

📖 **Full Guide:** [SETUP_GUIDE.md](SETUP_GUIDE.md) | [DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md)

---

### 💻 Local Installation

### Prerequisites

Before deploying the application locally, ensure you have the following installed:

1. **Python 3.7+**
   ```bash
   python3 --version
   ```

2. **Ansible**
   ```bash
   # On macOS
   brew install ansible
   
   # On Ubuntu/Debian
   sudo apt update && sudo apt install ansible -y
   
   # On RHEL/CentOS
   sudo yum install ansible -y
   
   # Via pip
   pip3 install ansible
   ```

3. **pip** (Python package manager)
   ```bash
   python3 -m pip --version
   ```

---

### Installation Steps

#### 1. Clone or Download the Project

```bash
cd /path/to/your/workspace
git clone <your-repository-url>
cd flask-ansible
```

Or download the project files directly to your preferred directory.

#### 2. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

This will install Flask and any other required Python packages.

#### 3. Verify File Structure

Ensure your project structure looks like this:

```
flask-ansible/
├── app.py
├── default_ping.yml
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

#### 4. Test Ansible Installation

Verify that Ansible is installed and accessible:

```bash
ansible --version
ansible-playbook --version
```

---

### Running the Application

#### Local Development

1. **Start the Flask server**:

   ```bash
   python3 app.py
   ```

   The application will start on `http://0.0.0.0:5000` by default.

2. **Access the Web UI**:

   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. **Run a playbook**:
   - Leave both fields empty to run the default playbook on localhost
   - Or specify custom hosts and playbook paths as needed

#### Production Deployment

For production environments, use a WSGI server like **Gunicorn** or **uWSGI**:

##### Option 1: Using Gunicorn

1. Install Gunicorn:
   ```bash
   pip3 install gunicorn
   ```

2. Run the application:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

   - `-w 4`: Use 4 worker processes
   - `-b 0.0.0.0:5000`: Bind to all interfaces on port 5000

##### Option 2: Using uWSGI

1. Install uWSGI:
   ```bash
   pip3 install uwsgi
   ```

2. Run the application:
   ```bash
   uwsgi --http 0.0.0.0:5000 --wsgi-file app.py --callable app --processes 4 --threads 2
   ```

##### Option 3: Docker Deployment (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

RUN apt-get update && apt-get install -y ansible && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t snake-cogwheel .
docker run -p 5000:5000 snake-cogwheel
```

---

### Configuration

#### Environment Variables

You can customize the application using environment variables:

- `FLASK_ENV`: Set to `production` for production deployments (default: `development`)
- `FLASK_DEBUG`: Set to `0` to disable debug mode (default: `1`)

Example:
```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
python3 app.py
```

#### Security Considerations

⚠️ **Important**: This application executes system commands and should be deployed with proper security measures:

1. **Authentication**: Add user authentication before deploying to production
2. **Input Validation**: Validate and sanitize all user inputs
3. **Network Isolation**: Run behind a reverse proxy (nginx, Apache)
4. **File Permissions**: Restrict playbook access to authorized files only
5. **HTTPS**: Use SSL/TLS for encrypted communication

---

### Troubleshooting

#### Common Issues

1. **"ansible-playbook command not found"**
   - Ensure Ansible is installed and in your PATH
   - Verify with: `which ansible-playbook`

2. **"Playbook file not found"**
   - Check that the playbook path is correct
   - Use absolute paths or paths relative to the Flask app directory

3. **Permission denied errors**
   - Ensure the Flask app has read permissions for playbook files
   - Check SSH key permissions for remote host access

4. **Connection timeout**
   - Verify target hosts are reachable
   - Check SSH configuration and credentials
   - Test manually: `ansible -i <host>, -m ping`

---

### Usage Examples

#### Example 1: Run default playbook on localhost
- Leave both fields empty
- Click "Run Playbook"

#### Example 2: Run custom playbook on localhost
- Target Hosts: (leave empty)
- Playbook Path: `/path/to/my-playbook.yml`
- Click "Run Playbook"

#### Example 3: Run on remote hosts
- Target Hosts: `192.168.1.10,192.168.1.11,`
- Playbook Path: `deploy.yml`
- Click "Run Playbook"

---

## 📝 Development Notes

### Project Structure

- **app.py**: Main Flask application with route handlers and Ansible execution logic
- **templates/index.html**: Jinja2 template for the web UI
- **default_ping.yml**: Default playbook for connectivity testing
- **requirements.txt**: Python package dependencies

### Extending the Application

To add new features:

1. **Custom Playbooks**: Place additional playbooks in the project directory
2. **Inventory Management**: Extend the UI to support inventory file uploads
3. **User Authentication**: Integrate Flask-Login or similar
4. **Job History**: Add database support to store execution history
5. **Real-time Streaming**: Use WebSockets for live output streaming

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📄 License

This project is provided as-is for educational and operational purposes.

---

## 👥 Authors

- **Project**: Snake and CogWheel
- **Framework**: Flask + Ansible
- **Year**: 2025

---

## 🔗 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Ansible Documentation](https://docs.ansible.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)

---

**Happy Automating! 🐍⚙️**
