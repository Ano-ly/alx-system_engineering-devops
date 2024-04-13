# Fix Apache on an Ubuntu Machine
exec { 'Fix_the_php':
  command  => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  provider => shell,
}
