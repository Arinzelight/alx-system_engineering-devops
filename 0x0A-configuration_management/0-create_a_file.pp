#create a file in /tmp

file{
	'/tmp/scool':
	content => 'I love puppet',
	mode 	=> '0744',
	owner 	=> 'www-data',
	group 	=> 'www-data',

}