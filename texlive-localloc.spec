Name:		texlive-localloc
Version:	20091006
Release:	1
Summary:	Macros for localizing TeX register allocations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/localloc
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/localloc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/localloc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/localloc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package approaches the problem of the shortage of
registers, by providing a mechanism for local allocation. The
package works with Plain TeX, LaTeX and LaTeX 2.09.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/localloc/localloc.sty
%doc %{_texmfdistdir}/doc/latex/localloc/localloc.README
%doc %{_texmfdistdir}/doc/latex/localloc/localloc.pdf
%doc %{_texmfdistdir}/doc/latex/localloc/localtst.tex
#- source
%doc %{_texmfdistdir}/source/latex/localloc/localloc.drv
%doc %{_texmfdistdir}/source/latex/localloc/localloc.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
