# Ensure file limits are set for all users
file { '/etc/security/limits.conf':
  ensure  => file,
  content => "/*\nsoft nofile 65536\nhard nofile 65536\n",
  notify  => Exec['reload_limits'],
}

# Ensure PAM limits are applied for interactive sessions
file { '/etc/pam.d/common-session':
  ensure  => file,
  content => "session required pam_limits.so\n",
  notify  => Exec['reload_pam'],
}

# Ensure PAM limits are applied for non-interactive sessions
file { '/etc/pam.d/common-session-noninteractive':
  ensure  => file,
  content => "session required pam_limits.so\n",
  notify  => Exec['reload_pam'],
}

# Set system-wide file descriptor limit
file { '/etc/sysctl.conf':
  ensure  => file,
  content => "fs.file-max = 65536\n",
  notify  => Exec['apply_sysctl'],
}

# Apply system configuration changes
exec { 'apply_sysctl':
  command     => '/sbin/sysctl -p',
  path        => ['/sbin', '/bin'],
  refreshonly => true,
}

# Reload PAM settings to apply limits
exec { 'reload_pam':
  command     => '/sbin/pam-auth-update --force',
  path        => ['/sbin', '/bin'],
  refreshonly => true,
}

# Reload limits configuration to apply changes
exec { 'reload_limits':
  command     => '/sbin/pam-auth-update --force',
  path        => ['/sbin', '/bin'],
  refreshonly => true,
}
