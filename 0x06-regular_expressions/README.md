0x06-regular_expressions

The project includes scripts on Regex. 


## Setup

Since it is a requirment to start the each script with "#!/usr/bin/env ruby", simply run this command in your working directory to ensure all files start with it. 
Then make them executable using chmod

```bash
for file in *; do echo '#!/usr/bin/env ruby' | cat - "$file" > temp && mv temp "$file"; done
```