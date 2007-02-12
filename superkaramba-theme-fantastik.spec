%define		theme	fantastik

Summary:	superkaramba - Fantastik theme
Summary(pl.UTF-8):   superkaramba - motyw Fantastik
Name:		superkaramba-theme-%{theme}
Version:	2.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/content/files/17775-fantastik-%{version}.tar.gz
# Source0-md5:	2f76a3cf141e9a31f1cb8114845f51dd
Patch0:		fantastik.theme.patch
URL:		http://www.kde-look.org/content/show.php?content=17775
Requires:	superkaramba
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fantastik theme for superkaramba. Features: 
1) CPU Monitor 
2) MEM Monitor 
3) DISK Monitor 
4) DOWNLOAD/UPLOAD Monitor 
5) MAIL Monitor 
6) Date and uptime 
This theme based on theme by Chip2003 
http://kde-look.org/content/show.php?content=6977 
Screenshot of this theme:

%description -l pl.UTF-8
Motyw Fantastik dla superkaramby. Wyświetlane informacje: 
1) Monitor obciążenia CPU 
2) Monitor wykorzystania pamięci 
3) Monitor wykorzystania dysku 
4) Monitor pobierania/wysyłania interfejsu sieciowego 
5) Monitor poczty pop3
6) Data i uptime
Ten motyw jest bazowanym na motywie zrobionym przez Chip2003
http://kde-look.org/content/show.php?content=6977
Zrzut ekranu tego motywu:

%prep
%setup -q -c
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/fantastik/{image,programs}

install fantastik-%{version}/image/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/fantastik/image
install fantastik-%{version}/programs/*.pl $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/fantastik/programs
install fantastik-%{version}/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/fantastik

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/superkaramba/fantastik
