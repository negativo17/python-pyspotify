%global real_name pyspotify

%global commit0 770aee08de274951b63e60bdd8835188b58e7862
%global date 2021810
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:           python-pyspotify
Version:        2.1.3
Release:        5%{!?tag:.%{date}git%{shortcommit0}}%{?dist}
Summary:        Python bindings for libspotify
License:        MIT
URL:            https://pyspotify.readthedocs.io/

%if 0%{?tag:1}
Source0:        https://github.com/jodal/%{real_name}/archive/v%{version}.tar.gz#/%{real_name}-%{version}.tar.gz
%else
Source0:        https://github.com/jodal/%{real_name}/archive/%{commit0}.tar.gz#/%{real_name}-%{shortcommit0}.tar.gz
%endif

BuildRequires:  gcc
BuildRequires:  libspotify-devel
BuildRequires:  python3-devel

%global _description %{expand:
pyspotify provides a Python interface to Spotify's online music streaming
service. With pyspotify you can access music metadata, search in Spotify's
library of 20+ million tracks, manage your Spotify playlists, and play music
from Spotify. All from your own Python applications.

pyspotify uses CFFI to make a pure Python wrapper around the official libspotify
library.}

%description %_description

%package     -n python3-%{real_name}
Summary:        %{summary}

%description -n python3-%{real_name} %_description

%prep
%if 0%{?tag:1}
%autosetup -n %{real_name}-%{version}
%else
%autosetup -n %{real_name}-%{commit0}
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spotify

%check
%py3_check_import spotify

%files -n python3-%{real_name}
%license LICENSE
%doc README.rst AUTHORS
%{python3_sitearch}/%{real_name}-%{version}.dist-info/
%{python3_sitearch}/spotify/

%changelog
* Mon Sep 27 2021 Simone Caronni <negativo17@gmail.com> - 2.1.3-5.2021810git770aee0
- Update to latest 2.1.4 snapshot.
- Update SPEC file to latest packaging guidelines.

* Wed Sep 22 2021 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-4.20210306git515ac42
- Add BR: python3-setuptools to fix build on Fedora 35+.

* Thu May 27 2021 Simone Caronni <negativo17@gmail.com> - 2.1.3-3.20210306git515ac42
- Update to latest snapshot.
- Fix source URL.

* Sat Nov 21 2020 Simone Caronni <negativo17@gmail.com> - 2.1.3-2
- Update build requirements.

* Sun Jun 14 2020 Simone Caronni <negativo17@gmail.com> - 2.1.3-1
- First build.
