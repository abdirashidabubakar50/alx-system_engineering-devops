# Puppet manifest to configure SSH client settings

# Ensure SSH client configuration file exists
file { '/etc/ssh/ssh_config':
  ensure => file,
}

# Configure SSH client to use specified private key and disable password authentication
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  ensure  => present,
}

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  ensure  => present,
}
