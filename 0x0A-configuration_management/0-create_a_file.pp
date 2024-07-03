# This Puppet manifest creates a file at /tmp/school with specific content, permissions, owner, and group.

file { '/tmp/school':
    ensure  => 'file',
    content => 'I love puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}