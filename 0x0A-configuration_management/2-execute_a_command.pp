# Puppet manifest to kill a process named "killmenow" using pkill

exec{'pkill -f killmenow':
path  => '/usr/bin/:/usr/local/bin/:/bin/'
}
