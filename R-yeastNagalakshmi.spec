%global packname  yeastNagalakshmi
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.99.3
Release:          1
Summary:          Yeast genome RNA sequencing data based on Nagalakshmi et. al
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              None
Source0:          http://bioconductor.org/packages/data/experiment/src/contrib/yeastNagalakshmi_0.99.3.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
The yeast genome data was retrieved from the sequence read archive,
aligned with bwa, and converted to BAM format with samtools.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
