#dnf --disablerepo '*' --enablerepo=extras swap centos-linux-repos centos-stream-repos
#dnf distro-sync

image_name=centos
image_tag=python3.8
docker build -t ${image_name}:${image_tag} .
