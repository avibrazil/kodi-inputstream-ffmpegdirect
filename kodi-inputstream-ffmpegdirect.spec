%global aname inputstream.ffmpegdirect
%global kodi_version 19.0
%global kodi_codename Matrix

Name:           kodi-inputstream-ffmpegdirect
Version:        19.0.3
Release:        2%{?dist}
Summary:        Kodi input stream addon for streams that can be opened by either FFmpeg's libavformat or Kodi's cURL
License:        GPLv2+
URL:            https://github.com/xbmc/inputstream.ffmpegdirect
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{aname}-%{version}-%{kodi_codename}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
%if 0%{?_with_external_ffmpeg}
%if 0%{?fedora} && 0%{?fedora} > 35
BuildRequires: compat-ffmpeg4-devel
%else
BuildRequires: ffmpeg-devel
%endif
%else
BuildRequires: trousers-devel
%endif

Requires:       kodi >= %{kodi_version}

ExcludeArch:    %{power64}

%description
%{summary}.


%prep
%setup -q -n %{aname}-%{version}-%{kodi_codename}

# Fix spurious-executable-perm on debug package
find . -name '*.h' -or -name '*.cpp' | xargs chmod a-x


%build
%if 0%{?fedora} && 0%{?fedora} > 35
export PKG_CONFIG_PATH="%{_libdir}/compat-ffmpeg4/pkgconfig"
%endif
%cmake3
%cmake3_build


%install
%cmake3_install

# Fix permissions at installation
find $RPM_BUILD_ROOT%{_datadir}/kodi/addons/ -type f -exec chmod 0644 {} \;


%files
%doc README.md
%license LICENSE.md
%{_libdir}/kodi/addons/%{aname}/
%{_datadir}/kodi/addons/%{aname}/


%changelog
* Sat Aug 13 2022 Avi Alkalay <avi@unix.sh> - 19.0.3-1
- First build attempt on Fedora 36
