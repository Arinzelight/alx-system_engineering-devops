#!/usr/bin/pup

#  install flask version (2.10) from pip3

package{'flask':
	ensure => '2.1.0',
	provider => 'pip3',

}
