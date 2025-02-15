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
ls -al %{_sourcedir}
cd %{_sourcedir}
tar -xf otp_src_%{version}.tar.gz
mv otp_src_%{version} erlang-%{version}


%build
ls -al
cd erlang-%{version}
export ERL_TOP=$(pwd)
%configure --with-ssl-rpath=no
%make_build
%install
echo %{buildroot}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/lib64/erlang
cd otp_src_%{version}
export ERL_TOP=$(pwd)
export DESTDIR=%{buildroot}
make install

%files
/usr/bin/ct_run
/usr/bin/dialyzer
/usr/bin/epmd
/usr/bin/erl
/usr/bin/erlc
/usr/bin/escript
/usr/bin/run_erl
/usr/bin/to_erl
/usr/bin/typer
/usr/lib64/erlang/*
%license
%doc


%changelog
* Sat Feb 15 2025 Philip Bove <phil@bove.online> 27.2.2-1
- new package built with tito

%autochangelog

