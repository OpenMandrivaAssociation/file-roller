Summary:	An archive manager for GNOME
Name:		file-roller
Version:	3.4.1
Release:	1
License:	GPLv2+
URL:		http://fileroller.sourceforge.net
Group:		Archiving/Compression
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	magic-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnautilus-extension)
BuildRequires:	pkgconfig(sm)

Suggests:	cdrecord-isotools
Requires: packagekit-gui
Requires(pre):	GConf2
# for the gsettings schema
Requires:	nautilus

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
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper \
	--enable-packagekit \
	--enable-nautilus-actions

%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS NEWS README 
%{_bindir}/*
%{_libdir}/nautilus/extensions-3.0/*.so
%{_libexecdir}/%{name}
%{_libexecdir}/%{name}-server
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/org.gnome.FileRoller.service
%{_datadir}/file-roller
%{_datadir}/GConf/gsettings/file-roller.convert
%{_datadir}/glib-2.0/schemas/org.gnome.FileRoller.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.*

