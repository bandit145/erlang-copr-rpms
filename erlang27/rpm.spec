Name: erlang
Version: 27.2.2
Release:        %autorelease
Summary: Erlang/OTP 27.2

License: EPL-1.1
URL: https://github.com/erlang/otp 
Source0: https://github.com/erlang/otp/releases/download/OTP-${version}/otp_src_${version}.tar.gz

BuildRequires: make gcc perl ncurses-devel openssl-devel unixODBC sed

%description
Erlang/OTP 27

%prep
%autosetup


%build
cd otp_src_${version}
export ERL_TOP=$(pwd)
make release_tests
make install
%configure --with-ssl-rpath=no
%make_build
make release_tests
%insall
%make_install


%check


%files
%license
%doc


%changelog
%autochangelog

