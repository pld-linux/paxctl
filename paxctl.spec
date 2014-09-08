Summary:	New PaX control program
Summary(pl.UTF-8):	Nowe narzędzie do kontroli PaX
Name:		paxctl
Version:	0.9
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://pax.grsecurity.net/%{name}-%{version}.tar.gz
# Source0-md5:	9bea59b1987dc4e16c2d22d745374e64
URL:		http://pax.grsecurity.net/
Obsoletes:	chpax
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Ten pakiet zawiera narzędzie paxctl do kontroli flag PaX dla każdej
binarki. Ten nowy program używa znaczników PT_PAX_FLAGS dostępnych w
łatach PaX po 2004.02.04 (jest to mocno zalecana wersja).

PaX to system zapobiegania włamaniom dostarczający mechanizmy
zabezpieczeń przeciwko błędom związanym z uszkadzaniem zawartości
pamięci. Niektóre aplikacje nie są kompatybilne z pewnymi cechami (ze
względów projektowych lub złej techniki) i przez to mogą musieć być
zwolnione z niektórych ograniczeń. Możliwe jest także uruchomienie
mechanizmu PaX w trybie łagodnym (soft), kiedy żaden z mechanizmów
ochrony nie jest domyślnie włączony i w takim przypadku można używać
paxctl do włączenia ich dla wybranych programów (np. demonów
sieciowych, programów przetwarzających dane sieciowe takich jak
klienci pocztowi, przeglądarki WWW itp.).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}
install paxctl $RPM_BUILD_ROOT%{_sbindir}
install paxctl.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_sbindir}/paxctl
%{_mandir}/man1/paxctl.1*
