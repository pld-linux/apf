Summary:	Active Port Forwarder - SSL secure packet tunneling
Summary(pl.UTF-8):	Active Port Forwarder - bezpieczne tunelowanie pakietów poprzez SSL
Name:		apf
Version:	0.8.3
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://gray-world.net/projects/af/%{name}-%{version}.tgz
# Source0-md5:	a70713279ce53e4aa6255deddbdb0f6b
URL:		http://xmlindent.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Active Port Forwarder is a software tool for secure port forwarding.
It uses SSL to increase security of communication between a server and
a client. APF is dedicated for people, who don't have an external IP
number and want to make some services available across the net.
Moreover, zlib is used to compress the transferred data. Using one,
permanent data/control channel with flow control/packet buffering
provides good performance and reasonably small latency. Running
afserver does not require root priviledges, nor does it use threads or
other processes.

%description -l pl.UTF-8
Active Port Forwarder jest narzędziem do bezpiecznego tunelowania
połączeń. Dla zwiększenia bezpieczeństwa komunikacji między serwerem a
klientem używana jest biblioteka SSL. APF został zaprojektowany z
myślą o ludziach nie posiadających zewnętrznych numerów IP, którzy
chcieliby udostępnić światu jakieś usługi. Ponadto, biblioteka zlib
jest używana do kompresowania przesyłanych danych. Użycie jednego
połączenia dla danych użytkownika/sterujących, wraz z kontrolą
przesyłu/buforowaniem pakietów, umożliwia osiągnięcie dobrej
wydajności i rozsądnie małych opóźnień. afserver nie potrzebuje
uprawnień roota, nie używa wątków ani innych procesów.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/*_example.conf
%lang(fr) %doc doc/fr/fr_README
%lang(ru) %doc doc/ru/ru_README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/afclient*
%{_mandir}/man?/afserver*
