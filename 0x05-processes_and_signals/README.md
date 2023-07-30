
0x05. Processes and signals

The project includes scripts about Linux proccesses and signals. 


## Setup

Since it is a requirment to start the each script with "#!/usr/bin/env bash", simply run this command in your working directory to ensure all files start with it. 
Then make them executable using chmod

```bash
for file in *; do echo '#!/usr/bin/env bash' | cat - "$file" > temp && mv temp "$file"; done
```

All files are executable and you just need to run them
For example
'''
 ./0-what-is-my-pid
'''
