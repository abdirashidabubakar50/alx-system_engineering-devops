# 0-strace_is_your_friend.pp
# This Puppet manifest fixes the WordPress wp-settings.php file by replacing
# 'phpp' with 'php' to correct any typos in the file.

exec { 'fix-wordpress':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}
