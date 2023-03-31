Name:		texlive-fontawesome
Version:	48145
Release:	2
Summary:	Font containing web-related icons
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fontawesome
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontawesome.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontawesome.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers access to the large number of web-related
icons provided by the included font. The package requires the
package, fontspec, running under XeTeX or LuaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/fontawesome
%{_texmfdistdir}/tex/latex/fontawesome
%{_texmfdistdir}/fonts/enc/dvips/fontawesome
%{_texmfdistdir}/fonts/map/dvips/fontawesome
%{_texmfdistdir}/fonts/tfm/public/fontawesome
%{_texmfdistdir}/fonts/type1/public/fontawesome
%doc %{_texmfdistdir}/doc/fonts/fontawesome

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
