
# 0x07. Networking basics #0

The project includes Networking basics such as:
1. OSI model
2. Localhost
3. Positional parameters
## Setup

Since it is a requirment to start the each script with "#!/usr/bin/env bash", simply run this command in your working directory to ensure all files start with it. 
Then make them executable using chmod

```bash
for file in *; do echo '#!/usr/bin/env bash'|cat - "$file" > temp && mv temp "$file"; done
```
You need to install net-tools in order to execute the scripts.

For Arch linux, run: 
```bash
sudo pacman -S net-tools
```
For Ubuntu, run:
```bash
 sudo apt-get install net-tools
```

