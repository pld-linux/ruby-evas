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
#BuildRequires:	setup.rb = 3.3.1
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding to the Evas library.

%prep
%setup -q -n ruby-evas
cp %{_datadir}/setup.rb .
mkdir ext
mv src ext/evas
ls ext/evas/*.c > ext/evas/MANIFEST
cat > ext/evas/extconf.rb <<EOF
require 'mkmf'
have_library('evas', 'evas_list_append') or exit 1
create_makefile('evas', '.')
EOF

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}
ruby setup.rb setup

#rdoc --op rdoc ext
#rdoc --ri --op ri ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_archdir}/evas.so
