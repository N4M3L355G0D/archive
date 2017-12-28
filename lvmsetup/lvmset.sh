#! /usr/bin/env bash

#noguilinux

#this is not meant to be changed
hostsdb="hosts.db"

lsBin() {
export IFS=":"
for i in $PATH; do
 ls -l $i/$1 
done
export IFS=" "
}

checkBin() {
 exist="`lsBin sqlite3 |& grep -v "ls: cannot access " | awk '{print $9;}' | head -n 1`"
 if test "$exist" == "" ; then
  echo "does not exist!"
 else
  echo "exists"
 fi
}

if test `whoami` == "root" ; then
	sqliteBin="`checkBin`"
        if test "$sqliteBin" == "exists" ; then
		conf="lvmset.cnf"
		conf_db="lvmsetup-conf.db"
		if test -f "$conf_db" ; then
			altconf="$2"
			readCnfDB(){
				COL="$1"
				table="cnf"
				SQL="select rowid from $table order by rowid desc limit 1;"
				if test "$2" != "" ; then
					rowid="$2"
					SQL="select rowid from $table where rowid=$2;"
					rowidCheck=`sqlite3 "$conf_db" "$SQL"`
					# do test to ensure that rowid exists
					if test "$rowidCheck" == "" ; then
						echo "alt conf does not exist in db"
						exit 1
					fi
				else
					rowid="`sqlite3 "$conf_db" "$SQL"`"
					if test "$rowid" == "" ; then
					rowid=1
					fi
				fi
				SQL="select $COL from $table where rowid=$rowid"
				sqlite3 "$conf_db" "$SQL"
			}
			VG="`readCnfDB VG $altconf`"
			if test "$VG" == "alt conf does not exist in db" ; then
				echo "alt conf does not exist in db!"
				exit 1
			fi
			LV="`readCnfDB LV $altconf`"
			DISKPATH_TOP="`readCnfDB DISKPATH_TOP $altconf`"
			DISKSIZE=`readCnfDB DISKSIZE $altconf`
			LVSIZE=`readCnfDB LVSIZE $altconf`
			fname="`readCnfDB fname $altconf`"
			top_num=`readCnfDB top_num $altconf`
			bot_num=`readCnfDB bot_num $altconf`
			echo "using: $conf_db"
		elif test -f "$conf" ; then
			VG="`grep -w "VG" "$conf" | cut -f2 -d=`"
			LV="$VG""`grep -w 'LV' "$conf" | cut -f2 -d=`"
			DISKPATH_TOP="`grep -w 'DISKPATH_TOP' "$conf" | cut -f2 -d=`"
			DISKSIZE="`grep -w 'DISKSIZE' "$conf" | cut -f2 -d=`"
			LVSIZE="`grep -w 'LVSIZE' "$conf" | cut -f2 -d=`"
			fname="`grep -w 'fname' "$conf" | cut -f2 -d=`"
			top_num=`grep -w 'top_num' "$conf" | cut -f2 -d=`
			bot_num=`grep -w 'bot_num' "$conf" | cut -f2 -d=`
			echo "using: $conf"
		else
			VG="new"
			LV="$VG""VG"
			DISKPATH_TOP="mount"
			DISKSIZE=1073741824
			LVSIZE=31138512896
			fname="disk"
			top_num=1
			bot_num=35
			echo "using: hardcoded values << cannot find config files!"
		fi
		checkVal=`expr $bot_num \* $DISKSIZE`
		if (( $checkVal < $LVSIZE )) ; then
			echo "(DISKSIZE*number of disks) < LVSIZE"
			exit 1
		fi
	
		DISKPATH="$DISKPATH_TOP/mount"
		ext_num=`expr $top_num + 1`
	
		vgtest() {
			res=`vgdisplay "$VG" |& tail -n1 | sed s\|' '\|''\|g`
			if test "$res" == "Cannotprocessvolumegroup$VG"; then
				echo "run"
			else
				echo "stop"
			fi
		}
		
		
		if test "$1" == "createLVM" ; then
			check="`vgtest`"
			#check to see if lvm exists
			if test "$check" == "run" ; then
				#need to check to see if $VG-$LV is active or not
	
				#get the disks ready
				i=$top_num
				while (( $i <= $bot_num )) ; do
					if test ! -d $DISKPATH$i ; then
						mkdir -p $DISKPATH$i
					fi
					#make the disk files
					read -rp "use ssh: " use_ssh
					if test $use_ssh != 'n' ; then
						if test -e "$hostsdb" ; then
							read -rp "user hosts.db: " use_hosts_db
							if test "$user_hosts_db" != 'n' ; then
								user="`sqlite3 "$hostsdb" "select user from hosts where rowid=$i;"`"
								host="`sqlite3 "$hostsdb" "select host from hosts where rowid=$i;"`"
								dpath="`sqlite3 "$hostsdb" "select diskpath from hosts where rowid=$i;"`"
							else
								read -rp "ssh user: " user
								read -rp "ssh host: " host
								read -rp "ssh host disk path: " dpath
							fi
								ssh "$user"@"$host" "fallocate -l $DISKSIZE \"$dpath\"/\"$fname\".\"$i\".img"
						else
								read -rp "ssh user: " user
								read -rp "ssh host: " host
								read -rp "ssh host disk path: " dpath
								ssh "$user"@"$host" "fallocate -l $DISKSIZE \"$dpath\"/\"$fname\".\"$i\".img"

						fi
					else
						dd if=/dev/zero of=$DISKPATH$i/$fname.$i.img bs=1M count=`echo "$DISKSIZE / (1024 ^ 1)" | bc` 
					fi
					#connect the disk files to a loop device
					losetup /dev/loop$i $DISKPATH$i/$fname.$i.img 
					#make a physical volume on the current loop device
					pvcreate /dev/loop$i
				        i=`expr $i + 1`	
				done
				#create the volume group on disk 1
				vgcreate "$VG" /dev/loop1
				#extend the volume group over the remainder of the disks
				i=$ext_num
				while (( $i <= $bot_num )) ; do
					vgextend "$VG" /dev/loop$i 
					i=`expr $i + 1`
				done 
				#create the logical volume
				lvcreate -L "$LVSIZE"b -n "$LV" "$VG" 
				#format the logical volume
				mkfs.ext4 -F /dev/mapper/"$VG"-"$LV"
			else
				echo "LVM $VG-$LV already exists"
				exit 1
			fi
		elif test "$1" == "disconnectLVM" ; then
			check="`vgtest`"
			#check to see if lvm exists
			if test "$check" == "stop"  ; then
				#need to check to see if $VG-$LV is mounted first
				vgchange -an "$VG"
				i=$top_num
				while (( $i <= $bot_num )) ; do
					losetup -d "/dev/loop$i"
					i=`expr $i + 1`
				done
			else
				echo "LVM $VG-$LV Does not exist!"
				exit 1
			fi
		elif test "$1" == "connectLVM" ; then
			check="`vgtest`"
			if test "$check" == "run" ; then
				if test -d "$DISKPATH_TOP" ; then
					i=$top_num
					while (( $i <= $bot_num )) ; do
						if test -d "$DISKPATH$i" ; then
							losetup /dev/loop$i "$DISKPATH$i"/$fname.$i.img
							i=`expr $i + 1`
						else
							echo "$DISKPATH$i does not exist"
							exit 1
						fi
					done
				else
					echo "$DISKPATH_TOP does not exist!"
				exit 1
				fi
			else
				echo "LVM $VG-$LV is already connected!"
			fi
		elif test "$1" == "removeLVM" ; then
			i=$top_num
			vgchange -an "$VG"
			while (( $i <= $bot_num )) ; do
				shred --random-source=/dev/urandom --verbose /dev/loop$i
				losetup -d /dev/loop$i
				i=`expr $i + 1`
			done
			rm -r "$DISKPATH_TOP"
		else
			echo "not an available command"
			exit 1
		fi
	else
		echo "sqlite3 binary does not exist in path!"
	fi
else
	echo "you are not root!"
	exit 1
fi
