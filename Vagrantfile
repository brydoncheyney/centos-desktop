# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|

  config.ssh.username = 'vagrant'
  config.ssh.password = 'vagrant'

  if Vagrant.has_plugin?("vagrant-cachier")
     config.cache.scope = :box
  end

  config.vm.define 'centos-7-desktop' do |desktop|
    desktop.vm.box = 'centos-7-desktop'
    if Vagrant.has_plugin?('vagrant-hosts')
      desktop.vm.provision :hosts
    end

    desktop.vm.synced_folder '.', '/work'

    desktop.vm.provider :virtualbox do |vb|
      vb.customize ['modifyvm', :id, '--clipboard', 'bidirectional']
    end

    desktop.vm.provision 'ansible' do |ansible|
      ansible.config_file = 'ansible/ansible.cfg'
      ansible.playbook = 'ansible/playbook.yml'
      ansible.sudo = true
      ansible.verbose = 'v'
      ansible.tags = 'all'
    end
  end

end
