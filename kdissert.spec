Summary:	kdissert - a mindmapping-like tool to help students to produce complicated documents
Summary(pl):	kdissert - narzêdzie wspomagaj±ce tworzenie map my¶li
Name:		kdissert
Version:	1.0.6c
Release:	1
License:	GPL
Group:		Applications
Source0:	http://freehackers.org/~tnagy/kdissert/%{name}-%{version}.tar.bz2
# Source0-md5:	cd7116fb61ee4cf7b87c8916ef5f7a5f
Source1:	http://freehackers.org/~tnagy/waf
# Source1-md5:	2c80272d967e6d9dded444d5ef2ac8e8
URL:		http://freehackers.org/~tnagy/kdissert/
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of kdissert is to help to structure ideas and concepts. Ideas
are first layed down on a canvas and then associated into a tree. The
tree is there to help to see how the ideas interact, and then to
develop them further (by adding ramifications). An idea is represented
by a shape which contains several a summary (visible part), several
text fields, and optional pictures and url links.

%description -l pl
Celem kdissert jest u³atwienie strukturalnej organizacji idei i
koncepcji. Idee s± najpierw rozk³adane na p³ótnie, a nastêpnie
budowane jest z nich drzewo, które ma u³atwiæ zrozumienie sposobu w
jaki sposób ³±cz± siê ze sob± dane idee. Idea jest reprezentowana
przez kszta³t, który mo¿e zawieraæ opis; pola tekstowe oraz je¶li
zachodzi taka potrzeba obrazki i odno¶niki.

%prep
%setup -q
%{__sed} -i -e 's/Categories=.*/Categories=QT;KDE;Education;/g' src/appdata/kdissert.desktop

%build
export CXXFLAGS="%{rpmcflags}"
export QTDIR="%{_usr}"

# workaround for broken waf file. Waf building system was creating some hidden files in
# user direcotry (.waf-version, .wafcache). Below the new version of waf is installed. 
# This one creates these files in rpm/BUILD/kdissert-version directory. In case of upgrade
# check if it is still necessary.
rm waf
install -m 755 %{SOURCE1} ./

# To install waf directories (.waf-version, .wafcache) in building directory.
export WAF_HOME=`pwd`

# autodetects all needed paths from kde-config not sure it supports amd64 at the moment
# im talking about it with the maintainer of kde's scons-based buildsystem

./waf configure \
	--qtincludes=%{_includedir}/qt \
	--prefix=%{_prefix} %{?debug:debug=full} \
%if "%{_lib}" == "lib64"
	--libsuffix=64 \
%endif
	--qtlibs=%{_libdir}
./waf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
./waf install --destdir $RPM_BUILD_ROOT

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
