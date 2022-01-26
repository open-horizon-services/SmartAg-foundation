
# If SSH is disabled consider to create systemd service activated after 
# board is connected to the internet to run this just once
# https://raspberrypi.stackexchange.com/a/79033
#

# Remove previous registration
hzn unregister -Df

# Register new node
hzn register --policy /var/automationhub/edgenode_capabilities.json
