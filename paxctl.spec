Summary:	New PaX control program
Summary(pl):	- -- pusty --
Name:		paxctl
Version:	0.2
Release:	0.9
License:	Public Domain
Group:		Applications/System
Source0:	http://pax.grsecurity.net/%{name}-%{version}.tar.gz
# Source0-md5:	efb173644c2dbf75a7a244feb212529c
URL:		http://pax.grsecurity.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	chpax

%define		_sbindir	/sbin

%description
This is paxctl for controlling PaX flags on a per binary basis.
PaX is an intrusion prevention system that provides the best protection
mechanisms against memory corruption bugs. Some applications are not
compatible with certain features (due to design or bad engineering)
and therefore they have to be exempted from certain enforcements. It
is also possible to use PaX in soft mode where none of the protection
mechanisms are active by default - here paxctl can be used to turn
them on for selected programs (e.g., network daemons, programs that
process network data such as mail clients, web browsers, etc).

New PaX control program when you use the PT_PAX_FLAGS marking
available in PaX patches after 2004.02.04 (highly recommended).

%description -l pl
- -- pusty --

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%doc README
%{_mandir}/man?/*
