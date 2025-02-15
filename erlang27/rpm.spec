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
wget https://github.com/erlang/otp/releases/download/OTP-%{version}/otp_src_%{version}.tar.gz -O %{_sourcedir}/otp_src_%{version}.tar.gz
cd %{_sourcedir}
tar -xf otp_src_%{version}.tar.gz
%autosetup


%build
mv %{_sourcedir}/otp_src_%{version} otp_src_%{version}
cd otp_src_%{version}
export ERL_TOP=$(pwd)
./configure --with-ssl-rpath=no --prefix=%{buildroot}/usr/local
%make_build
%install
echo %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/local/lib64/erlang
cd otp_src_%{version}
export ERL_TOP=$(pwd)
make install

%files
/usr/local/bin/ct_run
/usr/local/bin/dialyzer
/usr/local/bin/epmd
/usr/local/bin/erl
/usr/local/bin/erlc
/usr/local/bin/escript
/usr/local/bin/run_erl
/usr/local/bin/to_erl
/usr/local/bin/typer
/usr/local/lib64/erlang/*
%license
%doc


%changelog
%autochangelog

