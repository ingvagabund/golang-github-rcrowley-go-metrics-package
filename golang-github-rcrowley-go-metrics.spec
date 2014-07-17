%global debug_package   %{nil}
%global import_path     github.com/rcrowley/go-metrics
%global gopath          %{_datadir}/gocode
%global commit          3be59ceb5538550555459fb77d0efe0e218cdfc7
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-rcrowley-go-metrics
Version:        0
Release:        0.0.git%{shortcommit}%{?dist}
Summary:        Go port of Coda Hales Metrics library
License:        BSD
URL:            https://github.com/rcrowley/go-metrics
Source0:        https://github.com/rcrowley/go-metrics/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:      noarch

%description
Go port of Coda Hales Metrics library

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        Go port of Coda Hales Metrics library
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -n %{name}-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.md
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/github.com
%dir %attr(755,root,root) %{gopath}/src/github.com/rcrowley
%dir %attr(755,root,root) %{gopath}/src/github.com/rcrowley/go-metrics
%{gopath}/src/%{import_path}/*.go

%changelog
* Thu Jul 17 2014 Colin Walters <walters@verbum.org>
- Initial package
