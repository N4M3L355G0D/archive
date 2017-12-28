if [ "`pacman -Qqe barrage`" != 'barrage' ] ; then
	yaourt -S barrage
	if [ $? == 0 ] ; then
		echo "barrage: installed"
	else
		echo "barrage: !not installed: install failure"
	fi
else
	echo "barrage: !installed as already installed."
fi
if [ "`pacman -Qqe bigreqsproto`" != 'bigreqsproto' ] ; then
	yaourt -S bigreqsproto
	if [ $? == 0 ] ; then
		echo "bigreqsproto: installed"
	else
		echo "bigreqsproto: !not installed: install failure"
	fi
else
	echo "bigreqsproto: !installed as already installed."
fi
if [ "`pacman -Qqe bluez`" != 'bluez' ] ; then
	yaourt -S bluez
	if [ $? == 0 ] ; then
		echo "bluez: installed"
	else
		echo "bluez: !not installed: install failure"
	fi
else
	echo "bluez: !installed as already installed."
fi
if [ "`pacman -Qqe bzflag`" != 'bzflag' ] ; then
	yaourt -S bzflag
	if [ $? == 0 ] ; then
		echo "bzflag: installed"
	else
		echo "bzflag: !not installed: install failure"
	fi
else
	echo "bzflag: !installed as already installed."
fi
if [ "`pacman -Qqe cups`" != 'cups' ] ; then
	yaourt -S cups
	if [ $? == 0 ] ; then
		echo "cups: installed"
	else
		echo "cups: !not installed: install failure"
	fi
else
	echo "cups: !installed as already installed."
fi
if [ "`pacman -Qqe dialog`" != 'dialog' ] ; then
	yaourt -S dialog
	if [ $? == 0 ] ; then
		echo "dialog: installed"
	else
		echo "dialog: !not installed: install failure"
	fi
else
	echo "dialog: !installed as already installed."
fi
if [ "`pacman -Qqe dri2proto`" != 'dri2proto' ] ; then
	yaourt -S dri2proto
	if [ $? == 0 ] ; then
		echo "dri2proto: installed"
	else
		echo "dri2proto: !not installed: install failure"
	fi
else
	echo "dri2proto: !installed as already installed."
fi
if [ "`pacman -Qqe dri3proto`" != 'dri3proto' ] ; then
	yaourt -S dri3proto
	if [ $? == 0 ] ; then
		echo "dri3proto: installed"
	else
		echo "dri3proto: !not installed: install failure"
	fi
else
	echo "dri3proto: !installed as already installed."
fi
if [ "`pacman -Qqe edac-utils`" != 'edac-utils' ] ; then
	yaourt -S edac-utils
	if [ $? == 0 ] ; then
		echo "edac-utils: installed"
	else
		echo "edac-utils: !not installed: install failure"
	fi
else
	echo "edac-utils: !installed as already installed."
fi
if [ "`pacman -Qqe firefox-adblock-plus`" != 'firefox-adblock-plus' ] ; then
	yaourt -S firefox-adblock-plus
	if [ $? == 0 ] ; then
		echo "firefox-adblock-plus: installed"
	else
		echo "firefox-adblock-plus: !not installed: install failure"
	fi
else
	echo "firefox-adblock-plus: !installed as already installed."
fi
if [ "`pacman -Qqe firefox-extension-image-block`" != 'firefox-extension-image-block' ] ; then
	yaourt -S firefox-extension-image-block
	if [ $? == 0 ] ; then
		echo "firefox-extension-image-block: installed"
	else
		echo "firefox-extension-image-block: !not installed: install failure"
	fi
else
	echo "firefox-extension-image-block: !installed as already installed."
fi
if [ "`pacman -Qqe foomatic-db-gutenprint-ppds`" != 'foomatic-db-gutenprint-ppds' ] ; then
	yaourt -S foomatic-db-gutenprint-ppds
	if [ $? == 0 ] ; then
		echo "foomatic-db-gutenprint-ppds: installed"
	else
		echo "foomatic-db-gutenprint-ppds: !not installed: install failure"
	fi
else
	echo "foomatic-db-gutenprint-ppds: !installed as already installed."
fi
if [ "`pacman -Qqe glproto`" != 'glproto' ] ; then
	yaourt -S glproto
	if [ $? == 0 ] ; then
		echo "glproto: installed"
	else
		echo "glproto: !not installed: install failure"
	fi
else
	echo "glproto: !installed as already installed."
fi
if [ "`pacman -Qqe gnome-themes-standard`" != 'gnome-themes-standard' ] ; then
	yaourt -S gnome-themes-standard
	if [ $? == 0 ] ; then
		echo "gnome-themes-standard: installed"
	else
		echo "gnome-themes-standard: !not installed: install failure"
	fi
else
	echo "gnome-themes-standard: !installed as already installed."
fi
if [ "`pacman -Qqe groff`" != 'groff' ] ; then
	yaourt -S groff
	if [ $? == 0 ] ; then
		echo "groff: installed"
	else
		echo "groff: !not installed: install failure"
	fi
else
	echo "groff: !installed as already installed."
fi
if [ "`pacman -Qqe gstreamer0.10-bad`" != 'gstreamer0.10-bad' ] ; then
	yaourt -S gstreamer0.10-bad
	if [ $? == 0 ] ; then
		echo "gstreamer0.10-bad: installed"
	else
		echo "gstreamer0.10-bad: !not installed: install failure"
	fi
else
	echo "gstreamer0.10-bad: !installed as already installed."
fi
if [ "`pacman -Qqe gstreamer0.10-good`" != 'gstreamer0.10-good' ] ; then
	yaourt -S gstreamer0.10-good
	if [ $? == 0 ] ; then
		echo "gstreamer0.10-good: installed"
	else
		echo "gstreamer0.10-good: !not installed: install failure"
	fi
else
	echo "gstreamer0.10-good: !installed as already installed."
fi
if [ "`pacman -Qqe gstreamer0.10-ugly`" != 'gstreamer0.10-ugly' ] ; then
	yaourt -S gstreamer0.10-ugly
	if [ $? == 0 ] ; then
		echo "gstreamer0.10-ugly: installed"
	else
		echo "gstreamer0.10-ugly: !not installed: install failure"
	fi
else
	echo "gstreamer0.10-ugly: !installed as already installed."
fi
if [ "`pacman -Qqe gutenprint`" != 'gutenprint' ] ; then
	yaourt -S gutenprint
	if [ $? == 0 ] ; then
		echo "gutenprint: installed"
	else
		echo "gutenprint: !not installed: install failure"
	fi
else
	echo "gutenprint: !installed as already installed."
fi
if [ "`pacman -Qqe jre`" != 'jre' ] ; then
	yaourt -S jre
	if [ $? == 0 ] ; then
		echo "jre: installed"
	else
		echo "jre: !not installed: install failure"
	fi
else
	echo "jre: !installed as already installed."
fi
if [ "`pacman -Qqe lib32-curl`" != 'lib32-curl' ] ; then
	yaourt -S lib32-curl
	if [ $? == 0 ] ; then
		echo "lib32-curl: installed"
	else
		echo "lib32-curl: !not installed: install failure"
	fi
else
	echo "lib32-curl: !installed as already installed."
fi
if [ "`pacman -Qqe lib32-mesa`" != 'lib32-mesa' ] ; then
	yaourt -S lib32-mesa
	if [ $? == 0 ] ; then
		echo "lib32-mesa: installed"
	else
		echo "lib32-mesa: !not installed: install failure"
	fi
else
	echo "lib32-mesa: !installed as already installed."
fi
if [ "`pacman -Qqe lib32-mesa-demos`" != 'lib32-mesa-demos' ] ; then
	yaourt -S lib32-mesa-demos
	if [ $? == 0 ] ; then
		echo "lib32-mesa-demos: installed"
	else
		echo "lib32-mesa-demos: !not installed: install failure"
	fi
else
	echo "lib32-mesa-demos: !installed as already installed."
fi
if [ "`pacman -Qqe linux`" != 'linux' ] ; then
	yaourt -S linux
	if [ $? == 0 ] ; then
		echo "linux: installed"
	else
		echo "linux: !not installed: install failure"
	fi
else
	echo "linux: !installed as already installed."
fi
if [ "`pacman -Qqe linux-headers`" != 'linux-headers' ] ; then
	yaourt -S linux-headers
	if [ $? == 0 ] ; then
		echo "linux-headers: installed"
	else
		echo "linux-headers: !not installed: install failure"
	fi
else
	echo "linux-headers: !installed as already installed."
fi
if [ "`pacman -Qqe mariadb`" != 'mariadb' ] ; then
	yaourt -S mariadb
	if [ $? == 0 ] ; then
		echo "mariadb: installed"
	else
		echo "mariadb: !not installed: install failure"
	fi
else
	echo "mariadb: !installed as already installed."
fi
if [ "`pacman -Qqe mc-skin-modarin-debian`" != 'mc-skin-modarin-debian' ] ; then
	yaourt -S mc-skin-modarin-debian
	if [ $? == 0 ] ; then
		echo "mc-skin-modarin-debian: installed"
	else
		echo "mc-skin-modarin-debian: !not installed: install failure"
	fi
else
	echo "mc-skin-modarin-debian: !installed as already installed."
fi
if [ "`pacman -Qqe mesa-demos`" != 'mesa-demos' ] ; then
	yaourt -S mesa-demos
	if [ $? == 0 ] ; then
		echo "mesa-demos: installed"
	else
		echo "mesa-demos: !not installed: install failure"
	fi
else
	echo "mesa-demos: !installed as already installed."
fi
if [ "`pacman -Qqe package-query`" != 'package-query' ] ; then
	yaourt -S package-query
	if [ $? == 0 ] ; then
		echo "package-query: installed"
	else
		echo "package-query: !not installed: install failure"
	fi
else
	echo "package-query: !installed as already installed."
fi
if [ "`pacman -Qqe pmacct`" != 'pmacct' ] ; then
	yaourt -S pmacct
	if [ $? == 0 ] ; then
		echo "pmacct: installed"
	else
		echo "pmacct: !not installed: install failure"
	fi
else
	echo "pmacct: !installed as already installed."
fi
if [ "`pacman -Qqe ppp`" != 'ppp' ] ; then
	yaourt -S ppp
	if [ $? == 0 ] ; then
		echo "ppp: installed"
	else
		echo "ppp: !not installed: install failure"
	fi
else
	echo "ppp: !installed as already installed."
fi
if [ "`pacman -Qqe presentproto`" != 'presentproto' ] ; then
	yaourt -S presentproto
	if [ $? == 0 ] ; then
		echo "presentproto: installed"
	else
		echo "presentproto: !not installed: install failure"
	fi
else
	echo "presentproto: !installed as already installed."
fi
if [ "`pacman -Qqe projectlibre`" != 'projectlibre' ] ; then
	yaourt -S projectlibre
	if [ $? == 0 ] ; then
		echo "projectlibre: installed"
	else
		echo "projectlibre: !not installed: install failure"
	fi
else
	echo "projectlibre: !installed as already installed."
fi
if [ "`pacman -Qqe pulseaudio-alsa`" != 'pulseaudio-alsa' ] ; then
	yaourt -S pulseaudio-alsa
	if [ $? == 0 ] ; then
		echo "pulseaudio-alsa: installed"
	else
		echo "pulseaudio-alsa: !not installed: install failure"
	fi
else
	echo "pulseaudio-alsa: !installed as already installed."
fi
if [ "`pacman -Qqe python`" != 'python' ] ; then
	yaourt -S python
	if [ $? == 0 ] ; then
		echo "python: installed"
	else
		echo "python: !not installed: install failure"
	fi
else
	echo "python: !installed as already installed."
fi
if [ "`pacman -Qqe python-pillow`" != 'python-pillow' ] ; then
	yaourt -S python-pillow
	if [ $? == 0 ] ; then
		echo "python-pillow: installed"
	else
		echo "python-pillow: !not installed: install failure"
	fi
else
	echo "python-pillow: !installed as already installed."
fi
if [ "`pacman -Qqe python2`" != 'python2' ] ; then
	yaourt -S python2
	if [ $? == 0 ] ; then
		echo "python2: installed"
	else
		echo "python2: !not installed: install failure"
	fi
else
	echo "python2: !installed as already installed."
fi
if [ "`pacman -Qqe resourceproto`" != 'resourceproto' ] ; then
	yaourt -S resourceproto
	if [ $? == 0 ] ; then
		echo "resourceproto: installed"
	else
		echo "resourceproto: !not installed: install failure"
	fi
else
	echo "resourceproto: !installed as already installed."
fi
if [ "`pacman -Qqe rssowl`" != 'rssowl' ] ; then
	yaourt -S rssowl
	if [ $? == 0 ] ; then
		echo "rssowl: installed"
	else
		echo "rssowl: !not installed: install failure"
	fi
else
	echo "rssowl: !installed as already installed."
fi
if [ "`pacman -Qqe sysstat`" != 'sysstat' ] ; then
	yaourt -S sysstat
	if [ $? == 0 ] ; then
		echo "sysstat: installed"
	else
		echo "sysstat: !not installed: install failure"
	fi
else
	echo "sysstat: !installed as already installed."
fi
if [ "`pacman -Qqe system-config-printer`" != 'system-config-printer' ] ; then
	yaourt -S system-config-printer
	if [ $? == 0 ] ; then
		echo "system-config-printer: installed"
	else
		echo "system-config-printer: !not installed: install failure"
	fi
else
	echo "system-config-printer: !installed as already installed."
fi
if [ "`pacman -Qqe tcl`" != 'tcl' ] ; then
	yaourt -S tcl
	if [ $? == 0 ] ; then
		echo "tcl: installed"
	else
		echo "tcl: !not installed: install failure"
	fi
else
	echo "tcl: !installed as already installed."
fi
if [ "`pacman -Qqe thc-ipv6`" != 'thc-ipv6' ] ; then
	yaourt -S thc-ipv6
	if [ $? == 0 ] ; then
		echo "thc-ipv6: installed"
	else
		echo "thc-ipv6: !not installed: install failure"
	fi
else
	echo "thc-ipv6: !installed as already installed."
fi
if [ "`pacman -Qqe ttf-tahoma`" != 'ttf-tahoma' ] ; then
	yaourt -S ttf-tahoma
	if [ $? == 0 ] ; then
		echo "ttf-tahoma: installed"
	else
		echo "ttf-tahoma: !not installed: install failure"
	fi
else
	echo "ttf-tahoma: !installed as already installed."
fi
if [ "`pacman -Qqe urbanterror`" != 'urbanterror' ] ; then
	yaourt -S urbanterror
	if [ $? == 0 ] ; then
		echo "urbanterror: installed"
	else
		echo "urbanterror: !not installed: install failure"
	fi
else
	echo "urbanterror: !installed as already installed."
fi
if [ "`pacman -Qqe urbanterror-data`" != 'urbanterror-data' ] ; then
	yaourt -S urbanterror-data
	if [ $? == 0 ] ; then
		echo "urbanterror-data: installed"
	else
		echo "urbanterror-data: !not installed: install failure"
	fi
else
	echo "urbanterror-data: !installed as already installed."
fi
if [ "`pacman -Qqe vi`" != 'vi' ] ; then
	yaourt -S vi
	if [ $? == 0 ] ; then
		echo "vi: installed"
	else
		echo "vi: !not installed: install failure"
	fi
else
	echo "vi: !installed as already installed."
fi
if [ "`pacman -Qqe webkit2gtk`" != 'webkit2gtk' ] ; then
	yaourt -S webkit2gtk
	if [ $? == 0 ] ; then
		echo "webkit2gtk: installed"
	else
		echo "webkit2gtk: !not installed: install failure"
	fi
else
	echo "webkit2gtk: !installed as already installed."
fi
if [ "`pacman -Qqe windows8-cursor`" != 'windows8-cursor' ] ; then
	yaourt -S windows8-cursor
	if [ $? == 0 ] ; then
		echo "windows8-cursor: installed"
	else
		echo "windows8-cursor: !not installed: install failure"
	fi
else
	echo "windows8-cursor: !installed as already installed."
fi
if [ "`pacman -Qqe wings3d`" != 'wings3d' ] ; then
	yaourt -S wings3d
	if [ $? == 0 ] ; then
		echo "wings3d: installed"
	else
		echo "wings3d: !not installed: install failure"
	fi
else
	echo "wings3d: !installed as already installed."
fi
if [ "`pacman -Qqe wpa_supplicant_gui`" != 'wpa_supplicant_gui' ] ; then
	yaourt -S wpa_supplicant_gui
	if [ $? == 0 ] ; then
		echo "wpa_supplicant_gui: installed"
	else
		echo "wpa_supplicant_gui: !not installed: install failure"
	fi
else
	echo "wpa_supplicant_gui: !installed as already installed."
fi
if [ "`pacman -Qqe xcmiscproto`" != 'xcmiscproto' ] ; then
	yaourt -S xcmiscproto
	if [ $? == 0 ] ; then
		echo "xcmiscproto: installed"
	else
		echo "xcmiscproto: !not installed: install failure"
	fi
else
	echo "xcmiscproto: !installed as already installed."
fi
if [ "`pacman -Qqe xlockmore`" != 'xlockmore' ] ; then
	yaourt -S xlockmore
	if [ $? == 0 ] ; then
		echo "xlockmore: installed"
	else
		echo "xlockmore: !not installed: install failure"
	fi
else
	echo "xlockmore: !installed as already installed."
fi
if [ "`pacman -Qqe xtrans`" != 'xtrans' ] ; then
	yaourt -S xtrans
	if [ $? == 0 ] ; then
		echo "xtrans: installed"
	else
		echo "xtrans: !not installed: install failure"
	fi
else
	echo "xtrans: !installed as already installed."
fi
if [ "`pacman -Qqe yajl`" != 'yajl' ] ; then
	yaourt -S yajl
	if [ $? == 0 ] ; then
		echo "yajl: installed"
	else
		echo "yajl: !not installed: install failure"
	fi
else
	echo "yajl: !installed as already installed."
fi
if [ "`pacman -Qqe avahi`" != 'avahi' ] ; then
	yaourt -S avahi
	if [ $? == 0 ] ; then
		echo "avahi: installed"
	else
		echo "avahi: !not installed: install failure"
	fi
else
	echo "avahi: !installed as already installed."
fi
if [ "`pacman -Qqe conky-i3`" != 'conky-i3' ] ; then
	yaourt -S conky-i3
	if [ $? == 0 ] ; then
		echo "conky-i3: installed"
	else
		echo "conky-i3: !not installed: install failure"
	fi
else
	echo "conky-i3: !installed as already installed."
fi
if [ "`pacman -Qqe cython`" != 'cython' ] ; then
	yaourt -S cython
	if [ $? == 0 ] ; then
		echo "cython: installed"
	else
		echo "cython: !not installed: install failure"
	fi
else
	echo "cython: !installed as already installed."
fi
if [ "`pacman -Qqe cython2`" != 'cython2' ] ; then
	yaourt -S cython2
	if [ $? == 0 ] ; then
		echo "cython2: installed"
	else
		echo "cython2: !not installed: install failure"
	fi
else
	echo "cython2: !installed as already installed."
fi
if [ "`pacman -Qqe engrampa-thunar-plugin`" != 'engrampa-thunar-plugin' ] ; then
	yaourt -S engrampa-thunar-plugin
	if [ $? == 0 ] ; then
		echo "engrampa-thunar-plugin: installed"
	else
		echo "engrampa-thunar-plugin: !not installed: install failure"
	fi
else
	echo "engrampa-thunar-plugin: !installed as already installed."
fi
if [ "`pacman -Qqe faenza-green-icon-theme`" != 'faenza-green-icon-theme' ] ; then
	yaourt -S faenza-green-icon-theme
	if [ $? == 0 ] ; then
		echo "faenza-green-icon-theme: installed"
	else
		echo "faenza-green-icon-theme: !not installed: install failure"
	fi
else
	echo "faenza-green-icon-theme: !installed as already installed."
fi
if [ "`pacman -Qqe gstreamer0.10-base-plugins`" != 'gstreamer0.10-base-plugins' ] ; then
	yaourt -S gstreamer0.10-base-plugins
	if [ $? == 0 ] ; then
		echo "gstreamer0.10-base-plugins: installed"
	else
		echo "gstreamer0.10-base-plugins: !not installed: install failure"
	fi
else
	echo "gstreamer0.10-base-plugins: !installed as already installed."
fi
if [ "`pacman -Qqe iptables`" != 'iptables' ] ; then
	yaourt -S iptables
	if [ $? == 0 ] ; then
		echo "iptables: installed"
	else
		echo "iptables: !not installed: install failure"
	fi
else
	echo "iptables: !installed as already installed."
fi
if [ "`pacman -Qqe john`" != 'john' ] ; then
	yaourt -S john
	if [ $? == 0 ] ; then
		echo "john: installed"
	else
		echo "john: !not installed: install failure"
	fi
else
	echo "john: !installed as already installed."
fi
if [ "`pacman -Qqe linux-firmware`" != 'linux-firmware' ] ; then
	yaourt -S linux-firmware
	if [ $? == 0 ] ; then
		echo "linux-firmware: installed"
	else
		echo "linux-firmware: !not installed: install failure"
	fi
else
	echo "linux-firmware: !installed as already installed."
fi
if [ "`pacman -Qqe linux44`" != 'linux44' ] ; then
	yaourt -S linux44
	if [ $? == 0 ] ; then
		echo "linux44: installed"
	else
		echo "linux44: !not installed: install failure"
	fi
else
	echo "linux44: !installed as already installed."
fi
if [ "`pacman -Qqe linux44-headers`" != 'linux44-headers' ] ; then
	yaourt -S linux44-headers
	if [ $? == 0 ] ; then
		echo "linux44-headers: installed"
	else
		echo "linux44-headers: !not installed: install failure"
	fi
else
	echo "linux44-headers: !installed as already installed."
fi
if [ "`pacman -Qqe linux44-ndiswrapper`" != 'linux44-ndiswrapper' ] ; then
	yaourt -S linux44-ndiswrapper
	if [ $? == 0 ] ; then
		echo "linux44-ndiswrapper: installed"
	else
		echo "linux44-ndiswrapper: !not installed: install failure"
	fi
else
	echo "linux44-ndiswrapper: !installed as already installed."
fi
if [ "`pacman -Qqe linux44-r8168`" != 'linux44-r8168' ] ; then
	yaourt -S linux44-r8168
	if [ $? == 0 ] ; then
		echo "linux44-r8168: installed"
	else
		echo "linux44-r8168: !not installed: install failure"
	fi
else
	echo "linux44-r8168: !installed as already installed."
fi
if [ "`pacman -Qqe linux49`" != 'linux49' ] ; then
	yaourt -S linux49
	if [ $? == 0 ] ; then
		echo "linux49: installed"
	else
		echo "linux49: !not installed: install failure"
	fi
else
	echo "linux49: !installed as already installed."
fi
if [ "`pacman -Qqe linux49-headers`" != 'linux49-headers' ] ; then
	yaourt -S linux49-headers
	if [ $? == 0 ] ; then
		echo "linux49-headers: installed"
	else
		echo "linux49-headers: !not installed: install failure"
	fi
else
	echo "linux49-headers: !installed as already installed."
fi
if [ "`pacman -Qqe linux49-ndiswrapper`" != 'linux49-ndiswrapper' ] ; then
	yaourt -S linux49-ndiswrapper
	if [ $? == 0 ] ; then
		echo "linux49-ndiswrapper: installed"
	else
		echo "linux49-ndiswrapper: !not installed: install failure"
	fi
else
	echo "linux49-ndiswrapper: !installed as already installed."
fi
if [ "`pacman -Qqe linux49-r8168`" != 'linux49-r8168' ] ; then
	yaourt -S linux49-r8168
	if [ $? == 0 ] ; then
		echo "linux49-r8168: installed"
	else
		echo "linux49-r8168: !not installed: install failure"
	fi
else
	echo "linux49-r8168: !installed as already installed."
fi
if [ "`pacman -Qqe linux49-virtualbox-host-modules`" != 'linux49-virtualbox-host-modules' ] ; then
	yaourt -S linux49-virtualbox-host-modules
	if [ $? == 0 ] ; then
		echo "linux49-virtualbox-host-modules: installed"
	else
		echo "linux49-virtualbox-host-modules: !not installed: install failure"
	fi
else
	echo "linux49-virtualbox-host-modules: !installed as already installed."
fi
if [ "`pacman -Qqe mkinitcpio-openswap`" != 'mkinitcpio-openswap' ] ; then
	yaourt -S mkinitcpio-openswap
	if [ $? == 0 ] ; then
		echo "mkinitcpio-openswap: installed"
	else
		echo "mkinitcpio-openswap: !not installed: install failure"
	fi
else
	echo "mkinitcpio-openswap: !installed as already installed."
fi
if [ "`pacman -Qqe mugshot`" != 'mugshot' ] ; then
	yaourt -S mugshot
	if [ $? == 0 ] ; then
		echo "mugshot: installed"
	else
		echo "mugshot: !not installed: install failure"
	fi
else
	echo "mugshot: !installed as already installed."
fi
if [ "`pacman -Qqe ndiswrapper-utils`" != 'ndiswrapper-utils' ] ; then
	yaourt -S ndiswrapper-utils
	if [ $? == 0 ] ; then
		echo "ndiswrapper-utils: installed"
	else
		echo "ndiswrapper-utils: !not installed: install failure"
	fi
else
	echo "ndiswrapper-utils: !installed as already installed."
fi
if [ "`pacman -Qqe openmp`" != 'openmp' ] ; then
	yaourt -S openmp
	if [ $? == 0 ] ; then
		echo "openmp: installed"
	else
		echo "openmp: !not installed: install failure"
	fi
else
	echo "openmp: !installed as already installed."
fi
if [ "`pacman -Qqe openresolv`" != 'openresolv' ] ; then
	yaourt -S openresolv
	if [ $? == 0 ] ; then
		echo "openresolv: installed"
	else
		echo "openresolv: !not installed: install failure"
	fi
else
	echo "openresolv: !installed as already installed."
fi
if [ "`pacman -Qqe opera`" != 'opera' ] ; then
	yaourt -S opera
	if [ $? == 0 ] ; then
		echo "opera: installed"
	else
		echo "opera: !not installed: install failure"
	fi
else
	echo "opera: !installed as already installed."
fi
if [ "`pacman -Qqe pa-applet`" != 'pa-applet' ] ; then
	yaourt -S pa-applet
	if [ $? == 0 ] ; then
		echo "pa-applet: installed"
	else
		echo "pa-applet: !not installed: install failure"
	fi
else
	echo "pa-applet: !installed as already installed."
fi
if [ "`pacman -Qqe pamac`" != 'pamac' ] ; then
	yaourt -S pamac
	if [ $? == 0 ] ; then
		echo "pamac: installed"
	else
		echo "pamac: !not installed: install failure"
	fi
else
	echo "pamac: !installed as already installed."
fi
if [ "`pacman -Qqe plasma-meta`" != 'plasma-meta' ] ; then
	yaourt -S plasma-meta
	if [ $? == 0 ] ; then
		echo "plasma-meta: installed"
	else
		echo "plasma-meta: !not installed: install failure"
	fi
else
	echo "plasma-meta: !installed as already installed."
fi
if [ "`pacman -Qqe plymouth-theme-manjaro-elegant`" != 'plymouth-theme-manjaro-elegant' ] ; then
	yaourt -S plymouth-theme-manjaro-elegant
	if [ $? == 0 ] ; then
		echo "plymouth-theme-manjaro-elegant: installed"
	else
		echo "plymouth-theme-manjaro-elegant: !not installed: install failure"
	fi
else
	echo "plymouth-theme-manjaro-elegant: !installed as already installed."
fi
if [ "`pacman -Qqe poppler-data`" != 'poppler-data' ] ; then
	yaourt -S poppler-data
	if [ $? == 0 ] ; then
		echo "poppler-data: installed"
	else
		echo "poppler-data: !not installed: install failure"
	fi
else
	echo "poppler-data: !installed as already installed."
fi
if [ "`pacman -Qqe python-bottleneck`" != 'python-bottleneck' ] ; then
	yaourt -S python-bottleneck
	if [ $? == 0 ] ; then
		echo "python-bottleneck: installed"
	else
		echo "python-bottleneck: !not installed: install failure"
	fi
else
	echo "python-bottleneck: !installed as already installed."
fi
if [ "`pacman -Qqe python-cysignals`" != 'python-cysignals' ] ; then
	yaourt -S python-cysignals
	if [ $? == 0 ] ; then
		echo "python-cysignals: installed"
	else
		echo "python-cysignals: !not installed: install failure"
	fi
else
	echo "python-cysignals: !installed as already installed."
fi
if [ "`pacman -Qqe python-hidapi`" != 'python-hidapi' ] ; then
	yaourt -S python-hidapi
	if [ $? == 0 ] ; then
		echo "python-hidapi: installed"
	else
		echo "python-hidapi: !not installed: install failure"
	fi
else
	echo "python-hidapi: !installed as already installed."
fi
if [ "`pacman -Qqe python-pyzmq`" != 'python-pyzmq' ] ; then
	yaourt -S python-pyzmq
	if [ $? == 0 ] ; then
		echo "python-pyzmq: installed"
	else
		echo "python-pyzmq: !not installed: install failure"
	fi
else
	echo "python-pyzmq: !installed as already installed."
fi
if [ "`pacman -Qqe python2-bottleneck`" != 'python2-bottleneck' ] ; then
	yaourt -S python2-bottleneck
	if [ $? == 0 ] ; then
		echo "python2-bottleneck: installed"
	else
		echo "python2-bottleneck: !not installed: install failure"
	fi
else
	echo "python2-bottleneck: !installed as already installed."
fi
if [ "`pacman -Qqe python2-cysignals`" != 'python2-cysignals' ] ; then
	yaourt -S python2-cysignals
	if [ $? == 0 ] ; then
		echo "python2-cysignals: installed"
	else
		echo "python2-cysignals: !not installed: install failure"
	fi
else
	echo "python2-cysignals: !installed as already installed."
fi
if [ "`pacman -Qqe python2-hidapi`" != 'python2-hidapi' ] ; then
	yaourt -S python2-hidapi
	if [ $? == 0 ] ; then
		echo "python2-hidapi: installed"
	else
		echo "python2-hidapi: !not installed: install failure"
	fi
else
	echo "python2-hidapi: !installed as already installed."
fi
if [ "`pacman -Qqe python2-pyzmq`" != 'python2-pyzmq' ] ; then
	yaourt -S python2-pyzmq
	if [ $? == 0 ] ; then
		echo "python2-pyzmq: installed"
	else
		echo "python2-pyzmq: !not installed: install failure"
	fi
else
	echo "python2-pyzmq: !installed as already installed."
fi
if [ "`pacman -Qqe qpdfview-djvu-plugin`" != 'qpdfview-djvu-plugin' ] ; then
	yaourt -S qpdfview-djvu-plugin
	if [ $? == 0 ] ; then
		echo "qpdfview-djvu-plugin: installed"
	else
		echo "qpdfview-djvu-plugin: !not installed: install failure"
	fi
else
	echo "qpdfview-djvu-plugin: !installed as already installed."
fi
if [ "`pacman -Qqe qpdfview-ps-plugin`" != 'qpdfview-ps-plugin' ] ; then
	yaourt -S qpdfview-ps-plugin
	if [ $? == 0 ] ; then
		echo "qpdfview-ps-plugin: installed"
	else
		echo "qpdfview-ps-plugin: !not installed: install failure"
	fi
else
	echo "qpdfview-ps-plugin: !installed as already installed."
fi
if [ "`pacman -Qqe qt4`" != 'qt4' ] ; then
	yaourt -S qt4
	if [ $? == 0 ] ; then
		echo "qt4: installed"
	else
		echo "qt4: !not installed: install failure"
	fi
else
	echo "qt4: !installed as already installed."
fi
if [ "`pacman -Qqe steam-manjaro`" != 'steam-manjaro' ] ; then
	yaourt -S steam-manjaro
	if [ $? == 0 ] ; then
		echo "steam-manjaro: installed"
	else
		echo "steam-manjaro: !not installed: install failure"
	fi
else
	echo "steam-manjaro: !installed as already installed."
fi
if [ "`pacman -Qqe subnetcalc`" != 'subnetcalc' ] ; then
	yaourt -S subnetcalc
	if [ $? == 0 ] ; then
		echo "subnetcalc: installed"
	else
		echo "subnetcalc: !not installed: install failure"
	fi
else
	echo "subnetcalc: !installed as already installed."
fi
if [ "`pacman -Qqe viennacl`" != 'viennacl' ] ; then
	yaourt -S viennacl
	if [ $? == 0 ] ; then
		echo "viennacl: installed"
	else
		echo "viennacl: !not installed: install failure"
	fi
else
	echo "viennacl: !installed as already installed."
fi
if [ "`pacman -Qqe wpa_supplicant`" != 'wpa_supplicant' ] ; then
	yaourt -S wpa_supplicant
	if [ $? == 0 ] ; then
		echo "wpa_supplicant: installed"
	else
		echo "wpa_supplicant: !not installed: install failure"
	fi
else
	echo "wpa_supplicant: !installed as already installed."
fi
if [ "`pacman -Qqe xcursor-menda`" != 'xcursor-menda' ] ; then
	yaourt -S xcursor-menda
	if [ $? == 0 ] ; then
		echo "xcursor-menda: installed"
	else
		echo "xcursor-menda: !not installed: install failure"
	fi
else
	echo "xcursor-menda: !installed as already installed."
fi
if [ "`pacman -Qqe xfce-theme-greenbird`" != 'xfce-theme-greenbird' ] ; then
	yaourt -S xfce-theme-greenbird
	if [ $? == 0 ] ; then
		echo "xfce-theme-greenbird: installed"
	else
		echo "xfce-theme-greenbird: !not installed: install failure"
	fi
else
	echo "xfce-theme-greenbird: !installed as already installed."
fi
if [ "`pacman -Qqe xfce4-weather-plugin-menda-circle-icons`" != 'xfce4-weather-plugin-menda-circle-icons' ] ; then
	yaourt -S xfce4-weather-plugin-menda-circle-icons
	if [ $? == 0 ] ; then
		echo "xfce4-weather-plugin-menda-circle-icons: installed"
	else
		echo "xfce4-weather-plugin-menda-circle-icons: !not installed: install failure"
	fi
else
	echo "xfce4-weather-plugin-menda-circle-icons: !installed as already installed."
fi
if [ "`pacman -Qqe xournal`" != 'xournal' ] ; then
	yaourt -S xournal
	if [ $? == 0 ] ; then
		echo "xournal: installed"
	else
		echo "xournal: !not installed: install failure"
	fi
else
	echo "xournal: !installed as already installed."
fi
if [ "`pacman -Qqe xscreensaver`" != 'xscreensaver' ] ; then
	yaourt -S xscreensaver
	if [ $? == 0 ] ; then
		echo "xscreensaver: installed"
	else
		echo "xscreensaver: !not installed: install failure"
	fi
else
	echo "xscreensaver: !installed as already installed."
fi
if [ "`pacman -Qqe xz`" != 'xz' ] ; then
	yaourt -S xz
	if [ $? == 0 ] ; then
		echo "xz: installed"
	else
		echo "xz: !not installed: install failure"
	fi
else
	echo "xz: !installed as already installed."
fi
