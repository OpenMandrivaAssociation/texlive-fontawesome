%global tl_name fontawesome
%global tl_revision 78348
%global tl_version 4.6.3.2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Font containing web-related icons
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fontawesome
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontawesome.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontawesome.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package offers access to the large number of web-related icons
provided by the included font. The package requires the package,
fontspec, if run with XeTeX or LuaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from fontawesome:
Map fontawesome.map
TL_DROPIN_EOF
