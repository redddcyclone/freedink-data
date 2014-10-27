#!/bin/bash

##	Derived release (doesn't include Audacity and Rosegarden
##	projects, original Ogg Vorbis files, etc.)
##      Used for the NSIS installer
PACKAGE=freedink-data
VERSION=$1

if [ -z "$VERSION" ]; then
    echo "Usage: $0 version"
    exit 1
fi

rm -rf $PACKAGE-$VERSION/
tar xzf $PACKAGE-$VERSION.tar.gz
pushd $PACKAGE-$VERSION/
make install DESTDIR=`pwd`/t
mkdir zip/

# Documentation
for i in *.txt; do
    cp $i zip/freedink-data-$i
done
for i in COPYING NEWS; do
    cp $i zip/freedink-data-$i.txt
done
cp -a licenses zip/
for i in zip/*.* zip/licenses/*.txt zip/licenses/URLS; do
    sed -i -e 's/\(^\|[^\r]\)$/\1\r/' $i
done

# Dink
mv t/usr/local/share/dink/dink/ zip/

rm -f ../$PACKAGE-$VERSION-nosrc.zip
(cd zip/ && zip -r ../../$PACKAGE-$VERSION-nosrc.zip .)
