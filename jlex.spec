%define name            jlex
%define version         1.2.6
%define release         4.4
%define section		free
%define gcj_support	1

Name:           %{name}
Version:        %{version}
Release:        %mkrel %{release}
Epoch:		0
Summary:        A Lexical Analyzer Generator for Java
License:        BSD-style
Group:          Development/Java
#Vendor:         JPackage Project
#Distribution:   JPackage
Source0:        http://www.cs.princeton.edu/~appel/modern/java/JLex/Archive/1.2.5/Main.java
Source1:        %{name}-%{version}.build.xml
Patch0:         %{name}-%{version}.static.patch
URL:            http://www.cs.princeton.edu/~appel/modern/java/JLex/
BuildRequires:  ant
BuildRequires:  jpackage-utils > 0:1.5
BuildRequires:  sed
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
JLex is a Lexical Analyzer Generator for Java.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c -T
cp %{SOURCE0} .
%patch0 -p0
cp %{SOURCE1} build.xml

%build
%ant

%install
# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -r dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{gcj_support}
%post
%{update_gcjdb}

%postun
%{clean_gcjdb}
%endif

%files
%defattr(-,root,root,-)
%{_javadir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}-%{version}


