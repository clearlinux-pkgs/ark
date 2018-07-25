#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ark
Version  : 18.04.3
Release  : 1
URL      : https://github.com/KDE/ark/archive/v18.04.3.tar.gz
Source0  : https://github.com/KDE/ark/archive/v18.04.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: ark-bin
Requires: ark-lib
Requires: ark-data
Requires: ark-license
Requires: ark-man
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : bzip2-dev
BuildRequires : karchive-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : kitemmodels-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kparts-dev
BuildRequires : kpty-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : libarchive-dev
BuildRequires : solid-dev
BuildRequires : sonnet-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
What is it
----------
Ark is a graphical file compression/decompression utility with support for multiple formats,
including tar, gzip, bzip2, rar and zip, as well as CD-ROM images.
Ark can be used to browse, extract, create, and modify archives.

%package bin
Summary: bin components for the ark package.
Group: Binaries
Requires: ark-data
Requires: ark-license
Requires: ark-man

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
Requires: ark-man

%description doc
doc components for the ark package.


%package lib
Summary: lib components for the ark package.
Group: Libraries
Requires: ark-data
Requires: ark-license

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
%setup -q -n ark-18.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532526213
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1532526213
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ark
cp COPYING %{buildroot}/usr/share/doc/ark/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

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
/usr/lib64/libkerfuffle.so.18.4.3
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
/usr/lib64/qt5/plugins/kf5/kfileitemaction/compressfileitemaction.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/extractfileitemaction.so
/usr/lib64/qt5/plugins/kf5/kio_dnd/extracthere.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/ark/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/ark.1
