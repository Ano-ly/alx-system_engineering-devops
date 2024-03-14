# Installs Flask version 2.1.0
exec { 'Install flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  refreshonly => true
}
