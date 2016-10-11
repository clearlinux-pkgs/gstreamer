#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gstreamer
Version  : 1.8.3
Release  : 7
URL      : https://gstreamer.freedesktop.org/src/gstreamer/gstreamer-1.8.3.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gstreamer/gstreamer-1.8.3.tar.xz
Summary  : GStreamer streaming media framework runtime
Group    : Development/Tools
License  : GPL-2.0
Requires: gstreamer-bin
Requires: gstreamer-lib
Requires: gstreamer-data
Requires: gstreamer-doc
Requires: gstreamer-locales
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : flex
BuildRequires : gettext
BuildRequires : gmp-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : valgrind

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package bin
Summary: bin components for the gstreamer package.
Group: Binaries
Requires: gstreamer-data

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
Requires: gstreamer-lib
Requires: gstreamer-bin
Requires: gstreamer-data
Provides: gstreamer-devel

%description dev
dev components for the gstreamer package.


%package doc
Summary: doc components for the gstreamer package.
Group: Documentation

%description doc
doc components for the gstreamer package.


%package lib
Summary: lib components for the gstreamer package.
Group: Libraries
Requires: gstreamer-data

%description lib
lib components for the gstreamer package.


%package locales
Summary: locales components for the gstreamer package.
Group: Default

%description locales
locales components for the gstreamer package.


%prep
%setup -q -n gstreamer-1.8.3

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install
%find_lang gstreamer-1.0

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gst-inspect-1.0
/usr/bin/gst-launch-1.0
/usr/bin/gst-stats-1.0
/usr/bin/gst-typefind-1.0
/usr/libexec/gstreamer-1.0/gst-plugin-scanner
/usr/libexec/gstreamer-1.0/gst-ptp-helper

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/gst-inspect-1.0
/usr/share/bash-completion/completions/gst-launch-1.0
/usr/share/bash-completion/helpers/gst
/usr/share/bash-completion/helpers/gst-completion-helper-1.0

%files dev
%defattr(-,root,root,-)
/usr/include/gstreamer-1.0/gst/base/base.h
/usr/include/gstreamer-1.0/gst/base/gstadapter.h
/usr/include/gstreamer-1.0/gst/base/gstbaseparse.h
/usr/include/gstreamer-1.0/gst/base/gstbasesink.h
/usr/include/gstreamer-1.0/gst/base/gstbasesrc.h
/usr/include/gstreamer-1.0/gst/base/gstbasetransform.h
/usr/include/gstreamer-1.0/gst/base/gstbitreader.h
/usr/include/gstreamer-1.0/gst/base/gstbytereader.h
/usr/include/gstreamer-1.0/gst/base/gstbytewriter.h
/usr/include/gstreamer-1.0/gst/base/gstcollectpads.h
/usr/include/gstreamer-1.0/gst/base/gstdataqueue.h
/usr/include/gstreamer-1.0/gst/base/gstflowcombiner.h
/usr/include/gstreamer-1.0/gst/base/gstpushsrc.h
/usr/include/gstreamer-1.0/gst/base/gstqueuearray.h
/usr/include/gstreamer-1.0/gst/base/gsttypefindhelper.h
/usr/include/gstreamer-1.0/gst/check/check.h
/usr/include/gstreamer-1.0/gst/check/gstbufferstraw.h
/usr/include/gstreamer-1.0/gst/check/gstcheck.h
/usr/include/gstreamer-1.0/gst/check/gstconsistencychecker.h
/usr/include/gstreamer-1.0/gst/check/gstharness.h
/usr/include/gstreamer-1.0/gst/check/gsttestclock.h
/usr/include/gstreamer-1.0/gst/check/internal-check.h
/usr/include/gstreamer-1.0/gst/controller/controller.h
/usr/include/gstreamer-1.0/gst/controller/gstargbcontrolbinding.h
/usr/include/gstreamer-1.0/gst/controller/gstdirectcontrolbinding.h
/usr/include/gstreamer-1.0/gst/controller/gstinterpolationcontrolsource.h
/usr/include/gstreamer-1.0/gst/controller/gstlfocontrolsource.h
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
/usr/include/gstreamer-1.0/gst/gstcontext.h
/usr/include/gstreamer-1.0/gst/gstcontrolbinding.h
/usr/include/gstreamer-1.0/gst/gstcontrolsource.h
/usr/include/gstreamer-1.0/gst/gstdatetime.h
/usr/include/gstreamer-1.0/gst/gstdebugutils.h
/usr/include/gstreamer-1.0/gst/gstdevice.h
/usr/include/gstreamer-1.0/gst/gstdevicemonitor.h
/usr/include/gstreamer-1.0/gst/gstdeviceprovider.h
/usr/include/gstreamer-1.0/gst/gstdeviceproviderfactory.h
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
/usr/include/gstreamer-1.0/gst/gstprotection.h
/usr/include/gstreamer-1.0/gst/gstquery.h
/usr/include/gstreamer-1.0/gst/gstregistry.h
/usr/include/gstreamer-1.0/gst/gstsample.h
/usr/include/gstreamer-1.0/gst/gstsegment.h
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
/usr/include/gstreamer-1.0/gst/net/gstptpclock.h
/usr/include/gstreamer-1.0/gst/net/net.h
/usr/lib64/*.so
/usr/lib64/girepository-1.0/Gst-1.0.typelib
/usr/lib64/girepository-1.0/GstBase-1.0.typelib
/usr/lib64/girepository-1.0/GstCheck-1.0.typelib
/usr/lib64/girepository-1.0/GstController-1.0.typelib
/usr/lib64/girepository-1.0/GstNet-1.0.typelib
/usr/lib64/gstreamer-1.0/include/gst/gstconfig.h
/usr/lib64/pkgconfig/*.pc
/usr/share/aclocal/*.m4
/usr/share/gir-1.0/*.gir

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/gtk-doc/html/gstreamer-1.0/GstAllocator.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstBin.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstBuffer.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstBufferList.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstBufferPool.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstBus.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstCaps.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstCapsFeatures.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstChildProxy.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstClock.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstContext.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstControlBinding.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstControlSource.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstDateTime.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstDeviceProviderFactory.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstElement.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstElementFactory.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstEvent.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstGhostPad.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstMemory.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstMessage.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstObject.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstPad.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstPadTemplate.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstPipeline.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstPlugin.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstPluginFeature.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstPreset.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstQuery.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstRegistry.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstSample.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstSegment.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstStructure.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstSystemClock.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstTagList.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstTagSetter.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstTask.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstTaskPool.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstToc.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstTracer.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstTracerFactory.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstTracerRecord.html
/usr/share/gtk-doc/html/gstreamer-1.0/GstTypeFindFactory.html
/usr/share/gtk-doc/html/gstreamer-1.0/annotation-glossary.html
/usr/share/gtk-doc/html/gstreamer-1.0/gst-building.html
/usr/share/gtk-doc/html/gstreamer-1.0/gst-running.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-1.0.devhelp2
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-Gst.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstAtomicQueue.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstConfig.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstDevice.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstDeviceMonitor.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstDeviceProvider.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstFormat.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstGError.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstInfo.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstIterator.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstMeta.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstMiniObject.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstParamSpec.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstParse.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstPoll.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstProtectionMeta.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstTocSetter.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstTypeFind.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstUri.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstUriHandler.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstUtils.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstValue.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-GstVersion.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-device-probing.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-hierarchy.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer-support.html
/usr/share/gtk-doc/html/gstreamer-1.0/gstreamer.html
/usr/share/gtk-doc/html/gstreamer-1.0/home.png
/usr/share/gtk-doc/html/gstreamer-1.0/index.html
/usr/share/gtk-doc/html/gstreamer-1.0/ix01.html
/usr/share/gtk-doc/html/gstreamer-1.0/ix02.html
/usr/share/gtk-doc/html/gstreamer-1.0/ix03.html
/usr/share/gtk-doc/html/gstreamer-1.0/ix04.html
/usr/share/gtk-doc/html/gstreamer-1.0/ix05.html
/usr/share/gtk-doc/html/gstreamer-1.0/ix06.html
/usr/share/gtk-doc/html/gstreamer-1.0/ix07.html
/usr/share/gtk-doc/html/gstreamer-1.0/ix08.html
/usr/share/gtk-doc/html/gstreamer-1.0/left-insensitive.png
/usr/share/gtk-doc/html/gstreamer-1.0/left.png
/usr/share/gtk-doc/html/gstreamer-1.0/libgstreamer.html
/usr/share/gtk-doc/html/gstreamer-1.0/right-insensitive.png
/usr/share/gtk-doc/html/gstreamer-1.0/right.png
/usr/share/gtk-doc/html/gstreamer-1.0/style.css
/usr/share/gtk-doc/html/gstreamer-1.0/up-insensitive.png
/usr/share/gtk-doc/html/gstreamer-1.0/up.png
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstARGBControlBinding.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstAdapter.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstBaseParse.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstBaseSink.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstBaseSrc.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstBaseTransform.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstCollectPads.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstDirectControlBinding.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstInterpolationControlSource.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstLFOControlSource.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstNetClientClock.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstNetTimeProvider.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstPtpClock.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstPushSrc.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstTestClock.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstTimedValueControlSource.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/GstTriggerControlSource.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/annotation-glossary.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gdp-header.png
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-base.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-check.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-control.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-hierarchy.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-1.0.devhelp2
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstBitReader.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstBufferStraw.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstByteReader.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstByteWriter.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstCheck.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstDataQueue.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstFlowCombiner.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstHarness.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstNetAddressMeta.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstNetControlMessageMeta.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstNetTimePacket.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstQueueArray.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstStreamConsistency.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs-GstTypeFindHelper.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-libs.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/gstreamer-net.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/home.png
/usr/share/gtk-doc/html/gstreamer-libs-1.0/index.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/ix01.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/ix02.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/ix03.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/ix04.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/ix05.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/ix06.html
/usr/share/gtk-doc/html/gstreamer-libs-1.0/left-insensitive.png
/usr/share/gtk-doc/html/gstreamer-libs-1.0/left.png
/usr/share/gtk-doc/html/gstreamer-libs-1.0/right-insensitive.png
/usr/share/gtk-doc/html/gstreamer-libs-1.0/right.png
/usr/share/gtk-doc/html/gstreamer-libs-1.0/style.css
/usr/share/gtk-doc/html/gstreamer-libs-1.0/up-insensitive.png
/usr/share/gtk-doc/html/gstreamer-libs-1.0/up.png
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/ch01.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/ch02.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-1.0.devhelp2
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-capsfilter.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-concat.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-downloadbuffer.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-fakesink.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-fakesrc.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-fdsink.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-fdsrc.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-filesink.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-filesrc.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-funnel.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-identity.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-input-selector.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-multiqueue.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-output-selector.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-plugin-coreelements.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-queue.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-queue2.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-streamiddemux.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-tee.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-typefind.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/gstreamer-plugins-valve.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/home.png
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/index.html
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/left-insensitive.png
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/left.png
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/right-insensitive.png
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/right.png
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/style.css
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/up-insensitive.png
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/gstreamer-1.0/libgstcoreelements.so
/usr/lib64/gstreamer-1.0/libgstcoretracers.so

%files locales -f gstreamer-1.0.lang 
%defattr(-,root,root,-)

