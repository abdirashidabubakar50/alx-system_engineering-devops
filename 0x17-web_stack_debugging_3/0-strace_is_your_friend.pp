# 0-strace_is_your_friend.pp
# This Puppet manifest fixes the WordPress wp-settings.php file by replacing
# 'phpp' with 'php' to correct any typos in the file.

exec { 'fix-wordpress':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/bin:/bin',
  user    => 'root',
  group   => 'root',
  unless  => 'grep -q "phpp" /var/www/html/wp-settings.php',
  require => File['/var/www/html/wp-settings.php'],
}

file { '/var/www/html/wp-settings.php':
  ensure => file,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
}
