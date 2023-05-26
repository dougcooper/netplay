Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/kinetic64"

    #nat
    config.vm.network "public_network"
    
    #internal network to talk to yocto
    config.vm.network "private_network", type: "dhcp"

    config.vm.provision "shell", path: "provision.sh" do |s|
        s.privileged = false
    end
end