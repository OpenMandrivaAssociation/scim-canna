%define version	1.0.1
%define release	%mkrel 1

%define scim_version	1.4.0
%define canna_version	3.7p3

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-canna
Summary:	SCIM IMEngine module for Canna
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPLv2+
URL:		http://sourceforge.jp/projects/scim-imengine/
Source0:	http://osdn.dl.sourceforge.jp/scim-imengine/29155/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes:	%libname
Requires:		canna >= %{canna_version}
Requires:		scim-client = %{scim_api}
BuildRequires:		canna >= %{canna_version}
BuildRequires:		canna-devel >= %{canna_version}
BuildRequires:		scim-devel >= 1.4.7-3mdk
BuildRequires:		automake, libltdl-devel

%description
Scim-canna is an SCIM IMEngine module for Canna.
It supports Japanese input.

%prep
%setup -q
cp /usr/share/automake-1.10/mkinstalldirs .

%build
[[ ! -x configure ]] && ./bootstrap
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%{scim_plugins_dir}/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%_datadir/scim/icons/scim-canna.png
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so
