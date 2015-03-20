%global provider	github.com
%global project		GoogleCloudPlatform
%global repo		heapster
%global commit		3827a923e14f486c9bb2d6b0ab2c5cf11b60132e

%global import_path	%{provider}/%{project}/%{repo}
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global debug_package	%{nil}

Name:		%{repo}
Version:	0.9
Release:	0.1.git%{shortcommit}%{?dist}
Summary:	Enables monitoring of clusters using cAdvisor
License:	ASL 2.0
URL:		https://%{import_path}
Source0:	https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source1:	heapster
Source2:	heapster.service

BuildRequires:	git
BuildRequires:	systemd
BuildRequires:	golang >= 1.2.1-3
ExclusiveArch:	x86_64

%description
%{summary}

Heapster supports Kubernetes natively and collects resource usage of all the
pods running in the cluster. It was built to showcase the power of core
Kubernetes concepts like labels and pods and the awesomeness that is cAdvisor.


%prep
%autosetup -Sgit -n %{name}-%{commit}

%build
pushd Godeps/_workspace
  mkdir -p src/github.com/%{project}
  ln -s $(dirs +1 -l) src/github.com/%{project}/heapster
popd

export GOPATH=$PWD/Godeps/_workspace:%{gopath}
go build %{provider}/%{project}/heapster

%install
# main package binary
install -d -p %{buildroot}%{_bindir}
install -p -m0755 heapster %{buildroot}%{_bindir}

# install systemd/sysconfig
install -d -m0755 %{buildroot}%{_sysconfdir}/sysconfig/
install -p -m0660 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -d -m0755 %{buildroot}%{_unitdir}
install -p -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

# install run an log
install -d -m0755 %{buildroot}%{_localstatedir}/run/%{name}
touch %{buildroot}%{_localstatedir}/run/%{name}/hosts
install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}

%post
%systemd_post heapster.service

%preun
%systemd_preun heapster.service

%postun
%systemd_postun

%files
%doc CONTRIBUTING.md LICENSE README.md RELEASES.md
%{_bindir}/heapster
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_localstatedir}/run/%{name}
%dir %{_localstatedir}/log/%{name}
%{_localstatedir}/run/%{name}/hosts

%changelog
* Wed Mar 18 2015 Federico Simoncelli <fsimonce@redhat.com> - 0.9-0.1.git3827a92
- first build
