# This Puppet manifest kills a process named 'killmenow' using pkill.

exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  refreshonly => true,
}
