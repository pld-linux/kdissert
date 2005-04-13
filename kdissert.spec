%define		_pre	pre6
Summary:	kdissert is a mindmapping-like tool to help students to produce complicated documents
Summary(pl):	kdissert wspiera tworzenie map my¶li
Name:		kdissert
Version:	0.3.9
Release:	0.%{_pre}.1
License:	GPL
Group:		Applications
Source0:	http://freehackers.org/~tnagy/%{name}/%{name}-%{version}.%{_pre}.tar.bz2
# Source0-md5:	2b4df25dff5a12dc496ec2570c81fc62
Source1:	%{name}-kde.py
URL:		http://freehackers.org/~tnagy/kdissert/
BuildRequires:	scons
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of kdissert is to help to structure ideas and concepts. Ideas
are first layed down on a canvas and then associated into a tree. The
tree is there to help to see how the ideas interact, and then to
develop them further (by adding ramifications). An idea is represented
by a shape which contains several a summary (visible part), several
text fields, and optional pictures and url links.

%description -l pl
Celem kdissert jest u³atwienie strukturalnej organizacji idei i koncepcji.
Idee s± najpierw rozk³adane na p³ótnie, a nastêpnie budowane jest z nich drzewo,
które ma u³atwiæ zrozumienie sposobu w jaki sposób ³±cz± siê ze sob± zadane idee.
Idea jest reprezentowana przez kszta³t, który mo¿e zawieraæ opis; pola tekstowe
oraz je¶li zachodzi taka potrzeba obrazki i odno¶niki.

%prep
%setup -q -n %{name}-%{version}.%{_pre}
%{__sed} -i -e 's/Categories=.*/Categories=QT;KDE;Education;/g' src/appdata/kdissert.desktop
install %{SOURCE1} ./kde.py

%build
export CXXFLAGS="%{rpmcflags}"
export QTDIR="%{_usr}"
# autodetects all needed paths from kde-config not sure it supports amd64 at the moment
# im talking about it with the maintainer of kde's scons-based buildsystem
scons configure qtincludes=%{_includedir}/qt prefix=%{_prefix} %{?debug:debug=full} \
	qtlibs=%{_libdir}
scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT scons install

%find_lang %{name} --with-kde 

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdissert
%{_libdir}/kde3/libkdissOOOdoc.la
%attr(755,root,root) %{_libdir}/kde3/libkdissOOOdoc.so
%{_libdir}/kde3/libkdissOOOimpress.la
%attr(755,root,root) %{_libdir}/kde3/libkdissOOOimpress.so
%{_libdir}/kde3/libkdissapplet.la
%attr(755,root,root) %{_libdir}/kde3/libkdissapplet.so
%{_libdir}/kde3/libkdissasciidoc.la
%attr(755,root,root) %{_libdir}/kde3/libkdissasciidoc.so
%{_libdir}/kde3/libkdissbeamerslides.la
%attr(755,root,root) %{_libdir}/kde3/libkdissbeamerslides.so
%{_libdir}/kde3/libkdisshtmldoc.la
%attr(755,root,root) %{_libdir}/kde3/libkdisshtmldoc.so
%{_libdir}/kde3/libkdisspdflatexarticle.la
%attr(755,root,root) %{_libdir}/kde3/libkdisspdflatexarticle.so
%{_libdir}/kde3/libkdisspdflatexbook.la
%attr(755,root,root) %{_libdir}/kde3/libkdisspdflatexbook.so
%{_libdir}/kde3/libkdissprosperslides.la
%attr(755,root,root) %{_libdir}/kde3/libkdissprosperslides.so
%{_desktopdir}/kde/kdissert.desktop
%{_datadir}/apps/kdissert/kdissertui.rc
%{_datadir}/apps/kdissert/pics/nopix.png
%{_datadir}/apps/kdissert/templatedata/kdissOOOdoc.tar.gz
%{_datadir}/apps/kdissert/templatedata/kdissOOOimpress.tar.gz
%{_datadir}/apps/kdissert/templatedata/kdissapplet.tar.gz
%{_datadir}/apps/kdissert/templatedata/kdissasciidoc.tar.gz
%{_datadir}/apps/kdissert/templatedata/kdissbeamerslides.tar.gz
%{_datadir}/apps/kdissert/templatedata/kdisshtmldoc.tar.gz
%{_datadir}/apps/kdissert/templatedata/kdisspdflatexarticle.tar.gz
%{_datadir}/apps/kdissert/templatedata/kdisspdflatexbook.tar.gz
%{_datadir}/apps/kdissert/templatedata/kdissprosperslides.tar.gz
%{_datadir}/apps/kdissert/tips
%{_datadir}/apps/kdissertpart/kdissertpart.rc
%{_datadir}/config.kcfg/kdissert.kcfg
%{_iconsdir}/crystalsvg/128x128/actions/kdissert_sort.png
%{_iconsdir}/crystalsvg/16x16/actions/kdissert_link.png
%{_iconsdir}/crystalsvg/16x16/actions/kdissert_point.png
%{_iconsdir}/crystalsvg/16x16/actions/kdissert_sort.png
%{_iconsdir}/crystalsvg/22x22/actions/kdissert_link.png
%{_iconsdir}/crystalsvg/22x22/actions/kdissert_point.png
%{_iconsdir}/crystalsvg/22x22/actions/kdissert_sort.png
%{_iconsdir}/crystalsvg/32x32/actions/kdissert_link.png
%{_iconsdir}/crystalsvg/32x32/actions/kdissert_point.png
%{_iconsdir}/crystalsvg/32x32/actions/kdissert_sort.png
%{_iconsdir}/crystalsvg/64x64/actions/kdissert_sort.png
%{_iconsdir}/hicolor/128x128/apps/kdissert.png
%{_iconsdir}/hicolor/16x16/apps/kdissert.png
%{_iconsdir}/hicolor/22x22/apps/kdissert.png
%{_iconsdir}/hicolor/32x32/apps/kdissert.png
%{_iconsdir}/hicolor/64x64/apps/kdissert.png
%{_datadir}/mimelnk/application/x-kdissert.desktop
%{_datadir}/services/kdissertpart.desktop
