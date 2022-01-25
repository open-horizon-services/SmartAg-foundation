#!/bin/bash
# (c) Copyright 2021-present Oleksandr Ivanov, All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
set +e

# Assume some errors will happen
ERR=/boot/errors.txt
touch /boot/errors.txt

echo "Init">>$ERR
FIRSTUSER=`getent passwd 1000 | cut -d: -f1`
FIRSTUSERHOME=`getent passwd 1000 | cut -d: -f6`
echo "chpasswd -e">>$ERR
echo "$FIRSTUSER:"'$5$Op3pINN5Vg$R4Y2YJLp7NRNIiJ8KxbHbyJ.8IcLtc.5C3CE/heMIC.' | chpasswd -e

systemctl enable ssh

echo "systemctl enable ssh">>$ERR

# Unpack all patched files
echo "unzip into /tmp/edgenode">>$ERR
unzip -o /boot/ospatch.zip -d /
echo "Override all files from archive">>$ERR
cp -r /tmp/edgenode/* /

# Set RO access for others for all files unpacked from archive
echo "Set RO access for others for all files unpacked from archive">>$ERR
find /tmp/edgenode/ -type f -exec sh -c "echo {} | sed 's/^\(\/tmp\/edgenode\)*//' | xargs chmod 644" \;

# Set root only access
echo "Set root only access">>$ERR
chmod 600 /etc/wpa_supplicant/wpa_supplicant.conf

echo "Unblock wifi">>$ERR
rfkill unblock wifi
for filename in /var/lib/systemd/rfkill/*:wlan ; do
  echo 0 > $filename
done
echo "rm -f /etc/xdg/autostart/piwiz.desktop">>$ERR
rm -f /etc/xdg/autostart/piwiz.desktop
echo "rm -f /etc/localtime">>$ERR
rm -f /etc/localtime

echo "dpkg-reconfigure -f noninteractive tzdata">>$ERR
dpkg-reconfigure -f noninteractive tzdata

echo "dpkg-reconfigure -f noninteractive keyboard-configuration">>$ERR
dpkg-reconfigure -f noninteractive keyboard-configuration

# Remove this file
echo "rm -f /boot/firstrun.sh">>$ERR
rm -f /boot/firstrun.sh

echo "sed -i 's| systemd.run.*||g' /boot/cmdline.txt">>$ERR
sed -i 's| systemd.run.*||g' /boot/cmdline.txt

# Remove OS patch archive
echo "rm -f /boot/ospatch.zip">>$ERR
rm -f /boot/ospatch.zip

# rm -f /boot/errors.txt
exit 0
