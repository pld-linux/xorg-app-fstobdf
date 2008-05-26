Summary:	fstobdf application - generate BDF font from X font server
Summary(pl.UTF-8):	Aplikacja fstobdf - generowanie fontów BDF z serwera fontów X
Name:		xorg-app-fstobdf
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/fstobdf-%{version}.tar.bz2
# Source0-md5:	49a6225380f6c18fff664a043cd569b1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fstobdf program reads a font from X font server and prints a BDF
file on the standard output that may be used to recreate the font.
This is useful in testing servers, debugging font metrics, and
reproducing lost BDF files.

%description -l pl.UTF-8
Program fstobdf czyta font z serwera fontów X i wypisuje na
standardowe wyjście plik BDF, który może służyć do odtworzenia fontu.
Jest to przydatne do testowania serwerów, diagnostyki metryk fontów i
odzyskiwania utraconych plików BDF.

%prep
%setup -q -n fstobdf-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/fstobdf
%{_mandir}/man1/fstobdf.1x*
