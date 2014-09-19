Name:       libgsasl
Summary:    Library for perfoming SASL authentication
Version:    1.8.0
Release:    0
Group:      Security/Accounts
License:    LGPL-2.1+
Source:     %{name}-%{version}.tar.gz
Source1:    %{name}.manifest
URL:        http://www.gnu.org/software/gsasl/
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
BuildRequires:      libgcrypt-devel

%description
%{name} is a library to perfom SASL authentication.


%package devel
Summary: Devel package for %{name}
Group: SDK/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} .


%build
%configure --with-libgcrypt
%__make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install

%find_lang %{name}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f %{name}.lang
%license COPYING COPYING.LIB
%defattr(-,root,root,-)
%manifest %{name}.manifest
%doc AUTHORS NEWS README THANKS
%{_libdir}/%{name}.so.*


%files devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_includedir}/gsasl*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
