FILE=./cronfile
read -rp "Who are you? " USER
sudo crontab -u "$USER" "$FILE"
echo "Cron Job Installed"
