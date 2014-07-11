# revision 31020
# category Package
# catalog-ctan /fonts/fontawesome
# catalog-date 2013-06-12 15:49:49 +0200
# catalog-license other-free
# catalog-version 3.1.1
Name:		texlive-fontawesome
Version:	3.1.1
Release:	7
Summary:	Font containing web-related icons
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fontawesome
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontawesome.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontawesome.doc.tar.xz
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
%{_texmfdistdir}/fonts/opentype/public/fontawesome/FontAwesome.otf
%{_texmfdistdir}/tex/latex/fontawesome/fontawesome.sty
%doc %{_texmfdistdir}/doc/latex/fontawesome/README
%doc %{_texmfdistdir}/doc/latex/fontawesome/fontawesome.pdf
%doc %{_texmfdistdir}/doc/latex/fontawesome/fontawesome.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
