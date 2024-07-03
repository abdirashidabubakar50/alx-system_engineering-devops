# This Puppet manifest kills a process named 'killmenow' using pkill.

exec { 'kill_killmenow_process':
  command     => '/usr/bin/pkill -f killmenow',
  path        => ['/usr/bin', '/bin', '/sbin', '/usr/sbin'],
  onlyif      => '/usr/bin/pgrep -fl killmenow',
  refreshonly => false, # Changed to false to ensure the command runs without needing a refresh event
}