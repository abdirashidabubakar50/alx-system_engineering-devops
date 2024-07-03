# This Puppet manifest install Flask version 2.1.0 using pip3



package { 'python3-pip':
    ensure  => 'installed',
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install werkzeug==2.1.1',
  unless  => '/usr/bin/pip3 show werkzeug | grep Version | grep -q 2.1.1',
  require => Package['python3-pip'],
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep Version | grep -q 2.1.0',
  require => Exec['install_werkzeug'],
}