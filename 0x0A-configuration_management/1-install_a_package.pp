# Install flask

exec { 'install_flask':
  command => 'pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => 'pip3 show Flask | grep Version | grep -q 2.1.0',
}

#install Werkzeug
exec { 'install_werkzeug':
  command => 'pip3 install Werkzeug==2.1.1',
  path    => ['/usr/bin'],
  unless  => 'pip3 show Werkzeug | grep Version | grep -q 2.1.1',
}
