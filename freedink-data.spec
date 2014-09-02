Name:		freedink-data
Version:	1.08.20140901
Release:	1%{?dist}
Summary:	Adventure and role-playing game (game data)

Group:		Amusements/Games
License:	zlib and CC-BY-SA and (GPLv3+ or Free Art or CC-BY-SA) and OAL and Public Domain and CC-BY and GPLv2+
URL:		http://www.gnu.org/software/freedink/
Source0:	ftp://ftp.gnu.org/gnu/freedink/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
Dink Smallwood is an adventure/role-playing game, similar to Zelda,
made by RTsoft. Besides twisted humor, it includes the actual game
editor, allowing players to create hundreds of new adventures called
Dink Modules or D-Mods for short.

This package contains the original game story, along with free sound
and music replacements.


%prep
%setup -q
# Strip DOS EOL from documentation
# https://fedoraproject.org/wiki/PackageMaintainers/Common_Rpmlint_Issues#wrong-file-end-of-line-encoding
sed -i 's/\r//' README.txt README-REPLACEMENTS.txt


%build


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt README-REPLACEMENTS.txt licenses/
%{_datadir}/dink/


%changelog
* Mon Sep 01 2014 Sylvain Beucler <beuc@beuc.net> - 1.08.20140901-1
- New upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20121209-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20121209-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20121209-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Sylvain Beucler <beuc@beuc.net> - 1.08.20121209-1
- New upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20111016-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20111016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 16 2011 Sylvain Beucler <beuc@beuc.net> - 1.08.20111016-1
- New upstream release

* Sat Jul 23 2011 Sylvain Beucler <beuc@beuc.net> - 1.08.20110723-1
- New upstream release
- Update homepage URL

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20100103-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan  3 2010 Sylvain Beucler <beuc@beuc.net> - 1.08.20100103-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20090706-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090706-1
- New upstream release (remove savegame)

* Sun Jul 05 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090705-1
- New upstream release
- Removed patch to preserve timestamps (applied upstream)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20080920-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-3
- Actually apply patch0 (preserve timestamps)

* Tue Sep 23 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-2
- Specify all licenses used by the package
- Added licenses texts in docs
- Replaced /usr by a RPM macro
- Add patch from upstream to preserve timestamps no install
- Converted DOS newlines

* Sat Sep 20 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-1
- Initial package
