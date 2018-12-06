# Run tests in check section
%bcond_without check

# https://github.com/square/go-jose
%global goipath         gopkg.in/square/go-jose.v2
%global forgeurl        https://github.com/square/go-jose
Version:                2.1.9

%global common_description %{expand:
Package jose aims to provide an implementation of the Javascript Object 
Signing and Encryption set of standards. This includes support for JSON Web 
Encryption, JSON Web Signature, and JSON Web Token standards.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        An implementation of JOSE standards (JWE, JWS, JWT) in Go
# Detected licences
# - *No copyright* Apache License (v2.0) at 'LICENSE'
# json/ is BSD
License:        ASL 2.0 and BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/crypto/ed25519)
BuildRequires: golang(golang.org/x/crypto/pbkdf2)
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(gopkg.in/alecthomas/kingpin.v2)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup

mv json/LICENSE LICENSE-json


%build 
%gobuildroot
%gobuild -o _bin/jose-util %{goipath}/jose-util
%gobuild -o _bin/jwk-keygen %{goipath}/jwk-keygen


%install
%goinstall -t jose-util -t jwk-keygen
install -Dpm 0755 _bin/jose-util %{buildroot}%{_bindir}/jose-util
install -Dpm 0755 _bin/jwk-keygen %{buildroot}%{_bindir}/jwk-keygen


%if %{with check}
%check
%gochecks
%endif


%files
%license LICENSE LICENSE-json
%{_bindir}/jose-util
%{_bindir}/jwk-keygen


%files devel -f devel.file-list
%license LICENSE LICENSE-json
%doc README.md CONTRIBUTING.md BUG-BOUNTY.md


%changelog
* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.9-1
- First package for Fedora

