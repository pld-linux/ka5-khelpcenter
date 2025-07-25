#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		khelpcenter
Summary:	khelpcenter
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	03ef818c0e43e350609d4399e49c3959
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5DBus-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	Qt5Xml-devel >= 5.15.2
BuildRequires:	cmake >= 3.20
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt5-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.83.0
BuildRequires:	kf5-karchive-devel >= 5.83.0
BuildRequires:	kf5-kauth-devel >= %{kframever}
BuildRequires:	kf5-kbookmarks-devel >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= 5.83.0
BuildRequires:	kf5-kdoctools-devel >= 5.83.0
BuildRequires:	kf5-khtml-devel >= 5.83.0
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf5-kjs-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= 5.83.0
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= 5.83.0
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-solid-devel >= %{kframever}
BuildRequires:	kf5-sonnet-devel >= %{kframever}
BuildRequires:	libxml2-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xapian-core-devel
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
Requires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Help Center.

%description -l pl.UTF-8
Centrum pomocy KDE.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=5
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khelpcenter
%attr(755,root,root) %{_prefix}/libexec/khc_mansearch.pl
%attr(755,root,root) %{_prefix}/libexec/khc_xapianindexer
%attr(755,root,root) %{_prefix}/libexec/khc_xapiansearch

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{_datadir}/config.kcfg/khelpcenter.kcfg
%{_datadir}/kde4/services/khelpcenter.desktop
%{_datadir}/khelpcenter
%{_datadir}/kservices5/khelpcenter.desktop
%{_datadir}/qlogging-categories5/khelpcenter.categories
%{_desktopdir}/org.kde.khelpcenter.desktop
%{_datadir}/dbus-1/services/org.kde.khelpcenter.service
%{_datadir}/metainfo/org.kde.khelpcenter.metainfo.xml
