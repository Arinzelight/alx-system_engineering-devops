# Install Flask using pip3 with specific versions
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.0.2',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep -q "^Version: 2.1.0"',
}

