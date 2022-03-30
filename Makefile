all:

install:
	mkdir -p $(DESTDIR)/usr/share/samba-ansible/

	cp -a ansible.cfg $(DESTDIR)/usr/share/samba-ansible/
	cp -a *.yml $(DESTDIR)/usr/share/samba-ansible/
	cp -a group_vars $(DESTDIR)/usr/share/samba-ansible/
	cp -a roles $(DESTDIR)/usr/share/samba-ansible/
	cp -a library $(DESTDIR)/usr/share/samba-ansible/

uninstall:
	rm -rf $(DESTDIR)/usr/share/samba-ansible