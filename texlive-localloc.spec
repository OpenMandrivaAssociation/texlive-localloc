Name:		texlive-localloc
Version:	56496
Release:	2
Summary:	Macros for localizing TeX register allocations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/localloc
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/localloc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/localloc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/localloc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package approaches the problem of the shortage of
registers, by providing a mechanism for local allocation. The
package works with Plain TeX, LaTeX and LaTeX 2.09.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/localloc
%doc %{_texmfdistdir}/doc/generic/localloc
#- source
%doc %{_texmfdistdir}/source/generic/localloc

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
