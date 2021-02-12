Name:          harbour-fraliit-itx
Version:       0.6.0
Release:       6
Summary:       ItalianoX
Obsoletes:     italiano-arw italianox harbour-italianox
Conflicts:      italiano-arw italianox harbour-italianox
Requires:      sailfish-version >= 2.1.0, harbour-fraliit-common >= 0.1.0-1
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPLv3

%description
Italian keyboard with arrows and numbers.

%files
/usr/share/maliit/plugins/com/jolla/layouts/itx.conf
/usr/share/maliit/plugins/com/jolla/layouts/itx.qml
/usr/share/maliit/plugins/com/jolla/layouts/itx_arw.conf
/usr/share/maliit/plugins/com/jolla/layouts/itx_arw.qml
/usr/share/maliit/plugins/com/jolla/layouts/itx_123.conf
/usr/share/maliit/plugins/com/jolla/layouts/itx_123.qml

%post
systemctl-user restart maliit-server.service

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm /usr/share/maliit/plugins/com/jolla/layouts/itx.conf
rm /usr/share/maliit/plugins/com/jolla/layouts/itx.qml
rm /usr/share/maliit/plugins/com/jolla/layouts/itx_arw.conf
rm /usr/share/maliit/plugins/com/jolla/layouts/itx_arw.qml
rm /usr/share/maliit/plugins/com/jolla/layouts/itx_123.conf
rm /usr/share/maliit/plugins/com/jolla/layouts/itx_123.qml
systemctl-user restart maliit-server.service
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
systemctl-user restart maliit-server.service
fi
fi

%changelog
* Sat Jun 9 2018 0.6.0-5
- Uses fraliit-common.

* Sat Oct 22 2016 0.5.0-1
- italiano-arw and italianox packages merged.

* Thu Sep 15 2015 0.4.1-2
- It should be possible to install it even on the Jolla Tablet.

* Mon Jun 8 2015 0.4
- Updated to 0.6.2 codebase.
- Improved symbols layout

* Thu Jun 4 2015 0.3
- Build against italiano-arw dependency (to keep the same codebase).
- Domain keys added.
- New spacebar layout.

* Sun Apr 19 2015 0.2
- Improved symbols keyboard layout.

* Fri Apr 17 2015 0.1
- First build.
