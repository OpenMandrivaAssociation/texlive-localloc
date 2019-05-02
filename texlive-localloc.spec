# revision 21934
# category Package
# catalog-ctan /macros/latex/contrib/localloc
# catalog-date 2009-10-06 14:55:10 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-localloc
Version:	20190228
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091006-2
+ Revision: 753410
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091006-1
+ Revision: 718877
- texlive-localloc
- texlive-localloc
- texlive-localloc
- texlive-localloc

