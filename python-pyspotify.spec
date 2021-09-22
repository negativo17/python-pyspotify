%global real_name pyspotify

%global commit0 515ac42ab47724ca66e2da7516b96b6838864cfa
%global date 20210306
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:           python-pyspotify
Version:        2.1.3
Release:        4%{!?tag:.%{date}git%{shortcommit0}}%{?dist}
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
BuildRequires:  python3-cffi
BuildRequires:  python3-setuptools

%description
pyspotify provides a Python interface to Spotify's online music streaming
service. With pyspotify you can access music metadata, search in Spotify's
library of 20+ million tracks, manage your Spotify playlists, and play music
from Spotify. All from your own Python applications.

pyspotify uses CFFI to make a pure Python wrapper around the official libspotify
library.

%package     -n python3-pyspotify
Summary:        Python bindings for libspotify

%description -n python3-pyspotify
pyspotify provides a Python interface to Spotify's online music streaming
service. With pyspotify you can access music metadata, search in Spotify's
library of 20+ million tracks, manage your Spotify playlists, and play music
from Spotify. All from your own Python applications.

pyspotify uses CFFI to make a pure Python wrapper around the official libspotify
library.

%prep
%if 0%{?tag:1}
%autosetup -n %{real_name}-%{version}
%else
%autosetup -n %{real_name}-%{commit0}
%endif

%build
CFLAGS="%optflags" %{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

#%check
#%{__python3} setup.py test

%files -n python3-pyspotify
%license LICENSE
%doc README.rst AUTHORS
%{python3_sitearch}/*

%changelog
* Wed Sep 22 2021 Fabio Valentini <decathorpe@gmail.com> - 2.1.3-4.20210306git515ac42
- Add BR: python3-setuptools to fix build on Fedora 35+.

* Thu May 27 2021 Simone Caronni <negativo17@gmail.com> - 2.1.3-3.20210306git515ac42
- Update to latest snapshot.
- Fix source URL.

* Sat Nov 21 2020 Simone Caronni <negativo17@gmail.com> - 2.1.3-2
- Update build requirements.

* Sun Jun 14 2020 Simone Caronni <negativo17@gmail.com> - 2.1.3-1
- First build.
