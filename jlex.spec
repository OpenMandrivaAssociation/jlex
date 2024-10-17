# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           jlex
Version:        1.2.6
Release:        14
Summary:        A Lexical Analyzer Generator for Java
License:        BSD
Group:          Development/Java
Source0:        http://www.cs.princeton.edu/~appel/modern/java/JLex/Archive/%{version}/Main.java
Source1:        %{name}-%{version}.build.xml
Patch0:         %{name}-%{version}.static.patch
URL:            https://www.cs.princeton.edu/~appel/modern/java/JLex/

BuildRequires: ant
BuildRequires: java-devel
BuildRequires: jpackage-utils

Requires:      java
Requires:      jpackage-utils

BuildArch:     noarch

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
JLex is a Lexical Analyzer Generator for Java.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -c -T
cp %{SOURCE0} .
%patch0 -p0
cp %{SOURCE1} build.xml

%build
unset CLASSPATH
ant

%install
rm -rf $RPM_BUILD_ROOT

# jar
install -pD -T dist/lib/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre javadoc
# workaround for rpm bug, can be removed in F-17
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%defattr(-,root,root,-)
%{_javadir}/%{name}.jar

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}



%changelog
* Sun Nov 27 2011 Guilherme Moro <guilherme@mandriva.com> 1.2.6-13
+ Revision: 734051
- rebuild
- imported package jlex

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.2.6-4.7mdv2011.0
+ Revision: 619830
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0:1.2.6-4.6mdv2010.0
+ Revision: 425463
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0:1.2.6-4.5mdv2009.0
+ Revision: 140829
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Anssi Hannula <anssi@mandriva.org> 0:1.2.6-4.5mdv2008.1
+ Revision: 120945
- buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Sat Sep 15 2007 Anssi Hannula <anssi@mandriva.org> 0:1.2.6-4.4mdv2008.0
+ Revision: 87437
- rebuild to filter out autorequires of GCJ AOT objects
- remove unnecessary Requires(post) on java-gcj-compat

* Sun Sep 09 2007 Pascal Terjan <pterjan@mandriva.org> 0:1.2.6-4.3mdv2008.0
+ Revision: 82793
- update to new version


* Thu Mar 15 2007 Christiaan Welvaart <spturtle@mandriva.org> 1.2.6-4.2mdv2007.1
+ Revision: 144246
- rebuild for 2007.1
- Import jlex

* Sun Jul 23 2006 David Walluck <walluck@mandriva.org> 0:1.2.6-4.1mdv2007.0
- bump release

* Sun Jun 04 2006 David Walluck <walluck@mandriva.org> 0:1.2.6-2.2mdv2007.0
- rebuild for libgcj.so.7
- aot-compile

* Tue May 10 2005 David Walluck <walluck@mandriva.org> 0:1.2.6-2.1mdk
- release

* Tue Aug 24 2004 Randy Watler <rwatler at finali.com> - 1.2.6-2jpp
- Rebuild with ant-1.6.2

