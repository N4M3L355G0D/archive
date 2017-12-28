#! /bin/bash
TARBALL=nmap*.tar.bz2

get() {
echo "Downloading TARBALL"
SOURCE=https://nmap.org/dist/nmap-7.12.tar.bz2
wget -c $SOURCE
}

install() {
echo "Compling and Installing"
DEST=nmap
tar -xvf $TARBALL
cd `echo $TARBALL | sed s\|".tar.bz2"\|""\|g`
./configure --prefix=$HOME/"$DEST"
make "LUA_LIBS=../liblua/liblua.a -ldl -lm"
make install
}

clean() {
cd ..
echo "Clean"
rm -r $TARBALL ./`echo $TARBALL | sed s\|".tar.bz2"\|""\|g` 
}

get
install
clean
