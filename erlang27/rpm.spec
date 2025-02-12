%define version 27.2.2
%global _disable_source_fetch 0

Name: erlang
Version: %{version}
Release:        %autorelease
Summary: Erlang/OTP 27.2

License: EPL-1.1
URL: https://github.com/erlang/otp
Source0: https://github.com/erlang/otp/releases/download/OTP-%{version}/otp_src_%{version}.tar.gz


BuildRequires: make gcc perl ncurses-devel openssl-devel unixODBC sed wget

%description
Erlang/OTP 27

%prep
%autosetup


%build
ls -al
export ERL_TOP=$(pwd)
%configure --with-ssl-rpath=no
%make_build
make release_tests
%install
%make_install


%check


%files
%license
%doc


%changelog
%autochangelog

