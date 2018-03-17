#! /usr/bin/env bash
#NoGuiLinux

apache_doc_root="/srv/samba"
packages=("apache" "mysql" "php" "php-apache" "phpadmin" "php-sodium")
systemctl_cmds=("start" "enable")
deps=('pacman')
function pacmanCheck(){
	#check to see if pacman exists in the currently running system
	for dep in ${deps[@]} ; do
		if ! bash depCheck.sh "$dep"; then
			exit 1
		fi
	done
}

function rootCheck(){
	if test `whoami` != "root" ; then
		printf "\e[1;33;40m%s\e[0;m\n" "you are not root/sudo!"
		exit 1
	fi
}
function installPackages(){
	pacman -S ${packages[@]}
}

function systemctlRun(){
	SERVICE="$1"
	for i in ${systemctl_cmds[@]} ; do
		systemctl "$i" "$SERVICE"
	done
}

function installApache(){
	sed s\|^'LoadModule unique_id_module modules/mod_unique_id.so'\|'#LoadModule unique_id_module modules/mod_unique_id.so'\|g -i /etc/httpd/conf/httpd.conf
	systemctlRun httpd
}

function testHtml(){
cat > "$apache_doc_root""/test.html" << EOF
<html>
<title>Welcome to the Lamp Test for the Apache Server installation</title>
	<body>
		<h1>This is the Apache Test Page<h1>
	</body>
</html>
EOF
 
}

function installMySQL(){
	mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/myqsql
	systemctlRun mysqld
	mysql_secure_installation
}

function testPhp(){
 cat > "$apache_doc_root""/test.php" << EOF
<?php
	phpinfo();
?>
EOF
}

function installPhp(){
	sed -i s\|^'LoadModule mpm_event_module modules/mod_mpm_event.so'\|'#LoadModule mpm_event_module modules/mod_mpm_event.so'\|g /etc/httpd/conf/httpd.conf
cat >> /etc/httpd/conf/httpd.conf << EOF
LoadModule mpm_prefork_module modules/mod_mpm_prefork.so
LoadModule php7_module modules/libphp7.so
AddHandler php-script php
Include conf/extra/php7_module.conf
EOF
	systemctlRun httpd
}

function phpMyAdminCfg(){
cat > /etc/httpd/conf/extra/phpmyadmin.conf << EOF
Alias /phpmyadmin "/usr/share/webapps/phpMyAdmin"
<Directory "/usr/share/webapps/phpMyAdmin">
	DirectoryIndex index.php
	AllowOverride All
	options FollowSymlinks
	Require all granted
</Directory>
EOF
}

function installPhpMyAdmin(){
	ext=( "bz2" "mysqli")
cat >> /etc/php/php.ini << EOF
extension=sodium
EOF
	for i in ${ext[@]} ; do
		sed s\|^";extension=$i"\|"extension=$i"\|g /etc/php/php.ini -i
	done
	phpMyAdminCfg
cat >> /etc/httpd/conf/httpd.conf << EOF
Include conf/extra/phpmyadmin.conf
EOF
	systemctl restart httpd
}

function blowFish(){
	read -rp "what is your blowfish secret? : " blow
	secret=`python3 blowfishSecretGen.py "$blow"`
	sed -i s\|"\$cfg\['blowfish_secret'\] = '';"\|"\$cfg\['blowfish_secret'\] = \'$secret';"\|g /etc/webapps/phpmyadmin/config.inc.php
	sudo systemctl restart httpd
}
function main(){
	rootCheck
	pacmanCheck
	installPackages
	installApache
	installMySQL
	installPhp
	installPhpMyAdmin
	testHtml
	testPhp
	blowFish
}
main
