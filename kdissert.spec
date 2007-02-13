Summary:	kdissert - a mindmapping-like tool to help students to produce complicated documents
Summary(pl.UTF-8):	kdissert - narzędzie wspomagające tworzenie map myśli
Name:		kdissert
Version:	1.0.7
Release:	2
License:	GPL
Group:		Applications
Source0:	http://freehackers.org/~tnagy/kdissert/%{name}-%{version}.tar.bz2
# Source0-md5:	8e72785b8ab2adfc959522fcdcec10e6
URL:		http://freehackers.org/~tnagy/kdissert/
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.335
BuildRequires:	waf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq      libtool(.*)

%description
The goal of kdissert is to help to structure ideas and concepts. Ideas
are first layed down on a canvas and then associated into a tree. The
tree is there to help to see how the ideas interact, and then to
develop them further (by adding ramifications). An idea is represented
by a shape which contains several a summary (visible part), several
text fields, and optional pictures and url links.

%description -l pl.UTF-8
Celem kdissert jest ułatwienie strukturalnej organizacji idei i
koncepcji. Idee są najpierw rozkładane na płótnie, a następnie
budowane jest z nich drzewo, które ma ułatwić zrozumienie sposobu w
jaki sposób łączą się ze sobą dane idee. Idea jest reprezentowana
przez kształt, który może zawierać opis; pola tekstowe oraz jeśli
zachodzi taka potrzeba obrazki i odnośniki.

%prep
%setup -q
%{__sed} -i -e 's/Categories=.*/Categories=QT;KDE;Education;/g' src/appdata/kdissert.desktop

%build
export QTDIR="%{_usr}"

# autodetects all needed paths from kde-config not sure it supports amd64 at the moment
# im talking about it with the maintainer of kde's scons-based buildsystem

%waf configure \
	--prefix=%{_prefix} %{?debug:debug=full} \
	--qtincludes=%{_includedir}/qt \
%if "%{_lib}" == "lib64"
	--libsuffix=64 \
%endif
	--qtlibs=%{_libdir}

%waf

%install
rm -rf $RPM_BUILD_ROOT

%waf install \
	--destdir $RPM_BUILD_ROOT

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
%{_libdir}/kde3/libkdissdocbook.la
%attr(755,root,root) %{_libdir}/kde3/libkdissdocbook.so
%{_libdir}/kde3/libkdissstx.la
%attr(755,root,root) %{_libdir}/kde3/libkdissstx.so
%{_desktopdir}/kde/kdissert.desktop
%{_datadir}/apps/kdissert
%{_datadir}/apps/kdissertpart
%{_datadir}/config.kcfg/kdissert.kcfg
%{_iconsdir}/hicolor/*/*/*.png
%{_datadir}/mimelnk/application/x-kdissert.desktop
%{_datadir}/services/kdissertpart.desktop
%{_datadir}/applnk/Utilities/kdissert.desktop
