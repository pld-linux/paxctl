Summary:	Manage PaX flags for ELF and a.out binaries
Summary(pl):	Zarz±dca znaczników PaX dla binarek ELF oraz a.out
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
New PaX control program when you use the PT_PAX_FLAGS marking
available in PaX patches after 2004.02.04 (highly recommended).

This program manages various PaX related flags for ELF and a.out
binaries. The flags only have effect when running the patched Linux
kernel.

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
%{_mandir}/man?/*
