# Ensure limits.conf is configured correctly
file { '/etc/security/limits.conf':
  ensure  => file,
  content => "
*                soft    nofile           65536
*                hard    nofile           65536
",
  notify  => Exec['apply_sysctl'], # Notify to reapply sysctl settings
}

# Ensure common-session PAM file is configured
file { '/etc/pam.d/common-session':
  ensure  => file,
  content => "session required pam_limits.so\n",
}

# Ensure common-session-noninteractive PAM file is configured
file { '/etc/pam.d/common-session-noninteractive':
  ensure  => file,
  content => "session required pam_limits.so\n",
}

# Ensure sysctl.conf is updated for file descriptor limits
file { '/etc/sysctl.conf':
  ensure  => file,
  content => "fs.file-max = 65536\n",
  notify  => Exec['apply_sysctl'], # Notify to reapply sysctl settings
}

# Apply sysctl settings
exec { 'apply_sysctl':
  command     => '/sbin/sysctl -p',
  refreshonly => true,
}

# Ensure limits are applied to PAM configuration
exec { 'reload_pam':
  command     => '/usr/sbin/pam-auth-update --force', # Update PAM configuration
  path        => ['/usr/sbin', '/usr/bin'],
  refreshonly => true,
}
