Summary:	Ruby binding to the evas library
Summary(pl):	Dowi±zania jêzyka Ruby do biblioteki evas
Name:		ruby-evas
Version:	0
Release:	2
License:	Ruby's
Group:		Development/Languages
Source0:	%{name}.tar.gz
# Source0-md5:	3257203bb047d370cd86460b83f709d4
URL:		http://code-monkey.de/projects/ruby-efl.html
BuildRequires:	evas-devel
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%ruby_mod_ver_requires_eq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding to the evas library.

%description -l pl
Dowi±zania jêzyka Ruby do biblioteki evas.

%package devel
Summary:	Header files for ruby-evas
Summary(pl):	Pliki nag³ówkowe ruby-evas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ruby-evas.

%description devel -l pl
Pliki nag³ówkowe ruby-evas.

%prep
%setup -q -n %{name}

%build
rake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

DESTDIR=$RPM_BUILD_ROOT RUBYARCHDIR=%{ruby_archdir} rake install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/evas.so

%files devel
%defattr(644,root,root,755)
%{ruby_archdir}/evas
