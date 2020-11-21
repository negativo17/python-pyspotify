%global real_name pyspotify

Name:           python-pyspotify
Version:        2.1.3
Release:        2%{?dist}
Summary:        Python bindings for libspotify
License:        MIT
URL:            https://pyspotify.readthedocs.io/

Source0:        https://github.com/jodal/%{name}/archive/v%{version}.tar.gz#/%{real_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libspotify-devel
BuildRequires:  python3-devel
BuildRequires:  python3-cffi

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
%autosetup -n %{real_name}-%{version}

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
* Sat Nov 21 2020 Simone Caronni <negativo17@gmail.com> - 2.1.3-2
- Update build requirements.

* Sun Jun 14 2020 Simone Caronni <negativo17@gmail.com> - 2.1.3-1
- First build.
