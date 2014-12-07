# revision 26807
# category Package
# catalog-ctan /macros/latex/contrib/mycv
# catalog-date 2012-05-21 10:58:59 +0200
# catalog-license lppl1.3
# catalog-version 1.5.6
Name:		texlive-mycv
Version:	1.5.6
Release:	8
Summary:	A list-driven CV class, allowing TikZ decorations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mycv
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mycv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mycv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mycv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides a set of functionality for writing
"curriculum vitae" with different layouts. The idea is that a
user can write some custom configuration directives, by means
of which is possible both to produce different c.v. layouts and
quickly switch among them. In order to process such directives,
the class uses a set of lists, provided by the package
etextools. Basic support for using TikZ decorations is also
provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/mycv/mycv_split_contents.pl
%{_texmfdistdir}/tex/latex/mycv/mycv.cls
%{_texmfdistdir}/tex/latex/mycv/mycv_base.def
%{_texmfdistdir}/tex/latex/mycv/mycv_dec.sty
%{_texmfdistdir}/tex/latex/mycv/mycv_misc.def
%{_texmfdistdir}/tex/latex/mycv/mycv_style.sty
%{_texmfdistdir}/tex/latex/mycv/mycv_version.def
%doc %{_texmfdistdir}/doc/latex/mycv/CHANGELOG
%doc %{_texmfdistdir}/doc/latex/mycv/Doc/Images/logo-1.png
%doc %{_texmfdistdir}/doc/latex/mycv/Doc/mycv.tex
%doc %{_texmfdistdir}/doc/latex/mycv/Examples/Notes.txt
%doc %{_texmfdistdir}/doc/latex/mycv/Examples/mycv-example-dpl.pdf
%doc %{_texmfdistdir}/doc/latex/mycv/Examples/mycv-example-dpl2.pdf
%doc %{_texmfdistdir}/doc/latex/mycv/Examples/mycv-example-spl.pdf
%doc %{_texmfdistdir}/doc/latex/mycv/Examples/mycv-example-spl2.pdf
%doc %{_texmfdistdir}/doc/latex/mycv/Examples/mycv-examples.dtx
%doc %{_texmfdistdir}/doc/latex/mycv/README
%doc %{_texmfdistdir}/doc/latex/mycv/checksum.pl
%doc %{_texmfdistdir}/doc/latex/mycv/mycv.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mycv/mycv.dtx
%doc %{_texmfdistdir}/source/latex/mycv/mycv.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5.6-1
+ Revision: 812637
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5.4-1
+ Revision: 804949
- Import texlive-mycv
- Import texlive-mycv

