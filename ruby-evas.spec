%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby binding to the evas library
Name:		ruby-evas
Version:	0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	ruby-evas.tar.gz
# Source0-md5:	3257203bb047d370cd86460b83f709d4
URL:		http://code-monkey.de/projects/ruby-efl.html
BuildRequires:	rake
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	evas-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding to the Evas library.

%package devel
Summary: Header files for ruby-evas
Group:	Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for ruby-evas.

%prep
%setup -q -n ruby-evas

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
%{ruby_archdir}/evas.so

%files devel
%{ruby_archdir}/evas
