Name:           {{{ git_dir_name }}}
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        This is a test package.

License:        GPLv2+
URL:            https://github.com/trabucayre/openFPGALoader
VCS:            {{{ git_dir_vcs }}}

Source:         {{{ git_dir_pack }}}

Requires:       libftdi libgudev
BuildRequires:  libftdi-devel libgudev-devel cmake gcc-c++

%description
Universal utility for programming FPGA

%global debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
cmake --build .

%install
cd build
make install DESTDIR=%{buildroot}

%files
/usr/bin/openFPGALoader
/usr/share/openFPGALoader/test_sfl.svf
/usr/share/openFPGALoader/spiOverJtag_xc7a35.bit

%changelog
{{{ git_dir_changelog }}}
