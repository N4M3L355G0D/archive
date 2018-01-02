export QEMU_AUDIO_DRV=pa
export QEMU_PA_SOURCE=input

export QEMU_PA_SINK=`pactl list sinks | grep "Monitor Source" | cut -f2 -d: | sed s/^' '*//`
CD='/srv/samba/middle/Torrents/ubuntu-17.10-desktop-amd64.iso'
#export QEMU_PA_SINK=alsa_output.pci-0000_00_1f.3.analog-stereo.monitor
if test "$1" == "iso-only" ; then
	sudo qemu-system-x86_64 -drive file="$CD",format=raw,media=cdrom,readonly -m 2G -smp cores=4 -enable-kvm -net nic,model=pcnet -net user -soundhw hda -usb -device usb-host,hostbus=1,hostaddr=7
elif test "$1" == "install" ; then
	fallocate -l 10G ubu.img
	mkfs.ext4 ubu.img
	sudo qemu-system-x86_64 -cdrom "$CD" -boot order=d -drive format=raw,file=ubu.img -m 4G -smp cores=4 -enable-kvm -net nic,model=pcnet -net user -soundhw hda -usb -device usb-host,hostbus=1,hostaddr=7
elif test "$1" == "check" ; then
	sudo qemu-system-x86_64 -cdrom "$CD" -boot order=d -drive format=raw,file=ubu.img -m 4G -smp cores=4 -enable-kvm -net nic,model=pcnet -net user -soundhw hda 
else
	#need to regroup options to easily create a common options and a unique options set of vars to reduce code maintentance as i learn more about QEMU
	sudo qemu-system-x86_64 -drive format=raw,file=ubu.img -m 4G -smp cores=4 -enable-kvm -net nic,model=pcnet -net user -soundhw hda -vga std -display gtk -cpu host -accel kvm -usb -device usb-host,hostbus=1,hostaddr=7
fi
