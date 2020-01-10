%define GTOOL /usr/bin/gconftool-2

Summary: Small desktop tweaks such as default buttons on panel
Name: SL_desktop_tweaks
Version: 6
Release: 2
License:        GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
Obsoletes: zz_desktop_tweeks, SL_desktop_tweeks
BuildRoot: %{_tmppath}/%{name}-%{version}root

%description
This changes minor desktop annoyances, such as the default buttons on 
Gnome's panel.

%prep
%setup -q

%install
#put in files
mkdir -p $RPM_BUILD_ROOT/usr/share/config
cp -r * $RPM_BUILD_ROOT/usr/share/config


%triggerin -- gnome-panel
if [ -f %{GTOOL} ] ; then
	export GCONF_CONFIG_SOURCE=`%{GTOOL} --get-default-source`
	%{GTOOL} --direct --config-source=$GCONF_CONFIG_SOURCE --load /usr/share/config/panel-default-setup.SL.entries > /dev/null
	%{GTOOL} --direct --config-source=$GCONF_CONFIG_SOURCE --load /usr/share/config/panel-default-setup.SL.entries /apps/panel > /dev/null
fi

%triggerpostun -- gnome-panel
if [ -f %{GTOOL} ] ; then
	export GCONF_CONFIG_SOURCE=`%{GTOOL} --get-default-source`
	%{GTOOL} --direct --config-source=$GCONF_CONFIG_SOURCE --load /usr/share/config/panel-default-setup.SL.entries > /dev/null
	%{GTOOL} --direct --config-source=$GCONF_CONFIG_SOURCE --load /usr/share/config/panel-default-setup.SL.entries /apps/panel > /dev/null
fi


%files
/usr/share/config

%changelog
* Thu Dec 09 2010 Troy Dawson <dawson@fnal.gov> - 6-2
- Changed panel-default-setup.SL.entries to work better with SL6 gnome


