%define		kdeplasmaver	6.1.4
%define		qtver		5.3.2
%define		kpname		kwayland

Summary:	Qt-style Client library wrapper for the Wayland libraries
Name:		kp6-%{kpname}
Version:	6.1.4
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	d297f096ac9492262b8274a024618bd3
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	plasma-wayland-protocols >= 1.13.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	wayland-devel
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
Qt-style Client library wrapper for the Wayland libraries.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kp5-%{kpname}-devel < %{version}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKWaylandClient.so.*.*
%ghost %{_libdir}/libKWaylandClient.so.6
%{_datadir}/qlogging-categories6/kwayland.categories
%{_datadir}/qlogging-categories6/kwayland.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KWayland
%{_libdir}/cmake/KWayland
%{_libdir}/libKWaylandClient.so
%{_pkgconfigdir}/KWaylandClient.pc
