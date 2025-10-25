cisco_ios_config 'set_hostname_and_ssh' do
  config_lines [
    "hostname #{node['cisco_ios_config']['hostname']}",
	"ip domain-name #{node[cisco_ios_config]['domain_name']}",
	"crypto key generate rsa modulus 2048",
	"ip ssh version 2",
	"line vty 0 4",
	"transport input all",
	"login local"
  ]
  action :apply
end