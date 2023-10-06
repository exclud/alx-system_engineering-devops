# 0x0E-web_stack_debugging_1

This folder contains scripts related to debugging web stacks, with a focus on issues concerning the Nginx web server not running on port 80. The scripts provided in this folder address the specific issue by making necessary configuration changes and restarting the services as needed.

## Files & Usage

### 1. 0-nginx_likes_port_80

This script addresses the issue where Nginx does not run on port 80 due to a misconfiguration in the `sites-enabled` and `sites-available` directories.

**Usage:**
./0-nginx_likes_port_80

**Steps Performed:**
1. Removes the default configuration file from the `sites-enabled` directory.
2. Creates a symbolic link from the `sites-available` directory to the `sites-enabled` directory.
3. Restarts the Nginx service to apply the configuration changes.

### 2. 1-debugging_made_short

This script provides a quicker method to address the issue of Nginx not running on port 80. 

**Usage:**
./1-debugging_made_short

**Steps Performed:**
1. Creates (or overwrites if exists) a symbolic link from the `sites-available` directory to the `sites-enabled` directory.
2. Starts the Nginx service.
3. Kills the first Nginx process that appears in the process list.

## Requirements & Dependencies

- These scripts are written in Bash and therefore need a Linux environment to run.
- Ensure that you have the appropriate permissions to execute these scripts and make configuration changes.
- These scripts are specifically tailored for configurations where Nginx settings are located in `/etc/nginx/sites-enabled` and `/etc/nginx/sites-available`.

## Disclaimer

Always backup your configuration and essential data before running any scripts that make changes to your system configuration. Use these scripts at your own risk.
