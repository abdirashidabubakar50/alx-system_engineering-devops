# Increase the number of open files limit for all users
file { '/etc/security/limits.conf':
  ensure  => file,
  content => "/*\nsoft nofile 65536\nhard nofile 65536\n",
  notify  => Exec['reload-limits'],
}

# Ensure PAM limits are applied
file { '/etc/pam.d/common-session':
  ensure  => file,
  content => "session required pam_limits.so\n",
  notify  => Exec['reload-pam'],
}

file { '/etc/pam.d/common-session-noninteractive':
  ensure  => file,
  content => "session required pam_limits.so\n",
  notify  => Exec['reload-pam'],
}

# Set system-wide file descriptor limit
file { '/etc/sysctl.conf':
  ensure  => file,
  content => "fs.file-max = 65536\n",
  notify  => Exec['apply-sysctl'],
}

# Apply system configuration
exec { 'apply-sysctl':
  command => '/sbin/sysctl -p',
  path    => ['/sbin', '/bin'],
  refreshonly => true,
}

# Reload PAM settings
exec { 'reload-pam':
  command => '/sbin/pam-auth-update --force',
  path    => ['/sbin', '/bin'],
  refreshonly => true,
}

# Reload limits configuration
exec { 'reload-limits':
  command => '/sbin/pam-auth-update --force',
  path    => ['/sbin', '/bin'],
  refreshonly => true,
}
