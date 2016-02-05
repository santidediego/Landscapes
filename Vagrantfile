# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure('2') do |config|
    config.vm.box = 'azure'
    config.vm.network "public_network"
    config.vm.provider :azure do |azure, override|
        # Mandatory Settings
        azure.mgmt_certificate = File.expand_path('cert.pem')
        azure.mgmt_endpoint    = 'https://management.core.windows.net'
        azure.subscription_id = 'f9094523-9318-4f12-a0c7-a9792fe740bc'
        azure.vm_name     = 'landscapes-vagrantazure'
        azure.vm_image    = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
        azure.vm_size     = 'Small'
        config.vm.box     = 'azure'
        config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'



        # vm_password is optional when specifying the private_key_file with Linux VMs
        # When building a Windows VM and using WinRM this setting is used to authenticate via WinRM (PowerShell Remoting)
        #azure.vm_password = 'PROVIDE A VALID PASSWORD' # min 8 characters. should contain a lower case letter, an uppercase letter, a number and a special character

        # Optional Settings
        azure.vm_user = 'vagrant' # defaults to 'vagrant' if not provided
        #azure.cloud_service_name = 'azurevagrant'
        #azure.storage_acct_name  = 'azurevagrantstorage'
        #azure.deployment_name    = 'azurevagrantdeployment'
        azure.vm_location = 'Central US' # e.g., West US
        azure.ssh_port             = '22'
        azure.tcp_endpoints = '5000:80'
        azure.ssh_private_key_file = File.expand_path('cert.pem')

        # Optional *Nix Settings
        #azure.ssh_port = 'A VALID PUBLIC PORT' # defaults to 22
        #azure.private_key_file = 'Path to your ssh private key file (~/.ssh/id_rsa) to use for passwordless auth. If the id_rsa file is password protected, you will be prompted for the password.'

  #Provisionamiento
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/webservice.yml"
    ansible.inventory_path = "ansible/vagrant_ansible_inventory"
    #ansible.playbook = ".vagrant/provisioners/ansible/inventory/webservice.yml"
    #ansible.inventory_path = ".vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory"
  end
    end
end
