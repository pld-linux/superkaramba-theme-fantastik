%define		theme	fantastik

Summary:	superkaramba - Fantastik theme
Summary(pl):	superkaramba - motyw Fantastik
Name:		superkaramba-theme-%{theme}
Version:	1.4
Release:	0.1
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/content/files/17775-fantastik-%{version}.tar.gz
Patch0:		fantastik.theme.patch
# Source0-md5:	91d98821158d6b51b18c043017f32b11
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
http://www.kde-look.org/content/preview.php?preview=1&id=17775&file1=17775-1.png&file2=&file3=&name=fantastik

%description -l pl
Motyw Fantastik dla superkaramby. Wy¶wietlane informacje: 
1) Monitor obci±¿enia CPU 
2) Monitor wykorzystania pamiêci 
3) Monitor wykorzystania dysku 
4) Monitor pobierania/wysy³ania interfejsu sieciowego 
5) Monitor poczty pop3 6) Data i uptime
Ten motyw jest bazowanym na motywie zrobionym przez Chip2003
http://kde-look.org/content/show.php?content=6977
Zrzut ekranu tego motywu:
http://www.kde-look.org/content/preview.php?preview=1&id=17775&file1=17775-1.png&file2=&file3=&name=fantastik

%prep
%setup -q -c
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/fantastik
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/fantastik/image/
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/fantastik/programs/
install fantastik-%{version}/image/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/fantastik/image
install fantastik-%{version}/programs/*.pl $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/fantastik/programs
install fantastik-%{version}/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/fantastik

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/themes/superkaramba/fantastik
%dir %{_datadir}/themes/superkaramba/fantastik/image/
%{_datadir}/themes/superkaramba/fantastik/image/*.png
%{_datadir}/themes/superkaramba/fantastik/*.theme
%{_datadir}/themes/superkaramba/fantastik/programs/*.pl
