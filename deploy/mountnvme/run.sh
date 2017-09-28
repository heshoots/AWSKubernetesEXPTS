mkfs.ext4 /dev/nvme0n1
mkdir /media/host/mnt/drive
mount /dev/nvme0n1 /media/host/mnt/drive
nsenter --mount=/media/host/proc/1/ns/mnt -- mount /dev/nvme0n1 /mnt/drive
