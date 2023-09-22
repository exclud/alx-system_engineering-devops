# Puppet manifest to install Flask using pip3

# Ensure pip3 is installed (you can omit this if pip3 is already installed)
package { 'python3-pip':
  ensure => 'installed',
}

# Install Flask using pip3 with the specified version
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'], # Ensure pip3 is installed first
}
