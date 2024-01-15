#!/bin/sh

cd version-print/
version=$(cat version-label.txt)
echo $version
exit