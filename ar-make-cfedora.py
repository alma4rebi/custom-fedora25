#!/usr/bin/python3
import os
import subprocess
import sys
import time

def selinux_():
    check = subprocess.check_output("getenforce",shell=True).decode("utf-8").strip()
    if check == "Enforcing":
        if check != "Disabled":
            subprocess.call("sudo setenforce 0",shell=True)
        
def init_check():
    if os.getuid()==0:
        sys.exit("Run Script Without Root Permissions.") 

    if not sys.version.startswith("3"):
        sys.exit("Use Python 3 Try run python3 ar-make-cfedora.py")
init_check()
selinux_()

login_name = os.environ["LOGNAME"]
home = "/home/"+login_name
dirname = os.path.abspath(os.path.dirname(__file__))
fedora_version = "25"

desktop_dict = {
    "1" : "Gnome Shell." ,
    "2" : "Kde Plasma."
}

kickstart_files = {
    "Gnome Shell." : "%s/fedora-live-workstation.ks"%dirname ,
    "Kde Plasma."  : "%s/fedora-live-kde.ks"%dirname

}

desktop_iso_name = {
    "Gnome Shell." : "workstation" ,
    "Kde Plasma."  : "kde"

}


name = "generic"
code_name = ""
desktop = ""
website = "www.arfedora.blogspot.com"
version = ""
#icon_theme = ""
#cursor_icon_theme = ""
#theme = ""
local_repo = r"repo  --cost=1 --name=localrepo --baseurl=file://%s/repo"%dirname

def choice_name(msg=""):
    global name
    while True:
        subprocess.call("clear")
        print ("www.arfedora.blogspot.com\n")
        if len(msg) != 0:
            print (msg+"\n")
        answer = input("Choice Distor Name || q to quit :\n-").strip()
        if answer == "q" or answer == "Q":
            sys.exit("\nBye...\n")
        elif answer.isalpha():
            if len(answer)>10:
                return choice_name("Enter Name < 10 characters.")
            elif answer=="fedora":
                choice_name("Cant choice fedora.")
            name = answer
            break
        else:
            return choice_name("Enter Name without Number Space or symbol.")
    return choice_code_name()

def choice_code_name(msg=""):
    global code_name
    while True:
        subprocess.call("clear")
        print ("www.arfedora.blogspot.com\n")
        if len(msg) != 0:
            print (msg+"\n")
        answer = input("Choice Distor Code  Name || q to quit :\n-").strip()
        if answer == "q" or answer == "Q":
            sys.exit("\nBye...\n")

        elif answer == "b" or answer == "B":
            return choice_name()

        elif len(answer)<12:
            code_name = answer
            break
        else:
            return choice_code_name("Enter Code Name < 12 characters.")
    return choice_version_number()


def choice_version_number(msg=""):
    global version
    while True:
        subprocess.call("clear")
        print ("www.arfedora.blogspot.com\n")
        if len(msg) != 0:
            print (msg+"\n")
        answer = input("Choice Distor Version NUmber || q to quit :\n-").strip()
        answer.replace(" ","")
        if answer == "q" or answer == "Q":
            sys.exit("\nBye...\n")

        elif answer == "b" or answer == "B":
            return choice_code_name()

        elif len(answer)>=3 and not answer.isalpha():
            version = answer
            break
        else:
            return choice_version_number("Enter Number Example: 1.0 ")
    return choice_desktop()


def choice_desktop(msg=""):
    global name
    global desktop_dict
    global desktop
    while True:
        subprocess.call("clear")
        print ("www.arfedora.blogspot.com\n")
        if len(msg) != 0:
            print (msg+"\n")
        for v,k in  desktop_dict.items():
            print ("%s-%s\n"%(v,k))
        answer = input("Choice Desktop || q to quit || b to back :\n-").strip()
        if answer == "q" or answer == "Q":
            sys.exit("\nBye...\n")
        elif answer == "b" or answer == "B":
            return choice_version_number()
        elif answer in desktop_dict.keys():
            desktop = desktop_dict[answer]
            break
        else:
            return choice_desktop("Enter Number To Choice Desktop.")

    return choice_wesite()

def choice_wesite(msg=""):
    global website
    while True:
        subprocess.call("clear")
        print ("www.arfedora.blogspot.com\n")
        if len(msg) != 0:
            print (msg+"\n")
        answer = input("Your Website Example:<http://arfedora.blogspot.com> || q to quit || b to back :\n-").strip()
        if answer == "q" or answer == "Q":
            sys.exit("\nBye...\n")
        elif answer == "b" or answer == "B":
            return choice_desktop()
        elif answer.startswith("http"):
            website = answer
            break

choice_name()

"""
def get_all_desktop_themes():
    global dirname
    result = []
    for l in os.listdir(dirname+"/desktop_themes"):
        for f in os.listdir(l):
            if f == "index.theme":
                result.append(l)
    return result
all_desktop_themes = get_all_desktop_themes()


def get_all_icon_themes():
    global dirname
    result = []
    for l in os.listdir(dirname+"/icons_themes"):
        for f in os.listdir(l):
            if f == "index.theme":
                result.append(l)
    return result
 
all_icons_themes = get_all_icon_themes()


def get_all_cursor_icons_themes():
    global dirname
    result = []
    for l in os.listdir(dirname+"/cursor_icons_themes"):
        for f in os.listdir(l):
            if f == "index.theme":
                 result.append(l)
    return result
all_cursor_icons_themes = get_all_cursor_icons_themes()
"""


release_file = """%global release_name {0}
%global dist_version {1}

Summary:        {2} release files
Name:           {3}-release
Version:        {4}
Release:        1
License:        MIT
Group:	        System Environment/Base
URL:            {5}
Source0:        LICENSE
Source1:        README.developers
Source2:        README.{6}-Release-Notes
Source3:        README.license
Source4:        85-display-manager.preset
Source5:        90-default.preset
Source6:        99-default-disable.preset
Source7:        copr.conf
Obsoletes:      redhat-release
Provides:       redhat-release
Provides:       system-release
Provides:       system-release(%{{version}})
# Comment this next Requires out if we're building for a non-rawhide target
#Requires:       fedora-repos-rawhide
Requires:       fedora-repos(%{{version}})
Obsoletes:      generic-release-rawhide <= 21-5
Obsoletes:      generic-release
Obsoletes:      generic-release-cloud <= 23-0.4
Obsoletes:      generic-release-server <= 23-0.4
Obsoletes:      generic-release-workstation <= 23-0.4
BuildArch:      noarch
Conflicts:      fedora-release
Conflicts:      generic-release

%description
{7} release files such as yum configs and various /etc/ files that
define the release. This package explicitly is a replacement for the 
trademarked release package, if you are unable for any reason to abide by the 
trademark restrictions on that release package.

%package notes
Summary:	Release Notes
License:	Open Publication
Group:		System Environment/Base
Provides:	system-release-notes = %{{version}}-%{{release}}
Conflicts:	fedora-release-notes
Conflicts:	generic-release-notes

%description notes
{8} release notes package. This package explicitly is a replacement 
for the trademarked release-notes package, if you are unable for any reason
to abide by the trademark restrictions on that release-notes 
package. Please note that there is no actual useful content here.

%prep
%setup -c -T
cp -a %{{SOURCE0}} %{{SOURCE1}} %{{SOURCE2}} %{{SOURCE3}} %{{SOURCE4}} %{{SOURCE5}} %{{SOURCE6}} .

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/etc/dnf/plugins
install -m 644 %{{SOURCE7}} $RPM_BUILD_ROOT/etc/dnf/plugins
install -d %{{buildroot}}/etc
echo "{9} release %{{version}} (%{{release_name}})" > %{{buildroot}}/etc/fedora-release
echo "cpe:/o:{10}:{11}:{12}" > %{{buildroot}}/etc/system-release-cpe
cp -p %{{buildroot}}/etc/fedora-release %{{buildroot}}/etc/issue
echo "Kernel \r on an \m (\l)" >> %{{buildroot}}/etc/issue
cp -p %{{buildroot}}/etc/issue %{{buildroot}}/etc/issue.net
echo >> %{{buildroot}}/etc/issue
ln -s fedora-release %{{buildroot}}/etc/redhat-release
ln -s fedora-release %{{buildroot}}/etc/system-release

mkdir -p %{{buildroot}}/usr/lib/systemd/system-preset/

cat << EOF >>%{{buildroot}}/usr/lib/os-release
NAME={13}
VERSION="%{{dist_version}} (%{{release_name}})"
ID=fedora
VERSION_ID=%{{version}}
PRETTY_NAME="{14} %{{dist_version}} (%{{release_name}})"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:{15}:{16}:%{{dist_version}}"
HOME_URL="{17}"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=25
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=25
PRIVACY_POLICY_URL=https://fedoraproject.org/wiki/Legal:PrivacyPolicy
EOF

# Create the symlink for /etc/os-release
ln -s ../usr/lib/os-release %{{buildroot}}/etc/os-release

# Set up the dist tag macros
install -d -m 755 %{{buildroot}}%{{_rpmconfigdir}}/macros.d
cat >> %{{buildroot}}%{{_rpmconfigdir}}/macros.d/macros.dist << EOF
# dist macros.

%%fedora		%{{version}}
%%dist		.fc%{{version}}
%%fc%{{version}}		1
EOF

# Add presets
# Default system wide
install -m 0644 85-display-manager.preset %{{buildroot}}%{{_prefix}}/lib/systemd/system-preset/
install -m 0644 90-default.preset %{{buildroot}}%{{_prefix}}/lib/systemd/system-preset/
install -m 0644 99-default-disable.preset %{{buildroot}}%{{_prefix}}/lib/systemd/system-preset/

%clean
rm -rf %{{buildroot}}

%files
%defattr(-,root,root,-)
%license LICENSE README.license
%config %attr(0644,root,root) /usr/lib/os-release
/etc/os-release
%config %attr(0644,root,root) /etc/fedora-release
/etc/redhat-release
/etc/system-release
%config %attr(0644,root,root) /etc/system-release-cpe
%config(noreplace) %attr(0644,root,root) /etc/issue
%config(noreplace) %attr(0644,root,root) /etc/issue.net
%attr(0644,root,root) %{{_rpmconfigdir}}/macros.d/macros.dist
%{{_prefix}}/lib/systemd/system-preset/85-display-manager.preset
%{{_prefix}}/lib/systemd/system-preset/90-default.preset
%{{_prefix}}/lib/systemd/system-preset/99-default-disable.preset
%config  /etc/dnf/plugins/copr.conf

%files notes
%defattr(-,root,root,-)
%doc README.{18}-Release-Notes

%changelog
* Tue Apr 18 2017 youcef sourani <yousse.m.sourani@gmail.com> - 25-1
- Update To {19}-release
""".format(code_name , version   ,name.title()  , name , fedora_version , website,name.title() , name.title()   ,name.title() , name.title() , name , name ,version  ,name ,name ,name ,name ,website  ,name.title() ,name )

#.format(code_name 0, version 1  ,name.title() 2 , name 3, fedora_version 4,name.title() 5, name.title() 6  ,name.title() 7, name.title() 8, name 9, name 10,version 11 ,name 12,name 13,name 14,name 15,website 16 ,name.title() 17,name 18)



readme_file="""README.{}-Release-Notes
=============================

This is a placeholder. There are no useful release notes in here.

Sorry bout that.""".format(name.title())


copr = """[main]
distribution=Fedora
releasever=%s"""%fedora_version


def install_tools():
    check = subprocess.call("sudo dnf install @rpm-development-tools livecd-tools createrepo_c -y --best  --disablerepo=* --enablerepo=fedora",shell=True)
    if check != 0:
        sys.exit("Error Check Your Connection.")
    subprocess.call("rpmdev-setuptree",shell=True)


def download_extract_generic():
    global name
    global release_file
    global dirname
    global readme_file
    #check = subprocess.call("dnf download --source  generic-release -y  --disablerepo=* --enablerepo=fedora",shell=True)
    #if check != 0:
        #sys.exit("Error Check Your Connection.")
    
    release_folder_location = dirname+"/release_files"
    original_release_folder_location = dirname+"/original_release_files"
    subprocess.call("rm -r %s/*"%release_folder_location,shell=True)
    subprocess.call("cp -r %s/* %s"%(original_release_folder_location,release_folder_location),shell=True)
    #os.chdir(release_folder_location)
    #subprocess.call("rpm2cpio %s/generic-release* | cpio -idmv"%dirname,shell=True)
    
    subprocess.call("mv {}/README.Generic-Release-Notes {}/README.{}-Release-Notes".format(release_folder_location,release_folder_location,name.title()),shell=True)
    subprocess.call("mv {}/generic-release.spec {}/{}-release.spec".format(release_folder_location,release_folder_location,name),shell=True)
    with open (release_folder_location+"/%s-release.spec"%name,"w") as mm:
        mm.write(release_file)

    with open (release_folder_location+"/README.%s-Release-Notes"%name.title(),"w") as mm:
        mm.write(readme_file)

    with open (release_folder_location+"/copr.conf","w") as mm:
        mm.write(copr)
        
    #os.chdir(dirname)

    





def make_release_package():
    global name
    global home
    global dirname
    release_location = dirname+"/release_files"
    for i in os.listdir(release_location):
        if i.endswith(".spec"):
            subprocess.call("cp -r %s/%s %s/rpmbuild/SPECS"%(release_location ,i ,home),shell=True)
        else:
            subprocess.call("cp -r %s/%s %s/rpmbuild/SOURCES"%(release_location ,i ,home),shell=True)
    
    os.chdir("%s/rpmbuild/SPECS"%home)
    subprocess.call("rpmbuild -ba %s-release.spec"%name,shell=True)
    os.chdir(dirname)


def make_iso():
    global kickstart_files
    global dirname
    global login_name
    global desktop
    global desktop_iso_name
    time_now = time.strftime("%m%d%H%M", time.gmtime())
    check = subprocess.call("sudo livecd-creator --config=%s --verbose --fslabel=%s-%s-%s --cache=%s/arfedoracache/live --tmpdir=%s/tmp"%(kickstart_files[desktop] ,name , desktop_iso_name[desktop], time_now, dirname,dirname),shell=True)
    if check != 0:
        sys.exit("Error Check Your Connection.")
    iso_files= (lambda location,char: [f for f in os.listdir(location) if f.endswith(char)])(dirname,".iso")
    if len(iso_files) != 0:
        for iso in iso_files:
            subprocess.call("sudo chown %s:%s %s"%(login_name, login_name, dirname+"/"+iso),shell=True)

def make_local_repo():
    global name
    global home
    global dirname
    global local_repo
    subprocess.call("cp %s/rpmbuild/RPMS/noarch/%s-release*.rpm %s/repo"%(home ,name ,dirname),shell=True)
    subprocess.call("cp %s/rpmbuild/RPMS/noarch/%s-release-notes*.rpm %s/repo"%(home ,name ,dirname),shell=True)
    subprocess.call("createrepo_c  %s/repo"%dirname,shell=True)
    with open(dirname+"/local_repo.ks","w") as myfile:
        myfile.write(local_repo)

def make_ks_file():
    global name
    global dirname
    to_write=r"""
%packages
{}-release
{}-release-notes
%end
""".format(name,name)
    with open(dirname+"/custom_release.ks","w") as myfile:
        myfile.write(to_write)

def firefox():
    global name
    global dirname
    global website
    os.makedirs(dirname+"/mozilla/firefox/%s.default"%name,exist_ok=True)
    profile = """[General]
StartWithLastProfile=0

[Profile0]
Name=default
IsRelative=1
Path=%s.default
"""%name

    prefs = """user_pref("browser.startup.homepage", "%s");"""%website

    ks_file = """%post --nochroot
/usr/bin/mkdir -p $INSTALL_ROOT/etc/skel/.mozilla/firefox/{}.default
/usr/bin/cp mozilla/firefox/profiles.ini $INSTALL_ROOT/etc/skel/.mozilla/firefox/
/usr/bin/cp mozilla/firefox/{}.default/prefs.js $INSTALL_ROOT/etc/skel/.mozilla/firefox/{}.default

%end
""".format(name,name,name)

    with open(dirname+"/mozilla/firefox/profiles.ini","w") as myfile:
        myfile.write(profile)


    with open(dirname+"/mozilla/firefox/%s.default/prefs.js"%name,"w") as myfile:
        myfile.write(prefs)

    with open("firefox.ks","w") as myfile:
        myfile.write(ks_file)




install_tools()
download_extract_generic()
make_release_package()
make_local_repo()
make_ks_file()
firefox()
make_iso()

print ("\nFinish.\n")

