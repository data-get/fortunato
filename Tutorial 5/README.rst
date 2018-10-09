Client 
sudo apt install openssh-server

Host Computer
ansible-playbook -i hosts --ask-become-pass tutorial5.yml -k --ask-vault-pass
