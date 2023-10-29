# This code uses Puppet to make changes to the configuration file.
# SSH configuration file should not require authentication.

file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  content => "
    Host your_server_ip_address
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
  mode    => '0600',
}
