%global tl_name mycv
%global tl_revision 26807

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.6
Release:	%{tl_revision}.1
Summary:	A list-driven CV class, allowing TikZ decorations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mycv
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mycv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mycv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mycv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class provides a set of functionality for writing "curriculum vitae"
with different layouts. The idea is that a user can write some custom
configuration directives, by means of which is possible both to produce
different c.v. layouts and quickly switch among them. In order to
process such directives, the class uses a set of lists, provided by the
package etextools. Basic support for using TikZ decorations is also
provided.

