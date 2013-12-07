Summary:	A port of the default KDE widget theme (Oxygen) to gtk3
Name:		oxygen-gtk3
Version:	1.1.4
Release:	2
Group:		Graphical desktop/KDE
License:	LGPLv2+
Url:		https://projects.kde.org/projects/playground/artwork/oxygen-gtk
Source0:	ftp://ftp.kde.org/pub/kde/stable/oxygen-gtk3/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.2.0
Suggests:	oxygen-icon-theme
Requires:	%{name}-engine = %{version}-%{release}

%description
Oxygen-Gtk3 is a port of the default KDE widget theme (Oxygen), to gtk3.

It's primary goal is to ensure visual consistency between gtk and qt-based
applications running under kde. A secondary objective is to also have a
stand-alone nice looking gtk theme that would behave well on other Desktop
Environments.

Unlike other attempts made to port the kde oxygen theme to gtk3, this attempt
does not depend on Qt (via some Qt to Gtk conversion engine), nor does render
the widget appearance via hard coded pixmaps, which otherwise breaks everytime
some setting is changed in kde.

%files
%{_bindir}/%{name}-demo
%{_datadir}/themes/oxygen-gtk

#------------------------------------------------

%define libname %mklibname %{name}

%package -n %{libname}
Summary:	Dynamic libraries for %{name}
Group:		System/Libraries
Provides:	%{name}-engine = %{version}-%{release}

%description -n %{libname}
Dynamic libraries for %{name}.

%files -n %{libname}
%{_libdir}/gtk-3.0/3.0.0/theming-engines/liboxygen-gtk.so

#------------------------------------------------

%prep
%setup -q

%build
%cmake -DOXYGEN_FORCE_KDE_ICONS_AND_FONTS=0
%make

%install
%makeinstall_std -C build

