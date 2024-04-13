# Fix Apache on an Ubuntu Machine
file { '/var/www/html/index.html':
  ensure  => file,
  content => '<!DOCTYPE HTML><HTML></HTML>',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
