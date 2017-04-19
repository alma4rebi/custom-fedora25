%post --nochroot
/usr/bin/mkdir -p $INSTALL_ROOT/etc/skel/.mozilla/firefox/arfedora.default
/usr/bin/cp mozilla/firefox/profiles.ini $INSTALL_ROOT/etc/skel/.mozilla/firefox/
/usr/bin/cp mozilla/firefox/arfedora.default/prefs.js $INSTALL_ROOT/etc/skel/.mozilla/firefox/arfedora.default

%end
