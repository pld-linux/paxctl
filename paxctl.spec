Summary:	New PaX control program
Summary(pl):	Nowe narzêdzie do kontroli PaX
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
This is paxctl utility for controlling PaX flags on a per binary
basis. This new PaX control program uses the PT_PAX_FLAGS marking
available in PaX patches after 2004.02.04 (highly recommended).

PaX is an intrusion prevention system that provides some protection
mechanisms against memory corruption bugs. Some applications are not
compatible with certain features (due to design or bad engineering)
and therefore they have to be exempted from certain enforcements. It
is also possible to use PaX in soft mode where none of the protection
mechanisms are active by default - here paxctl can be used to turn
them on for selected programs (e.g., network daemons, programs that
process network data such as mail clients, web browsers, etc).

%description -l pl
Ten pakiet zawiera narzêdzie paxctl do kontroli flag PaX dla ka¿dej
binarki. Ten nowy program u¿ywa znaczników PT_PAX_FLAGS dostêpnych w
³atach PaX po 2004.02.04 (jest to mocno zalecana wersja).

PaX to system zapobiegania w³amaniom dostarczaj±cy mechanizmy
zabezpieczeñ przeciwko b³êdom zwi±zanym z uszkadzaniem zawarto¶ci
pamiêci. Niektóre aplikacje nie s± kompatybilne z pewnymi cechami (ze
wzglêdów projektowych lub z³ej techniki) i przez to mog± musieæ byæ
zwolnione z niektórych ograniczeñ. Mo¿liwe jest tak¿e uruchomienie
mechanizmu PaX w trybie ³agodnym (soft), kiedy ¿aden z mechanizmów
ochrony nie jest domy¶lnie w³±czony i w takim przypadku mo¿na u¿ywaæ
paxctl do w³±czenia ich dla wybranych programów (np. demonów
sieciowych, programów przetwarzaj±cych dane sieciowe takich jak
klienci pocztowi, przegl±darki WWW itp.).

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
