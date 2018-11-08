#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ark
Version  : 18.08.3
Release  : 9
URL      : https://github.com/KDE/ark/archive/v18.08.3.tar.gz
Source0  : https://github.com/KDE/ark/archive/v18.08.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 LGPL-3.0
Requires: ark-bin = %{version}-%{release}
Requires: ark-data = %{version}-%{release}
Requires: ark-lib = %{version}-%{release}
Requires: ark-license = %{version}-%{release}
Requires: ark-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : bzip2-dev
BuildRequires : libarchive-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libzip)
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
What is it
----------
Ark is a graphical file compression/decompression utility with support for multiple formats,
including tar, gzip, bzip2, rar and zip, as well as CD-ROM images.
Ark can be used to browse, extract, create, and modify archives.

%package abi
Summary: abi components for the ark package.
Group: Default

%description abi
abi components for the ark package.


%package bin
Summary: bin components for the ark package.
Group: Binaries
Requires: ark-data = %{version}-%{release}
Requires: ark-license = %{version}-%{release}
Requires: ark-man = %{version}-%{release}

%description bin
bin components for the ark package.


%package data
Summary: data components for the ark package.
Group: Data

%description data
data components for the ark package.


%package doc
Summary: doc components for the ark package.
Group: Documentation
Requires: ark-man = %{version}-%{release}

%description doc
doc components for the ark package.


%package lib
Summary: lib components for the ark package.
Group: Libraries
Requires: ark-data = %{version}-%{release}
Requires: ark-license = %{version}-%{release}

%description lib
lib components for the ark package.


%package license
Summary: license components for the ark package.
Group: Default

%description license
license components for the ark package.


%package man
Summary: man components for the ark package.
Group: Default

%description man
man components for the ark package.


%prep
%setup -q -n ark-18.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541688117
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1541688117
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ark
cp COPYING %{buildroot}/usr/share/package-licenses/ark/COPYING
cp COPYING.icons %{buildroot}/usr/share/package-licenses/ark/COPYING.icons
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files abi
%defattr(-,root,root,-)
/usr/share/abi/libkerfuffle.so.18.8.3.abi
/usr/share/abi/libkerfuffle.so.18.abi

%files bin
%defattr(-,root,root,-)
/usr/bin/ark

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.ark.desktop
/usr/share/config.kcfg/ark.kcfg
/usr/share/icons/hicolor/128x128/apps/ark.png
/usr/share/icons/hicolor/48x48/apps/ark.png
/usr/share/icons/hicolor/64x64/apps/ark.png
/usr/share/icons/hicolor/scalable/apps/ark.svgz
/usr/share/kservices5/ark_part.desktop
/usr/share/kservicetypes5/kerfufflePlugin.desktop
/usr/share/kxmlgui5/ark/ark_viewer.rc
/usr/share/metainfo/org.kde.ark.appdata.xml
/usr/share/xdg/ark.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/en/ark/ark-comment.png
/usr/share/doc/HTML/en/ark/ark-mainwindow.png
/usr/share/doc/HTML/en/ark/create-archive.png
/usr/share/doc/HTML/en/ark/create-protected-archive.png
/usr/share/doc/HTML/en/ark/extract-dialog.png
/usr/share/doc/HTML/en/ark/index.cache.bz2
/usr/share/doc/HTML/en/ark/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkerfuffle.so.18
/usr/lib64/libkerfuffle.so.18.8.3
/usr/lib64/qt5/plugins/arkpart.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_cli7z.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_clirar.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_cliunarchiver.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_clizip.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_libarchive.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_libarchive_readonly.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_libbz2.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_libgz.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_libxz.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_libzip.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/compressfileitemaction.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/extractfileitemaction.so
/usr/lib64/qt5/plugins/kf5/kio_dnd/extracthere.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ark/COPYING
/usr/share/package-licenses/ark/COPYING.icons

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ark.1
