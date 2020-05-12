#!/bin/bash
#
#+--------------------------------------------------------------------+
#+ kali-lxc-setup.bash - by: Costa Kavidas (@ckavidas)                +
#+ intent:                                                            +
#+  - update/upgrade/install kali packages on a kali lxc container    +
#+  - Add a kali user for SSH, enable core dump                       +
#+  - Install x2go and kali xfce4                                     +
#+  - Enable and start SSH                                            +
#+                                                                    +
#+  Reference post: https://ckavidas.github.io/kali-lxc-05-2020       +
#+--------------------------------------------------------------------+
#
# Update and upgrade apt
apt update && apt upgrade -y

# Install kali packages
apt install kali-linux-default -y

# Install x2go and  kali's xfce4
apt install x2goserver x2goserver-xsession xfce4 kali-desktop-xfce -y

# Enable SSH
systemctl enable ssh
systemctl start ssh

# Add Kali user
adduser kali
# add kali to sudo group
usermod -aG sudo kali
# Add color to the terminal
sed -i '1 i\TERM=xterm-256color' /home/kali/.bashrc
# Enable core dump in container
echo 'Set disable_coredump false' > /etc/sudo.conf
