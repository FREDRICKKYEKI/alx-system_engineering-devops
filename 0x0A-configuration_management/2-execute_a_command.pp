# Using Puppet, create a manifest that kills a process named killmenow.

# Requirements:

# Must use the exec Puppet resource
# Must use pkill

exec { 'pkill killmenow':
  path     => '/usr/bin',
  command  => 'pkill killmenow',
  provider => shell,
  returns  => [0, 1]
}
