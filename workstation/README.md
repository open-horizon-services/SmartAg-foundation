
###
### https://medium.com/@ifeanyiigili/how-to-setup-a-private-docker-registry-with-a-self-sign-certificate-43a7407a1613
###

# Register certificates for custom regostry server
mkdir -p /etc/docker/certs.d/192.168.1.36:5000
cp domain.crt /etc/docker/certs.d/192.168.1.36:5000
cp domain.crt /usr/local/share/ca-certificates/ca.crt
update-ca-certificates

# MacOS (add trusted root to keychain)
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ./domain.crt 

# Linux (TBD)

# RESTART docker service to use updated certificates
