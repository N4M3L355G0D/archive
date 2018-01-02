export QEMU_AUDIO_DRV=pa
export QEMU_PA_SOURCE=input

export QEMU_PA_SINK=`pactl list sinks | grep "Monitor Source" | cut -f2 -d: | sed s/^' '*//`

#export QEMU_PA_SINK=alsa_output.pci-0000_00_1f.3.analog-stereo.monitor

#sudo qemu-system-x86_64 -drive file=ubuntu-17.10-desktop-amd64.iso,format=raw,media=cdrom,readonly -m 2G -smp cores=4 -enable-kvm -net nic,model=pcnet -net user -soundhw hda
if test "$1" == "install" ; then
	fallocate -l 10G ubu.img
	mkfs.ext4 ubu.img
	CD='/srv/samba/middle/Torrents/ubuntu-17.10-desktop-amd64.iso'
	sudo qemu-system-x86_64 -cdrom "$CD" -boot order=d -drive format=raw,file=ubu.img -m 4G -smp cores=4 -enable-kvm -net nic,model=pcnet -net user -soundhw hda
elif test "$1" == "check" ; then
	CD='/srv/samba/middle/Torrents/ubuntu-17.10-desktop-amd64.iso'
	sudo qemu-system-x86_64 -cdrom "$CD" -boot order=d -drive format=raw,file=ubu.img -m 4G -smp cores=4 -enable-kvm -net nic,model=pcnet -net user -soundhw hda
else
	sudo qemu-system-x86_64 -drive format=raw,file=ubu.img -m 4G -smp cores=4 -enable-kvm -net nic,model=pcnet -net user -soundhw hda -vga std -display gtk -cpu host -accel kvm
fi
