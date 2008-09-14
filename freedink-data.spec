Name:		freedink-data
Version:	1.08.20080914
Release:	1%{?dist}
Summary:	Adventure and role-playing game (game data)

Group:		Amusements/Games
License:	zlib
URL:		http://www.freedink.org/
Source0:	http://www.freedink.org/releases/freedink-data-1.08.20080914.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
Dink Smallwood is an adventure/role-playing game, similar to Zelda,
made by RTsoft. Besides twisted humour, it includes the actual game
editor, allowing players to create hundreds of new adventures called
Dink Modules or D-Mods for short.

This package contains architecture-independent data for the original
game (except for non-free sounds).


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt README-REPLACEMENTS.txt
%{_datadir}/dink/


%changelog
* Sun Sep 14 2008 Sylvain Beucler <beuc@beuc.net> 1.08.20080914-1
- Initial package