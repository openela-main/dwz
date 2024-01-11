Summary: DWARF optimization and duplicate removal tool
Name: dwz
Version: 0.12
Release: 10%{?dist}
License: GPLv2+ and GPLv3+
Group: Development/Tools
# git archive --format=tar --remote=git://sourceware.org/git/dwz.git \
#   --prefix=%%{name}-%%{version}/ %%{name}-%%{version} \
#   | bzip2 -9 > %%{name}-%%{version}.tar.bz2
Source: %{name}-%{version}.tar.bz2
BuildRequires: gcc, elfutils-libelf-devel

Patch1: dwz-rh1949185.patch

%description
The dwz package contains a program that attempts to optimize DWARF
debugging information contained in ELF shared libraries and ELF executables
for size, by replacing DWARF information representation with equivalent
smaller representation where possible and by reducing the amount of
duplication using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information
and using DW_TAG_imported_unit to import it into each CU that needs it.

%prep
%setup -q
%patch1 -p1 -b .rh1949185~

%build
make %{?_smp_mflags} CFLAGS='%{optflags}' LDFLAGS='%{build_ldflags}' \
  prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir} \
  install

%files
%license COPYING COPYING3 COPYING.RUNTIME
%{_bindir}/dwz
%{_mandir}/man1/dwz.1*

%changelog
* Wed May  5 2021 Marek Polacek <polacek@redhat.com> 0.12-10
- handle intra-CU DW_FORM_ref_addr reference (#1949185)

* Tue Aug  7 2018 Marek Polacek <polacek@redhat.com> 0.12-9
- don't use arched BuildRequires (#1545773)
- remove %defattr

* Fri Feb 23 2018 Florian Weimer <fweimer@redhat.com> - 0.12-7
- Use LDFLAGS from redhat-rpm-config

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 01 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.12-3
- Add missing %%license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Jakub Jelinek <jakub@redhat.com> 0.12-1
- fix up alignment of moved non-allocated sections and section header table

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.11-5
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  2 2013 Jakub Jelinek <jakub@redhat.com> 0.11-1
- handle .gdb_index version 8 (#969454)

* Mon Mar 11 2013 Jakub Jelinek <jakub@redhat.com> 0.10-1
- when creating DW_AT_stmt_list, use DW_FORM_sec_offset for dwarf4
  and DW_FORM_data4 for dwarf[23] rather than vice versa (#919755)

* Mon Feb  4 2013 Jakub Jelinek <jakub@redhat.com> 0.9-1
- fix up handling of DIE equality if more than one DIE in the same
  CU compare equal (#889283)
- check DW_FORM_ref_addr properly during fi_multifile phase

* Thu Nov 29 2012 Jakub Jelinek <jakub@redhat.com> 0.8-1
- fix recompute_abbrevs (#880634)
- optimize DW_FORM_data[48] DW_AT_high_pc that GCC 4.8 produces

* Fri Aug 10 2012 Jakub Jelinek <jakub@redhat.com> 0.7-1
- fix iterative hasing on big-endian targets (#846685)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Jakub Jelinek <jakub@redhat.com> 0.6-1
- add --version/-v option support (Matt Newsome)
- fix building on RHEL 5

* Wed Jul  4 2012 Jakub Jelinek <jakub@redhat.com> 0.5-1
- handle .gdb_index version 7

* Fri Jun 22 2012 Jakub Jelinek <jakub@redhat.com> 0.4-1
- fix up DIE counting in low-mem mode for testing the -L limit

* Fri Jun 15 2012 Jakub Jelinek <jakub@redhat.com> 0.3-1
- update to dwz-0.3 (#830863)

* Mon Jun 11 2012 Jakub Jelinek <jakub@redhat.com> 0.2-1
- new package
