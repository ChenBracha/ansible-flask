#!/usr/bin/env python3
"""
Snake and CogWheel - Flask Ansible Playbook Runner
A web UI for executing Ansible playbooks with dynamic inventory and playbook selection.
"""

from flask import Flask, render_template, request
import subprocess
import os
import glob

app = Flask(__name__)


def get_available_playbooks():
    """Scan for available playbook files in the current directory."""
    playbooks = []
    
    # Get all .yml and .yaml files in current directory
    yml_files = glob.glob('*.yml') + glob.glob('*.yaml')
    
    # Also check playbooks subdirectory if it exists
    if os.path.exists('playbooks'):
        yml_files.extend(glob.glob('playbooks/*.yml'))
        yml_files.extend(glob.glob('playbooks/*.yaml'))
    
    # Filter out non-playbook files
    excluded_files = ['docker-compose.yml', 'requirements.yml']
    yml_files = [f for f in yml_files if os.path.basename(f).lower() not in excluded_files]
    
    for playbook in sorted(yml_files):
        # Get filename without path for display
        display_name = os.path.basename(playbook)
        
        # Add description based on filename
        if 'default' in playbook.lower() and 'ping' in playbook.lower():
            description = 'Connectivity Test (Default)'
        elif 'ping' in playbook.lower():
            description = 'Connectivity Test'
        elif 'system_info' in playbook.lower() or 'system-info' in playbook.lower():
            description = 'System Information & Health Check'
        elif 'workspace' in playbook.lower():
            description = 'Create Development Workspace'
        else:
            description = 'Custom Playbook'
        
        playbooks.append({
            'path': playbook,
            'name': display_name,
            'description': description
        })
    
    return playbooks


@app.route('/')
def index():
    """Render the main form page with available playbooks."""
    playbooks = get_available_playbooks()
    return render_template('index.html', playbooks=playbooks)


@app.route('/run', methods=['POST'])
def run_playbook():
    """
    Handle playbook execution based on user input.
    
    Defaults:
    - If no target_hosts provided, uses 'localhost,'
    - If no playbook_path provided, uses 'default_ping.yml'
    """
    # Get form data
    target_hosts = request.form.get('target_hosts', '').strip()
    playbook_path = request.form.get('playbook_path', '').strip()
    
    # Apply defaults
    use_localhost_direct = False
    if not target_hosts or target_hosts.lower() == 'localhost':
        target_hosts = 'localhost,'
        inventory_display = 'localhost (default)'
        use_localhost_direct = True
    else:
        inventory_display = target_hosts
    
    if not playbook_path:
        playbook_path = 'default_ping.yml'
        playbook_display = 'default_ping.yml (default)'
    else:
        playbook_display = playbook_path
    
    # Verify playbook exists
    if not os.path.exists(playbook_path):
        error_msg = f"Error: Playbook file '{playbook_path}' not found."
        return render_template(
            'index.html',
            playbooks=get_available_playbooks(),
            inventory=inventory_display,
            playbook=playbook_display,
            results=error_msg,
            error=True
        )
    
    # Construct ansible-playbook command
    if use_localhost_direct:
        # Use explicit localhost with comma and connection local
        command = [
            'ansible-playbook',
            '-i', 'localhost,',
            '--connection=local',
            '-e', 'ansible_python_interpreter=auto',
            playbook_path
        ]
    else:
        command = [
            'ansible-playbook',
            '-i', target_hosts,
        ]
        
        # Add connection=local for localhost to avoid SSH
        if target_hosts.strip().rstrip(',').lower() == 'localhost':
            command.extend(['--connection=local'])
        
        command.append(playbook_path)
    
    # Execute the command
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        # Combine stdout and stderr for complete output
        output = result.stdout
        if result.stderr:
            output += "\n--- STDERR ---\n" + result.stderr
        
        # Add return code information
        if result.returncode != 0:
            output += f"\n\n[Process exited with code {result.returncode}]"
        else:
            output += f"\n\n[Process completed successfully]"
        
    except subprocess.TimeoutExpired:
        output = "Error: Playbook execution timed out (exceeded 5 minutes)."
    except FileNotFoundError:
        output = "Error: 'ansible-playbook' command not found. Please ensure Ansible is installed."
    except Exception as e:
        output = f"Error executing playbook: {str(e)}"
    
    # Render results
    return render_template(
        'index.html',
        playbooks=get_available_playbooks(),
        inventory=inventory_display,
        playbook=playbook_display,
        results=output,
        error=result.returncode != 0 if 'result' in locals() else True
    )


if __name__ == '__main__':
    # Run in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
