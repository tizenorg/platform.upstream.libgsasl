Name: libgsasl
Summary: Library for perfoming SASL authentication
Version: 1.8.0
Release: 1
Group: Security/Accounts
License: LGPL-2.1+
Source: %{name}-%{version}.tar.gz
Source1: %{name}.manifest
URL: http://www.gnu.org/software/gsasl/
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: libgcrypt-devel

%description
%{summary}.


%package devel
Summary: Development files for %{name}
Group: SDK/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.


%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} .


%build
%configure --with-libgcrypt
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%doc AUTHORS COPYING COPYING.LIB INSTALL NEWS README THANKS
%{_libdir}/%{name}.so.*
%{_datadir}/locale/*/LC_MESSAGES/libgsasl.mo


%files devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_includedir}/gsasl*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

