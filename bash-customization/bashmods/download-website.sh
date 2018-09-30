function downloadWebSite(){
	wget -c --random-wait --limit-rate=512K -U mozilla --recursive --no-clobber --page-requisites -e robots=off --convert-links "$1"
}
