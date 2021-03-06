#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5D2EEE6F6F349D7C (tim@centricular.com)
#
Name     : gstreamer
Version  : 1.18.4
Release  : 56
URL      : https://gstreamer.freedesktop.org/src/gstreamer/gstreamer-1.18.4.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gstreamer/gstreamer-1.18.4.tar.xz
Source1  : https://gstreamer.freedesktop.org/src/gstreamer/gstreamer-1.18.4.tar.xz.asc
Summary  : Streaming media framework
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: gstreamer-bin = %{version}-%{release}
Requires: gstreamer-data = %{version}-%{release}
Requires: gstreamer-lib = %{version}-%{release}
Requires: gstreamer-libexec = %{version}-%{release}
Requires: gstreamer-license = %{version}-%{release}
Requires: gstreamer-locales = %{version}-%{release}
Requires: gstreamer-man = %{version}-%{release}
BuildRequires : bash-completion-dev
BuildRequires : bison
BuildRequires : buildreq-meson
BuildRequires : flex
BuildRequires : gmp-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gsl-dev
BuildRequires : libcap-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libdw)
BuildRequires : valgrind

%description
GStreamer 1.18.x stable series
WHAT IT IS
----------
This is GStreamer, a framework for streaming media.

%package bin
Summary: bin components for the gstreamer package.
Group: Binaries
Requires: gstreamer-data = %{version}-%{release}
Requires: gstreamer-libexec = %{version}-%{release}
Requires: gstreamer-license = %{version}-%{release}

%description bin
bin components for the gstreamer package.


%package data
Summary: data components for the gstreamer package.
Group: Data

%description data
data components for the gstreamer package.


%package dev
Summary: dev components for the gstreamer package.
Group: Development
Requires: gstreamer-lib = %{version}-%{release}
Requires: gstreamer-bin = %{version}-%{release}
Requires: gstreamer-data = %{version}-%{release}
Provides: gstreamer-devel = %{version}-%{release}
Requires: gstreamer = %{version}-%{release}

%description dev
dev components for the gstreamer package.


%package lib
Summary: lib components for the gstreamer package.
Group: Libraries
Requires: gstreamer-data = %{version}-%{release}
Requires: gstreamer-libexec = %{version}-%{release}
Requires: gstreamer-license = %{version}-%{release}

%description lib
lib components for the gstreamer package.


%package libexec
Summary: libexec components for the gstreamer package.
Group: Default
Requires: gstreamer-license = %{version}-%{release}

%description libexec
libexec components for the gstreamer package.


%package license
Summary: license components for the gstreamer package.
Group: Default

%description license
license components for the gstreamer package.


%package locales
Summary: locales components for the gstreamer package.
Group: Default

%description locales
locales components for the gstreamer package.


%package man
Summary: man components for the gstreamer package.
Group: Default

%description man
man components for the gstreamer package.


%prep
%setup -q -n gstreamer-1.18.4
cd %{_builddir}/gstreamer-1.18.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615858475
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gstreamer
cp %{_builddir}/gstreamer-1.18.4/COPYING %{buildroot}/usr/share/package-licenses/gstreamer/249308ff72cc14f24d4756377a537281c13ec8fa
cp %{_builddir}/gstreamer-1.18.4/docs/random/LICENSE %{buildroot}/usr/share/package-licenses/gstreamer/22990b105a08bb838c95fcc4bc5450c6dfdc79ac
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gstreamer-1.0

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gst-inspect-1.0
/usr/bin/gst-launch-1.0
/usr/bin/gst-stats-1.0
/usr/bin/gst-tester-1.0
/usr/bin/gst-typefind-1.0

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gst-1.0.typelib
/usr/lib64/girepository-1.0/GstBase-1.0.typelib
/usr/lib64/girepository-1.0/GstCheck-1.0.typelib
/usr/lib64/girepository-1.0/GstController-1.0.typelib
/usr/lib64/girepository-1.0/GstNet-1.0.typelib
/usr/share/bash-completion/completions/gst-inspect-1.0
/usr/share/bash-completion/completions/gst-launch-1.0
/usr/share/bash-completion/helpers/gst
/usr/share/gdb/auto-load/usr/lib64/libgstreamer-1.0.so.0.1804.0-gdb.py
/usr/share/gir-1.0/*.gir
/usr/share/gstreamer-1.0/gdb/glib_gobject_helper.py
/usr/share/gstreamer-1.0/gdb/gst_gdb.py

%files dev
%defattr(-,root,root,-)
/usr/include/gstreamer-1.0/gst/base/base-prelude.h
/usr/include/gstreamer-1.0/gst/base/base.h
/usr/include/gstreamer-1.0/gst/base/gstadapter.h
/usr/include/gstreamer-1.0/gst/base/gstaggregator.h
/usr/include/gstreamer-1.0/gst/base/gstbaseparse.h
/usr/include/gstreamer-1.0/gst/base/gstbasesink.h
/usr/include/gstreamer-1.0/gst/base/gstbasesrc.h
/usr/include/gstreamer-1.0/gst/base/gstbasetransform.h
/usr/include/gstreamer-1.0/gst/base/gstbitreader.h
/usr/include/gstreamer-1.0/gst/base/gstbitwriter.h
/usr/include/gstreamer-1.0/gst/base/gstbytereader.h
/usr/include/gstreamer-1.0/gst/base/gstbytewriter.h
/usr/include/gstreamer-1.0/gst/base/gstcollectpads.h
/usr/include/gstreamer-1.0/gst/base/gstdataqueue.h
/usr/include/gstreamer-1.0/gst/base/gstflowcombiner.h
/usr/include/gstreamer-1.0/gst/base/gstpushsrc.h
/usr/include/gstreamer-1.0/gst/base/gstqueuearray.h
/usr/include/gstreamer-1.0/gst/base/gsttypefindhelper.h
/usr/include/gstreamer-1.0/gst/check/check-prelude.h
/usr/include/gstreamer-1.0/gst/check/check.h
/usr/include/gstreamer-1.0/gst/check/gstbufferstraw.h
/usr/include/gstreamer-1.0/gst/check/gstcheck.h
/usr/include/gstreamer-1.0/gst/check/gstconsistencychecker.h
/usr/include/gstreamer-1.0/gst/check/gstharness.h
/usr/include/gstreamer-1.0/gst/check/gsttestclock.h
/usr/include/gstreamer-1.0/gst/check/internal-check.h
/usr/include/gstreamer-1.0/gst/controller/controller-enumtypes.h
/usr/include/gstreamer-1.0/gst/controller/controller-prelude.h
/usr/include/gstreamer-1.0/gst/controller/controller.h
/usr/include/gstreamer-1.0/gst/controller/gstargbcontrolbinding.h
/usr/include/gstreamer-1.0/gst/controller/gstdirectcontrolbinding.h
/usr/include/gstreamer-1.0/gst/controller/gstinterpolationcontrolsource.h
/usr/include/gstreamer-1.0/gst/controller/gstlfocontrolsource.h
/usr/include/gstreamer-1.0/gst/controller/gstproxycontrolbinding.h
/usr/include/gstreamer-1.0/gst/controller/gsttimedvaluecontrolsource.h
/usr/include/gstreamer-1.0/gst/controller/gsttriggercontrolsource.h
/usr/include/gstreamer-1.0/gst/glib-compat.h
/usr/include/gstreamer-1.0/gst/gst.h
/usr/include/gstreamer-1.0/gst/gstallocator.h
/usr/include/gstreamer-1.0/gst/gstatomicqueue.h
/usr/include/gstreamer-1.0/gst/gstbin.h
/usr/include/gstreamer-1.0/gst/gstbuffer.h
/usr/include/gstreamer-1.0/gst/gstbufferlist.h
/usr/include/gstreamer-1.0/gst/gstbufferpool.h
/usr/include/gstreamer-1.0/gst/gstbus.h
/usr/include/gstreamer-1.0/gst/gstcaps.h
/usr/include/gstreamer-1.0/gst/gstcapsfeatures.h
/usr/include/gstreamer-1.0/gst/gstchildproxy.h
/usr/include/gstreamer-1.0/gst/gstclock.h
/usr/include/gstreamer-1.0/gst/gstcompat.h
/usr/include/gstreamer-1.0/gst/gstconfig.h
/usr/include/gstreamer-1.0/gst/gstcontext.h
/usr/include/gstreamer-1.0/gst/gstcontrolbinding.h
/usr/include/gstreamer-1.0/gst/gstcontrolsource.h
/usr/include/gstreamer-1.0/gst/gstdatetime.h
/usr/include/gstreamer-1.0/gst/gstdebugutils.h
/usr/include/gstreamer-1.0/gst/gstdevice.h
/usr/include/gstreamer-1.0/gst/gstdevicemonitor.h
/usr/include/gstreamer-1.0/gst/gstdeviceprovider.h
/usr/include/gstreamer-1.0/gst/gstdeviceproviderfactory.h
/usr/include/gstreamer-1.0/gst/gstdynamictypefactory.h
/usr/include/gstreamer-1.0/gst/gstelement.h
/usr/include/gstreamer-1.0/gst/gstelementfactory.h
/usr/include/gstreamer-1.0/gst/gstelementmetadata.h
/usr/include/gstreamer-1.0/gst/gstenumtypes.h
/usr/include/gstreamer-1.0/gst/gsterror.h
/usr/include/gstreamer-1.0/gst/gstevent.h
/usr/include/gstreamer-1.0/gst/gstformat.h
/usr/include/gstreamer-1.0/gst/gstghostpad.h
/usr/include/gstreamer-1.0/gst/gstinfo.h
/usr/include/gstreamer-1.0/gst/gstiterator.h
/usr/include/gstreamer-1.0/gst/gstmacros.h
/usr/include/gstreamer-1.0/gst/gstmemory.h
/usr/include/gstreamer-1.0/gst/gstmessage.h
/usr/include/gstreamer-1.0/gst/gstmeta.h
/usr/include/gstreamer-1.0/gst/gstminiobject.h
/usr/include/gstreamer-1.0/gst/gstobject.h
/usr/include/gstreamer-1.0/gst/gstpad.h
/usr/include/gstreamer-1.0/gst/gstpadtemplate.h
/usr/include/gstreamer-1.0/gst/gstparamspecs.h
/usr/include/gstreamer-1.0/gst/gstparse.h
/usr/include/gstreamer-1.0/gst/gstpipeline.h
/usr/include/gstreamer-1.0/gst/gstplugin.h
/usr/include/gstreamer-1.0/gst/gstpluginfeature.h
/usr/include/gstreamer-1.0/gst/gstpoll.h
/usr/include/gstreamer-1.0/gst/gstpreset.h
/usr/include/gstreamer-1.0/gst/gstpromise.h
/usr/include/gstreamer-1.0/gst/gstprotection.h
/usr/include/gstreamer-1.0/gst/gstquery.h
/usr/include/gstreamer-1.0/gst/gstregistry.h
/usr/include/gstreamer-1.0/gst/gstsample.h
/usr/include/gstreamer-1.0/gst/gstsegment.h
/usr/include/gstreamer-1.0/gst/gststreamcollection.h
/usr/include/gstreamer-1.0/gst/gststreams.h
/usr/include/gstreamer-1.0/gst/gststructure.h
/usr/include/gstreamer-1.0/gst/gstsystemclock.h
/usr/include/gstreamer-1.0/gst/gsttaglist.h
/usr/include/gstreamer-1.0/gst/gsttagsetter.h
/usr/include/gstreamer-1.0/gst/gsttask.h
/usr/include/gstreamer-1.0/gst/gsttaskpool.h
/usr/include/gstreamer-1.0/gst/gsttoc.h
/usr/include/gstreamer-1.0/gst/gsttocsetter.h
/usr/include/gstreamer-1.0/gst/gsttracer.h
/usr/include/gstreamer-1.0/gst/gsttracerfactory.h
/usr/include/gstreamer-1.0/gst/gsttracerrecord.h
/usr/include/gstreamer-1.0/gst/gsttypefind.h
/usr/include/gstreamer-1.0/gst/gsttypefindfactory.h
/usr/include/gstreamer-1.0/gst/gsturi.h
/usr/include/gstreamer-1.0/gst/gstutils.h
/usr/include/gstreamer-1.0/gst/gstvalue.h
/usr/include/gstreamer-1.0/gst/gstversion.h
/usr/include/gstreamer-1.0/gst/math-compat.h
/usr/include/gstreamer-1.0/gst/net/gstnet.h
/usr/include/gstreamer-1.0/gst/net/gstnetaddressmeta.h
/usr/include/gstreamer-1.0/gst/net/gstnetclientclock.h
/usr/include/gstreamer-1.0/gst/net/gstnetcontrolmessagemeta.h
/usr/include/gstreamer-1.0/gst/net/gstnettimepacket.h
/usr/include/gstreamer-1.0/gst/net/gstnettimeprovider.h
/usr/include/gstreamer-1.0/gst/net/gstnetutils.h
/usr/include/gstreamer-1.0/gst/net/gstptpclock.h
/usr/include/gstreamer-1.0/gst/net/net-prelude.h
/usr/include/gstreamer-1.0/gst/net/net.h
/usr/lib64/libgstbase-1.0.so
/usr/lib64/libgstcheck-1.0.so
/usr/lib64/libgstcontroller-1.0.so
/usr/lib64/libgstnet-1.0.so
/usr/lib64/libgstreamer-1.0.so
/usr/lib64/pkgconfig/gstreamer-1.0.pc
/usr/lib64/pkgconfig/gstreamer-base-1.0.pc
/usr/lib64/pkgconfig/gstreamer-check-1.0.pc
/usr/lib64/pkgconfig/gstreamer-controller-1.0.pc
/usr/lib64/pkgconfig/gstreamer-net-1.0.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/gstreamer-1.0/libgstcoreelements.so
/usr/lib64/gstreamer-1.0/libgstcoretracers.so
/usr/lib64/libgstbase-1.0.so.0
/usr/lib64/libgstbase-1.0.so.0.1804.0
/usr/lib64/libgstcheck-1.0.so.0
/usr/lib64/libgstcheck-1.0.so.0.1804.0
/usr/lib64/libgstcontroller-1.0.so.0
/usr/lib64/libgstcontroller-1.0.so.0.1804.0
/usr/lib64/libgstnet-1.0.so.0
/usr/lib64/libgstnet-1.0.so.0.1804.0
/usr/lib64/libgstreamer-1.0.so.0
/usr/lib64/libgstreamer-1.0.so.0.1804.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gstreamer-1.0/gst-completion-helper
/usr/libexec/gstreamer-1.0/gst-hotdoc-plugins-scanner
/usr/libexec/gstreamer-1.0/gst-plugin-scanner
/usr/libexec/gstreamer-1.0/gst-plugins-doc-cache-generator
/usr/libexec/gstreamer-1.0/gst-ptp-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gstreamer/22990b105a08bb838c95fcc4bc5450c6dfdc79ac
/usr/share/package-licenses/gstreamer/249308ff72cc14f24d4756377a537281c13ec8fa

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gst-inspect-1.0.1
/usr/share/man/man1/gst-launch-1.0.1
/usr/share/man/man1/gst-stats-1.0.1
/usr/share/man/man1/gst-typefind-1.0.1

%files locales -f gstreamer-1.0.lang
%defattr(-,root,root,-)

