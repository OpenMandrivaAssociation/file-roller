Summary:	An archive manager for GNOME
Name:		file-roller
Version: 2.32.1
Release: %mkrel 1
License:	GPLv2+
URL:		http://fileroller.sourceforge.net
Group:		Archiving/Compression
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	%name-48.png
Source2:	%name-32.png
Source3:	%name-16.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:  gtk+2-devel >= 2.13.0
BuildRequires:  glib2-devel >= 2.25
BuildRequires:  libnautilus-devel >= 2.22.2
BuildRequires:  libGConf2-devel
BuildRequires:  scrollkeeper
BuildRequires:  intltool
BuildRequires:  gnome-doc-utils >= 0.3.2
BuildRequires:  libxslt-proc
BuildRequires:  desktop-file-utils
BuildRequires:  chrpath
BuildRequires:  packagekit
Requires(post):		scrollkeeper >= 0.3 desktop-file-utils
Requires(postun):		scrollkeeper >= 0.3 desktop-file-utils
Suggests:	cdrecord-isotools
Requires: packagekit-gui

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
%configure2_5x --disable-scrollkeeper --enable-packagekit
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std

# install icons
mkdir -p $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir},%{_iconsdir}}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
cp %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
cp %{SOURCE3} $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%find_lang %{name}-2.0 --with-gnome --all-name
for omf in %buildroot%_datadir/omf/*/*[_-]??.omf;do
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed s!%buildroot!!)" >> %name-2.0.lang
done

#remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/{bonobo,nautilus/extensions-2.0}/*.{la,a}

#gw rpmlint errors
chmod 755 %buildroot%_libdir/file-roller/isoinfo.sh
chrpath -d %buildroot{%_bindir/file-roller,%_libdir/nautilus/*/*.so}

%clean
rm -rf $RPM_BUILD_ROOT

%preun
%preun_uninstall_gconf_schemas %name

%files -f %{name}-2.0.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README 
%_sysconfdir/gconf/schemas/%name.schemas
%{_bindir}/*
%{_libdir}/nautilus/extensions-2.0/*.so
%{_datadir}/applications/*
%{_datadir}/file-roller
#%_datadir/glib-2.0/schemas/org.gnome.file-roller.gschema.xml
%dir %{_datadir}/omf/file-roller
%{_datadir}/omf/file-roller/file-roller-C.omf
%_libdir/%name
%_datadir/icons/hicolor/*/*/*.*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
