DESTDIR=
PREFIX=/usr/local
DATADIR=$(PREFIX)/share
version:=1.08.$(shell date +%Y%m%d)
releasedir=freedink-data-$(version)

all:
	@echo "No default action"

install:
#	Copy game data

#	The final directory is '$PREFIX/share/dink/dink' ('dink'
#	twice), as there can be site-wide D-Mods such as
#	'$PREFIX/share/dink/island'
	install -d -m 755 $(DESTDIR)$(DATADIR)/dink

#	'-a' will preserve timestamps, which some distros prefer. It
#	will also preserve symlinks, which may be useful as there are
#	a few duplicate musics. Use a .zip archive for woe releases,
#	it will duplicate files but avoid creating empty files instead
#	of symlinks.
	cp -a dink $(DESTDIR)$(DATADIR)/dink/

#	Tidy permissions
	find $(DESTDIR)$(DATADIR)/dink/dink/ -type d -print0 | xargs -0r chmod 755
	find $(DESTDIR)$(DATADIR)/dink/dink/ -type f -print0 | xargs -0r chmod 644

# Release:
# (Do this from a fresh Git checkout to avoid packaging temporary files)
dist: update-gmo
##	Source release

#	Not using Git because that doesn't ship the .mo files
#	Plus that forbids testing uncommitted changes
#	git archive --format=tar.gz --prefix=$(releasedir)/ -o > $(releasedir).tar.gz HEAD \
#	  -- ChangeLog COPYING NEWS *.txt *.spec Makefile autobuild/ debian/ dink/ doc/ licenses/ soundtest/ src/ \

	rm -rf $(releasedir)
	mkdir $(releasedir)
	cp -a ChangeLog COPYING NEWS *.txt *.spec Makefile autobuild/ debian/ dink/ doc/ licenses/ soundtest/ src/ $(releasedir)

#	Clean-up:
#	git files
	find $(releasedir)/ -name ".gitignore" -print0 | xargs -0r rm
#	backup files
	find $(releasedir)/ -name "*~" -print0 | xargs -0r rm
#	savegames
	find $(releasedir)/ -iname "save*.dat" -print0 | xargs -0r rm
#	cheat^Wdebugging tool
	rm -f $(releasedir)/dink/Story/key-67.c
#	debug mode output
	rm -f $(releasedir)/dink/DEBUG.TXT

#	Tarball:
	tar czf $(releasedir).tar.gz $(releasedir)/

	rm -rf $(releasedir)

# Compile translation strings catalogs
update-gmo:
	cd dink/l10n; \
	for i in da de fr nl mk es eo fi ca hu; do \
		mkdir -p $$i/LC_MESSAGES; \
		echo -n "$$i: "; \
		msgfmt --statistics $$i.po -o $$i/LC_MESSAGES/dink.mo; \
	done
