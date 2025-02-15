%define version 27.2.2
Name: erlang
Version: %{version}
Release:        %autorelease
Summary: Erlang/OTP 27.2

License: EPL-1.1
URL: https://github.com/erlang/otp
Source0: https://github.com/erlang/otp/releases/download/OTP-%{version}/otp_src_%{version}.tar.gz
BuildArch: %{_arch}
BuildRequires: make gcc perl ncurses-devel openssl-devel unixODBC-devel sed wget

%description
Erlang/OTP 27

%prep
wget https://github.com/erlang/otp/releases/download/OTP-%{version}/otp_src_%{version}.tar.gz -o %{_sourcedir}/otp_src_%{version}.tar.gz
cd %{_sourcedir}
tar -xf otp_src_%{version}.tar.gz
%autosetup


%build
mv %{_sourcedir}/otp_src_%{version} otp_src_%{version}
cd otp_src_%{version}
export ERL_TOP=$(pwd)
%configure --with-ssl-rpath=no
%make_build
%install
rm -rf $BUILDROOT
mkdir $BUILDROOT
mkdir -p $BUILDROOT/usr/local/bin
mkdir -p $BUILDROOT/usr/local/lib/erlang
cd otp_src_%{version}
export ERL_TOP=$(pwd)
%make_install

%check

%files
/usr/local/bin/erl
/usr/local/lib/erlang/*
%license
%doc


%changelog
%autochangelog

