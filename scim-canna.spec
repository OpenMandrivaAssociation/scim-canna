%define version	1.0.0
%define release	%mkrel 2

%define scim_version	1.4.0
%define canna_version	3.7p3

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-canna
Summary:	Scim-canna is an SCIM IMEngine module for Canna
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.jp/projects/scim-imengine/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		%{libname} = %{version}
Requires:		canna >= %{canna_version}
Requires:		scim >= %{scim_version}
BuildRequires:		canna >= %{canna_version}
BuildRequires:		canna-devel >= %{canna_version}
BuildRequires:		scim-devel >= 1.4.7-3mdk
BuildRequires:		automake, libltdl-devel

%description
Scim-canna is an SCIM IMEngine module for Canna.
It supports Japanese input.


%package -n	%{libname}
Summary:	Scim-canna library
Group:		System/Internationalization

%description -n %{libname}
scim-canna library.


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

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%_datadir/scim/icons/scim-canna.png

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so
