Name:		texlive-profcollege
Version:	69343
Release:	1
Summary:	A LaTeX package for French maths teachers in college
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/profcollege
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/profcollege.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/profcollege.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides some commands to help French mathematics
teachers for 11-16 years olds, for example: \Tableau[Metre] to
write the tabular km|hm|... with some facilities,
\Pythagore{ABC}{5}{7} to write the entire calculation of AC
with the Pythagorean theorem, \Trigo[Cosinus]{ABC}{3}{}{60} to
write the entire calculation of AC with cosine, ... and some
others.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/profcollege
%{_texmfdistdir}/metapost/profcollege
%doc %{_texmfdistdir}/doc/latex/profcollege

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
