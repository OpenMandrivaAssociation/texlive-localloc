%global tl_name localloc
%global tl_revision 56496

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros for localizing TeX register allocations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/localloc
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/localloc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/localloc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/localloc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package approaches the problem of the shortage of registers, by
providing a mechanism for local allocation. The package works with Plain
TeX, LaTeX, and LaTeX 2.09.

