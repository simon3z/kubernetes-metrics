%global provider	github.com
%global project		grafana
%global repo		grafana
%global commit		15cb1d898032fe09489f933aade1dc88c0523fb3

%global import_path	%{provider}/%{project}/%{repo}
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global debug_package	%{nil}

Name:		%{repo}
Version:	1.9.1
Release:	0.1.git%{shortcommit}%{?dist}
Summary:	Dashboard and graph editor for Graphite, InfluxDB and OpenTSDB
License:	ASL 2.0
URL:		https://%{import_path}
Source0:	https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
BuildArch:	noarch

BuildRequires:	git

Requires(pre):	httpd

%description
%{summary}


%prep
%autosetup -Sgit -n %{name}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}/

%post

%preun

%postun

%files
%doc CHANGELOG.md LICENSE.md NOTICE.md README.md
%{_datadir}/%{name}

%changelog
* Wed Mar 18 2015 Federico Simoncelli <fsimonce@redhat.com> - 1.9.1-0.1.git15cb1d8
- first build
