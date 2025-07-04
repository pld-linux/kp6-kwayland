%define		kdeplasmaver	6.4.2
%define		qtver		6.6.0
%define		kpname		kwayland

Summary:	Qt-style Client library wrapper for the Wayland libraries
Name:		kp6-%{kpname}
Version:	6.4.2
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	2d37d324116be911cafc0914e65cb722
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	plasma-wayland-protocols-devel >= 1.14.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	wayland-devel
BuildRequires:	xz
BuildRequires:	Qt6WaylandClient-devel >= %{qtver}
Obsoletes:	kp5-%{kpname} < 6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
Qt-style Client library wrapper for the Wayland libraries.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kp5-%{kpname}-devel < 6

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
