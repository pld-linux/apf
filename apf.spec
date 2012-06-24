Summary:	Active Port Forwarder - SSL secure packet tunneling
Summary(pl):	Active Port Forwarder - bezpieczne tunelowanie pakiet�w poprzez SSL
Name:		apf
Version:	0.7.5
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://gray-world.net/projects/af/%{name}-%{version}.tgz
# Source0-md5:	25c5b192adb6ff2763f4f2106065dbba
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
a client. APF is dedicated for people, who don't have an external ip
number and want to make some services available across the net.
Moreover, zlib is used to compress the transferred data. Using one,
permanent data/control channel with flow control/packet buffering
provides good performance and reasonably small latency. Running
afserver does not require root priviledges, nor does it use threads or
other processes.

%description -l pl
Active Port Forwarder jest narz�dziem do bezpiecznego tunelowania
po��cze�. Dla zwi�kszenia bezpiecze�stwa komunikacji mi�dzy serwerem a
klientem u�ywana jest biblioteka SSL. APF zosta� zaprojektowany z
my�l� o ludziach nie posiadaj�cych zewn�trznych numer�w IP, kt�rzy
chcieliby udost�pni� �wiatu jakie� us�ugi. Ponadto, biblioteka zlib
jest u�ywana do kompresowania przesy�anych danych. U�ycie jednego
po��czenia dla danych u�ytkownika/steruj�cych, wraz z kontrol�
przesy�u/buforowaniem pakiet�w, umo�liwia osi�gni�cie dobrej
wydajno�ci i rozs�dnie ma�ych op�nie�. afserver nie potrzebuje
uprawnie� roota, nie u�ywa w�tk�w ani innych proces�w.

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
