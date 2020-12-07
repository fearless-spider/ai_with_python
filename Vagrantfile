# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure('2') do |config|
  config.vm.box      = 'ubuntu/bionic64'
  config.vm.hostname = 'ai-with-python'

  config.vm.network :forwarded_port, guest: 3000, host: 3000
  config.vm.network :forwarded_port, guest: 8888, host: 8888

  config.vm.provider "virtualbox" do |v|
    v.memory = 512
    v.cpus = 2
  end

  config.vm.provision :shell, path: 'bootstrap.sh', keep_color: true
  config.vm.synced_folder "notebooks/", "/home/vagrant/notebooks"
  config.vm.synced_folder "models/", "/home/vagrant/models"

end