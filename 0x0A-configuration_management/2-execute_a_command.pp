#Puppet: killer of processes
exec { 'Kill kill_me_now':
  command => '/usr/bin/pkill killmenow',
}
