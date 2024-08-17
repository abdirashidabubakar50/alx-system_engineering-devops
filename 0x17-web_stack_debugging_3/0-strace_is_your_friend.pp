# 0-strace_is_your_friend.pp
# This manifest fixes the WordPress wp-settings.php file by replacing 'phpp' with 'php'

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wordpress/wp-settings.php',
  path    => ['/usr/bin', '/bin'], # Ensure the path to sed is included
  onlyif  => 'grep -q phpp /var/www/html/wordpress/wp-settings.php', # Only run if 'phpp' is found
  notify  => Exec['restart-apache'], # Notify to restart Apache if the change is made
}

exec { 'restart-apache':
  command     => '/usr/sbin/service apache2 restart',
  path        => ['/usr/sbin', '/usr/bin'], # Ensure the path to service is included
  refreshonly => true, # Only run if notified
}
