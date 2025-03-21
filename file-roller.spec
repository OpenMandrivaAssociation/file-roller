%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	An archive manager for GNOME
Name:		file-roller
Version:	44.5
Release:	2
License:	GPLv2+
Group:		Archiving/Compression
Url:		https://fileroller.sourceforge.net
Source0:	https://ftp.gnome.org/pub/GNOME/sources/file-roller/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: itstool
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libnautilus-extension-4)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: magic-devel
BuildRequires: pkgconfig(sm)
BuildRequires: meson ninja

Recommends:	cdrecord-isotools
Requires: packagekit-gui
# for the gsettings schema
Requires: nautilus
# as of file-roller 44.4 bzip3 is supported.
Requires: bzip3

%description
File Roller is an archive manager for the GNOME environment.  This means that
you can : create and modify archives; view the content of an archive; view a
file contained in the archive; extract files from the archive.
File Roller is only a front-end (a graphical interface) to archiving programs
like tar and zip. The supported file types are :
    * Tar archives uncompressed (.tar) or compressed with
          * gzip (.tar.gz , .tgz)
          * bzip (.tar.bz , .tbz)
          * bzip2 (.tar.bz2 , .tbz2)
          * bzip3 (.tar.bz3 , .tbz3)
          * compress (.tar.Z , .taz)
          * lzop (.tar.lzo , .tzo)
          * lzma (.tar.lzma , .tlz)
    * Zip archives (.zip)
    * Jar archives (.jar , .ear , .war)
    * Lha archives (.lzh)
    * Rar archives (.rar)
    * Single files compressed with gzip, bzip, bzip2, compress, lzop, lzma
    * ISO images

%prep
%setup -q
%autopatch -p1

%build
%meson
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%{_bindir}/*
%{_libdir}/nautilus/extensions-4/libnautilus-fileroller.so
%{_libexecdir}/%{name}
%{_datadir}/applications/*
%{_datadir}/metainfo/org.gnome.FileRoller.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.ArchiveManager1.service
%{_datadir}/dbus-1/services/org.gnome.FileRoller.service
%{_datadir}/file-roller
%{_datadir}/glib-2.0/schemas/org.gnome.FileRoller.gschema.xml
%{_iconsdir}/hicolor/*/*/*.*
