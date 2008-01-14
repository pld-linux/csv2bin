Summary:	Convert a CSV database to format suitable for GeoIP library
Name:		csv2bin
Version:	20041103
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://people.netfilter.org/peejix/GeoIP/tools/%{name}-%{version}.tar.gz
# Source0-md5:	b92bff0fc2adba02a48cfbb4b401205c
URL:		http://people.netfilter.org/peejix/GeoIP/tools/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
csv2bin is a tool specially written for the iptables/netfilter's GeoIP
match purpose. This file won't discuss about the iptables/netfilter's
framework. <www.netfilter.org> for details.

csv2bin's only task is to convert a comma-seperated-value database
containing all IPv4 subnets and their associated countries to an
understable binary format for the iptables' GeoIP shared library.

You can create your own database (perhaps you feel sado) or simply
gets the latest GeoIP's free database from MaxMind. This product
includes GeoIP data created by MaxMind, available from
<http://maxmind.com/>

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	OPTION="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/csv2bin
