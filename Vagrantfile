# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.box = 'centos-7-desktop'
  config.vm.hostname = 'centos-7-desktop'

  config.ssh.username = 'vagrant'
  config.ssh.password = 'vagrant'

  config.vm.define 'centos-7-desktop' do |instance|
    if Vagrant.has_plugin?('vagrant-hosts')
      instance.vm.provision :hosts
    end
  end

end
