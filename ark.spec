#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ark
Version  : 22.12.0
Release  : 65
URL      : https://download.kde.org/stable/release-service/22.12.0/src/ark-22.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.0/src/ark-22.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.0/src/ark-22.12.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 LGPL-3.0 MIT
Requires: ark-bin = %{version}-%{release}
Requires: ark-data = %{version}-%{release}
Requires: ark-lib = %{version}-%{release}
Requires: ark-license = %{version}-%{release}
Requires: ark-locales = %{version}-%{release}
Requires: ark-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libarchive-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libzip)
BuildRequires : zlib-dev

%description
Test data for the cliunarchiver's unit tests.
* The password for encrypted_entries.rar is 'asdasd' (without quotes).

%package bin
Summary: bin components for the ark package.
Group: Binaries
Requires: ark-data = %{version}-%{release}
Requires: ark-license = %{version}-%{release}

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


%package locales
Summary: locales components for the ark package.
Group: Default

%description locales
locales components for the ark package.


%package man
Summary: man components for the ark package.
Group: Default

%description man
man components for the ark package.


%prep
%setup -q -n ark-22.12.0
cd %{_builddir}/ark-22.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670519820
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1670519820
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ark
cp %{_builddir}/ark-%{version}/COPYING.icons %{buildroot}/usr/share/package-licenses/ark/69420a3ad87532e76ad02ac77b78f5dfff3cfc01 || :
cp %{_builddir}/ark-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/ark/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee || :
cp %{_builddir}/ark-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ark/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/ark-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ark/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/ark-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/ark/49e61f7864169f2e356c11a17422d7d20d74b40f || :
cp %{_builddir}/ark-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/ark/81e12d0c07782abcf558af7aa19846e3e2606a70 || :
pushd clr-build
%make_install
popd
%find_lang ark

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
/usr/share/kconf_update/ark.upd
/usr/share/kconf_update/ark_add_hamburgermenu_to_toolbar.sh
/usr/share/metainfo/org.kde.ark.appdata.xml
/usr/share/qlogging-categories5/ark.categories
/usr/share/xdg/arkrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/ark/index.cache.bz2
/usr/share/doc/HTML/ca/ark/index.docbook
/usr/share/doc/HTML/de/ark/ark-mainwindow.png
/usr/share/doc/HTML/de/ark/index.cache.bz2
/usr/share/doc/HTML/de/ark/index.docbook
/usr/share/doc/HTML/en/ark/ark-comment.png
/usr/share/doc/HTML/en/ark/ark-mainwindow.png
/usr/share/doc/HTML/en/ark/create-archive.png
/usr/share/doc/HTML/en/ark/create-protected-archive.png
/usr/share/doc/HTML/en/ark/extract-dialog.png
/usr/share/doc/HTML/en/ark/index.cache.bz2
/usr/share/doc/HTML/en/ark/index.docbook
/usr/share/doc/HTML/es/ark/index.cache.bz2
/usr/share/doc/HTML/es/ark/index.docbook
/usr/share/doc/HTML/et/ark/index.cache.bz2
/usr/share/doc/HTML/et/ark/index.docbook
/usr/share/doc/HTML/fr/ark/ark-mainwindow.png
/usr/share/doc/HTML/fr/ark/index.cache.bz2
/usr/share/doc/HTML/fr/ark/index.docbook
/usr/share/doc/HTML/gl/ark/index.cache.bz2
/usr/share/doc/HTML/gl/ark/index.docbook
/usr/share/doc/HTML/it/ark/ark-comment.png
/usr/share/doc/HTML/it/ark/ark-mainwindow.png
/usr/share/doc/HTML/it/ark/create-archive.png
/usr/share/doc/HTML/it/ark/create-protected-archive.png
/usr/share/doc/HTML/it/ark/extract-dialog.png
/usr/share/doc/HTML/it/ark/index.cache.bz2
/usr/share/doc/HTML/it/ark/index.docbook
/usr/share/doc/HTML/nl/ark/index.cache.bz2
/usr/share/doc/HTML/nl/ark/index.docbook
/usr/share/doc/HTML/pl/ark/index.cache.bz2
/usr/share/doc/HTML/pl/ark/index.docbook
/usr/share/doc/HTML/pt/ark/index.cache.bz2
/usr/share/doc/HTML/pt/ark/index.docbook
/usr/share/doc/HTML/pt_BR/ark/ark-mainwindow.png
/usr/share/doc/HTML/pt_BR/ark/create-protected-archive.png
/usr/share/doc/HTML/pt_BR/ark/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ark/index.docbook
/usr/share/doc/HTML/ru/ark/index.cache.bz2
/usr/share/doc/HTML/ru/ark/index.docbook
/usr/share/doc/HTML/sr/ark/index.cache.bz2
/usr/share/doc/HTML/sr/ark/index.docbook
/usr/share/doc/HTML/sr@latin/ark/index.cache.bz2
/usr/share/doc/HTML/sr@latin/ark/index.docbook
/usr/share/doc/HTML/sv/ark/index.cache.bz2
/usr/share/doc/HTML/sv/ark/index.docbook
/usr/share/doc/HTML/uk/ark/ark-comment.png
/usr/share/doc/HTML/uk/ark/ark-mainwindow.png
/usr/share/doc/HTML/uk/ark/create-archive.png
/usr/share/doc/HTML/uk/ark/create-protected-archive.png
/usr/share/doc/HTML/uk/ark/extract-dialog.png
/usr/share/doc/HTML/uk/ark/index.cache.bz2
/usr/share/doc/HTML/uk/ark/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkerfuffle.so.22
/usr/lib64/libkerfuffle.so.22.12.0
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_cli7z.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_cliarj.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_clirar.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_cliunarchiver.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_clizip.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_libarchive.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_libarchive_readonly.so
/usr/lib64/qt5/plugins/kerfuffle/kerfuffle_libzip.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/compressfileitemaction.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/extractfileitemaction.so
/usr/lib64/qt5/plugins/kf5/kio_dnd/extracthere.so
/usr/lib64/qt5/plugins/kf5/parts/arkpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ark/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/ark/49e61f7864169f2e356c11a17422d7d20d74b40f
/usr/share/package-licenses/ark/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee
/usr/share/package-licenses/ark/69420a3ad87532e76ad02ac77b78f5dfff3cfc01
/usr/share/package-licenses/ark/81e12d0c07782abcf558af7aa19846e3e2606a70
/usr/share/package-licenses/ark/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/ark.1
/usr/share/man/de/man1/ark.1
/usr/share/man/es/man1/ark.1
/usr/share/man/fr/man1/ark.1
/usr/share/man/gl/man1/ark.1
/usr/share/man/it/man1/ark.1
/usr/share/man/man1/ark.1
/usr/share/man/nl/man1/ark.1
/usr/share/man/pt/man1/ark.1
/usr/share/man/pt_BR/man1/ark.1
/usr/share/man/sr/man1/ark.1
/usr/share/man/sr@latin/man1/ark.1
/usr/share/man/sv/man1/ark.1
/usr/share/man/uk/man1/ark.1

%files locales -f ark.lang
%defattr(-,root,root,-)

