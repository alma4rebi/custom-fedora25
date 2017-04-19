repo --name=fedora --mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch
repo --name=updates --mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=updates-released-f$releasever&arch=$basearch
#repo --name=updates-testing --mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=updates-testing-f$releasever&arch=$basearch
url --mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch




#add by youssef sourani
####################################################################################################################
repo --name="RPMFusion Free" --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&arch=$basearch

repo --name="RPMFusion Free Updates" --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-updates-released-$releasever&arch=$basearch

repo --name="RPMFusion Nonfree" --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-$releasever&arch=$basearch

repo --name="RPMFusion Nonfree Updates" --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-updates-released-$releasever&arch=$basearch

repo --name="Adobe" --baseurl=http://linuxdownload.adobe.com/linux/x86_64/

repo --name="Adobe - 32bit" --baseurl=http://linuxdownload.adobe.com/linux/i386/

repo --name="google-chrome" --baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64

repo --name="region51 chrome gnome shell"    --baseurl=https://copr-be.cloud.fedoraproject.org/results/region51/chrome-gnome-shell/fedora-$releasever-$basearch/

repo --name="telegram-desktop" --baseurl=https://copr-be.cloud.fedoraproject.org/results/youssefmsourani/telegram-desktop/fedora-$releasever-$basearch/

repo --name="bumblebee"  --baseurl=http://install.linux.ncsu.edu/pub/yum/itecs/public/bumblebee/fedora$releasever/

repo --name="bumblebee-nonfree" --baseurl=http://install.linux.ncsu.edu/pub/yum/itecs/public/bumblebee-nonfree/fedora$releasever/

repo --name="arfedy" --baseurl=https://copr-be.cloud.fedoraproject.org/results/youssefmsourani/arfedy/fedora-$releasever-$basearch/

repo --name="fedy" --baseurl=http://folkswithhats.org/repo/$releasever/

repo --name="fedora cisco openh264"  --baseurl=https://codecs.fedoraproject.org/openh264/$releasever/$basearch/

%include local_repo.ks

####################################################################################################################
