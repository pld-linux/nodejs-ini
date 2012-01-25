%define		git_hash c730e12
%define		pkg	ini
Summary:	An INI parser/serializer for node.js
Name:		nodejs-%{pkg}
Version:	1.0.1
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/ini
# download from https://github.com/isaacs/ini/tarball/%{version}
Source0:	isaacs-%{pkg}-%{version}-0-g%{git_hash}.tar.gz
# Source0-md5:	07cb2acef7257f1431d5f0bd07365eee
#BuildRequires:  nodejs-tap
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An INI file parser and serializer for node.js.

%prep
%setup -qc
mv isaacs-%{pkg}-*/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}
cp -p %{pkg}.js $RPM_BUILD_ROOT%{nodejs_libdir}

# We currently don't run tests because I'd have to file another ten or
# so review reuqests for the node.js TAP testing framework and methinks there
# are enough of those for now.  ;-)
##%%check
##tap test/*.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}.js
