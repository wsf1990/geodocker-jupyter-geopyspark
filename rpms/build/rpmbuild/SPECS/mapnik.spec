%define _topdir   /tmp/rpmbuild
%define name      mapnik
%define release   33
%define version   093fcee

%define debug_package %{nil}

BuildRoot: %{buildroot}
Summary:   Mapnik
License:   LGPL
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    mapnik-093fcee6d1ba1fd360718ceade83894aeffc2548.zip
Prefix:    /usr/local
Group:     Azavea

%description
Mapnik 093fcee

%prep
%setup -q -n mapnik-093fcee6d1ba1fd360718ceade83894aeffc2548

%build
echo

%install
PKG_CONFIG_PATH=/usr/local/lib/pkgconfig python scons/scons.py PYTHON=/usr/bin/python3.4 DESTDIR=%{buildroot} PREFIX=/usr/local -j$(grep -c ^processor /proc/cpuinfo) install

%files
%defattr(-,root,root)
/usr/local/*
