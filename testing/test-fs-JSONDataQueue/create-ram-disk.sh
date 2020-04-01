#!/bin/bash

# see: https://www.linuxbabe.com/command-line/create-ramdisk-linux

sudo mkdir /tmp/myramdisk
sudo chmod 777 /tmp/myramdisk
sudo mount -t tmpfs -o size=4096m myramdisk /tmp/myramdisk
mount | tail -n 1



