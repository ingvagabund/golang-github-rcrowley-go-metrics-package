%global debug_package   %{nil}
%global import_path     github.com/rcrowley/go-metrics
%global commit          3be59ceb5538550555459fb77d0efe0e218cdfc7
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-rcrowley-go-metrics
Version:        0
Release:        0.0.git%{shortcommit}%{?dist}
Summary:        Go port of Coda Hales Metrics library
License:        BSD
URL:            https://github.com/rcrowley/go-metrics
Source0:        https://github.com/rcrowley/go-metrics/archive/%{commit}/%{name}-%{commit}.tar.gz
ExclusiveArch:  %{go_arches} noarch

%description
Go port of Coda Hales Metrics library

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        Go port of Coda Hales Metrics library
Provides:       golang(%{import_path}) = %{version}-%{release}
BuildArch:      noarch

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{commit}

%build
# the ./cmd pieces are presently examples

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}
# we're not providing the ./influxdb, ./stathat, or ./librato pieces yet,
# since they have additional dependencies and the core of this library isn't dependent of these pieces

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.md
%dir %attr(755,root,root) %{gopath}/src/github.com/rcrowley
%dir %attr(755,root,root) %{gopath}/src/github.com/rcrowley/go-metrics
%{gopath}/src/%{import_path}/*.go

%changelog
* Thu Jul 17 2014 Colin Walters <walters@verbum.org> 0-0.0.git3be59ce
- Initial package
