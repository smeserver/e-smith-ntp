Summary: e-smith specific NTP configuration files and templates
%define name e-smith-ntp
Name: %{name}
%define version 1.16.0
%define release 11
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-ntp-1.16.0-success.patch
Patch1: e-smith-ntp/P/e-smith-ntp-1.16.0-hwsync.patch
Patch2: e-smith-ntp-1.16.0-memlimit.patch
Patch3: e-smith-ntp-1.16.0-ChangeInitialtoFirstDateTimePanel.patch
Patch4: e-smith-ntp-1.16.0-smeserver.pool.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: e-smith-devtools >= 1.13.1-03
Requires: e-smith-base
Requires: ntp
Requires: e-smith-lib >= 1.15.1-19
AutoReqProv: no

%changelog
* Sun Jul 08 2007 Stephen Noble <support@dungog.net> 1.16.0-11
- Change default to smeserver.pool.ntp.org [SME: 1426]
 
* Tue Jun 26 2007 Gavin Weight <gweight@gmail.com> 1.16.0-10
- Change Initial to First in the Datetime panel. [SME: 3108]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Mon Jan 22 2007 Shad L. Lords <slords@mail.com> 1.16.0-9
- Up memory limit to remove out of memory errors [SME: 2241]

* Tue Jan 16 2007 Shad L. Lords <slords@mail.com> 1.16.0-8
- Rework hwclock sync patch to function properly. [SME: 1954]

* Tue Jan 16 2007 Shad L. Lords <slords@mail.com> 1.16.0-7
- Remove HWClockSupport needs rework. [SME: 1954]
- Rework success patch needs delay before signal-event [SME: 2292]

* Sun Jan 14 2007 Shad L. Lords <slords@mail.com> 1.16.0-6
- Fix migrate fragment [SME: 1954]

* Sat Jan 13 2007 Shad L. Lords <slords@mail.com> 1.16.0-5
- Make success/failure messages standard [SME: 2292]

* Tue Jan  2 2007 Charlie Brady <charlie_brady@mitel.com> 1.16.0-4
- Add patch from Zac Sprackett to support sync to HW clock. [SME: 1954]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Sat Dec 02 2006 Shad L. Lords <slords@mail.com> 1.16.0-02
- Bump version so it gets installed on upgrade and forces ntp to be installed.

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.16.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.15.2-02
- Bump release number only

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.15.2-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.15.1-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.15.0-14]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.15.0-13]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Wed Aug 31 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-12]
- Enforce minimum value of content of env/MEMLIMIT file. [SF: 1270649]

* Tue Aug 23 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-11]
- Fix update of /etc/localtime symlink after update via panel. [SF: 1264801]

* Wed Aug 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-10]
- Remove /etc/ntp.conf in %pre script, to work around
  problems with update of ntpd RPM. Add conditional expand-template
  to run script to be sure that file is regenerated before we need 
  it. [SF: 1237968]

* Fri Aug 12 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-09]
- Open config db r/w to allow property update. [SF: 1216546]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-08]
- Update to current db access APIs. [SF: 1216546]

* Thu Jun 23 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-07]
- Increase MemLimit setting to 6MB (for CentOS4 build). [SF: 1225925]
- Remove obsolete "authenticate" directive from ntpd.conf. [SF: 1225925]

* Thu Jun 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-06]
- Ensure that 'status' property is recognised at startup. [MN00061795]

* Thu Mar 31 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-05]
- Add default fragment for MemLimit property of ntp service.
  [MN00064130]

* Thu Mar 31 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-04]
- Remove explicity call of generic_template_expand - it's now
  implicit. [MN00064130]

* Tue Mar  8 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-03]
- Fix template expansion of /etc/ntp/step-tickers and ./env/MEMLIMIT
  [MN00064130]
- Use generic service adjust action for reload/restart. [MN00065576]

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-02]
- Combine set-date and set-clock, and use a shell script rather than
  perl. [MN00064941]
- Use generic_template_expand action where possible, in place
  of specific actions. Update e-smith-lib dependency. [MN00064130]

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-01]
- Changing version to development stream number - 1.15.0

* Thu Nov 11 2004 Michael Soulier <msoulier@e-smith.com>
- [1.14.0-02]
- Patched stderr "leaking" from ntpdate call. [msoulier MN00056927]

* Wed Nov  3 2004 Charlie Brady <charlieb@e-smith.com>
- [1.14.0-01]
- Changing version to stable stream number - 1.14.0

* Tue Oct 19 2004 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-21]
- pool.ntp.org now uses 0, 1, 2 prefixes rather than relying on
  short DNS TTLs. So, we need to add the prefixes if we are talking
  with pool.ntp.org or {region}.pool.ntp.org and revert to listing 
  "normal" NTP servers once [gordonr MN00053174]

* Mon Oct 18 2004 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-20]
- List the ntp server three times, for DNS round-robin servers, 
  such as pool.ntp.org, {region}.pool.ntp.org and time.nrc.ca
- [gordonr MN00053174]

* Tue Sep 28 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-19]
- Convert ntp.conf/10localhost template fragment from DOS text format
  [charlieb MN00050805]

* Tue Sep 28 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-18]
- Convert ntp.conf/30other template fragment from DOS text format
  [charlieb MN00050805]
- Don't create pid file, and remove one if we find an old one.
  [charlieb MN00050806]
- ntpdate should log to standard output, not to syslog. [charlieb MN00049205]

* Tue Sep 28 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-17]
- Need to create empty /service/ntpd/env directory for template to be
  expanded into.  [charlieb MN00050192]

* Tue Sep 28 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-16]
- Increase memory limit for running ntpd. While we are at it,
  we'll make the value templated, and update code in conf-ntpd 
  to modern standards.  [charlieb MN00050192]

* Tue Sep 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-15]
- Fixed logging to go to stdout. [msoulier MN00049205]

* Fri Sep  3 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-14]
- Clean BuildRequires. [charlieb MN00043055]

* Wed May  5 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-13]
- Fixed a logic error from last change. [msoulier MN00027900]

* Wed May  5 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-12]
- Added localhost as a stratum 10 server. [msoulier MN00027900]

* Wed Jan 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-11]
- Added ntpdate call to run script. [msoulier 10929]

* Thu Jan 22 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-10]
- Raised the softlimit for ntpd. libc is big. :) [msoulier 10929]

* Thu Jan 22 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-09]
- Moved proxy-start/stop to e-smith-proxy where they belong. [msoulier 10929]

* Thu Jan 22 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-08]
- Fixed missing directives to genfilelist. [msoulier 10586]

* Thu Jan 22 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-07]
- Fixed a typo in createlinks. The new ntpd initscript must not conflict with
  the one in the ntpd package. [msoulier 10586]

* Wed Jan 21 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-06]
- Removing old symlink creation and moving to createlinks. [msoulier 10586]

* Wed Jan 21 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-05]
- Adding supervision of ntpd. [msoulier 10586]

* Fri Nov  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-04]
- Enable ntpd by default [gordonr 10566]

* Fri Nov  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-03]
- Default time server to pool.ntp.org [gordonr 10566]

* Tue Jul 22 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-02]
- Remove deprecated -startup script, and add default db
  fragments [charlieb 9553]
- s/Copyright/License/

* Tue Jul  8 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-01]
- Changing version to development stream number - 1.13.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.12.0-01]
- Changing version to stable stream number - 1.12.0

* Fri May  9 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-22]
- Fix save button justification [tonyc 1588]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-21]
- Add Spanish lexicon for datetime panel [lijied 3793]

* Thu May  1 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-20]
- Background the timeserver-update event in panel [tonyc 1588]

* Wed Apr 30 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-19]
- Fix datetime panel when ntp stays disabled [tonyc 1588]
- Show date when ntp is enabled [tonyc 1588]

* Thu Apr 17 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.11.0-18]
- Start ntp after external network is (possibly) up [gordonr 8391]

* Thu Apr 10 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-17]
- Change $q->table back [lijied 8034]

* Wed Apr  9 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-16]
- Added French trans for "Set Date and Time" [lijied 7949]

* Fri Apr  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-15]
- Changed $q->table to $->start_table where necessary [lijied 8034]

* Thu Apr  3 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-14]
- Removed en-us and fr 'Mitel Networks SME Server' branding [lijied 8016]

* Tue Apr  1 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-13]
- Fix datetime to loop back to Initial page w/ status report [tonyc 1588]
- Fix link to Verify page [tonyc 1588]

* Tue Apr  1 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-12]
- Add container table to fix IE 6 handling of table-layout: fixed [tonyc 1588]
- Remove redundant newlines from some print statements [tonyc 1588]

* Fri Mar 28 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-11]
- Update fr l10n strings [tonyc 1588]

* Thu Mar 27 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-10]
- Major refactoring and cleanup of datetime.pm [tonyc 1588]
- Expand tabs to spaces in datetime.pm [tonyc 1588]
- Add radio buttons and don't allow setting date manually when ntp is enabled
  [tonyc 1588]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787]

* Mon Mar 17 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-09]
- Deleted inappropriate template-begin file
  deleted empty template-end files [lijied 3295]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-08]
- Modified datetime panel order [lijied 7356]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-07]
- Split en-us lexicon from datetime panel [lijied 4030]

* Mon Mar  3 2003 Lijie Deng <lijied@e-smith.com>
- [1.11.0-06]
- Add French lexicon for datetime [lijied 5003]

* Thu Jan 16 2003 Mark Knox <markk@e-smith.com>
- [1.11.0-05]
- Use new gen_locale_date_string routine [markk 3357]

* Fri Dec 27 2002 Mike Dickson <miked@e-smith.com>
- [1.11.0-04]
- updated the datetime panel to use css [miked 5494]

* Tue Dec 10 2002 Mike Dickson <miked@e-smith.com>
- [1.11.0-03]
- ui update  [miked 5494]

* Thu Nov 21 2002 Mike Dickson <miked@e-smith.com>
- [1.11.0-02]
- update to new UI system [miked 5494]

* Wed Nov 20 2002 Mike Dickson <miked@e-smith.com>
- [1.11.0-01]
- Changing to development stream; version upped to 1.11.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Rolling stable version number to 1.10.0

* Fri Aug 23 2002 Mark Knox <markk@e-smith.com>
- [1.9.4-01]
- Fixed duplicate English-only footers in panel [markk 3615]

* Mon Aug 19 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.3-01]
- Remove masq script update and restart symlinks. They are no longer
  needed not that we have connection tracking enabled. [charlieb 4501]
- Add rc7.d symlink, and don't set obsolete InitscriptsOrder property
  [charlieb 4458]

* Thu Aug  8 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.2-01]
- Remove NTP masq template fragment. We no longer need it, as netfilter
  connection tracking allows NTP replies. [charlieb 4499]

* Wed Jul 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.1-01]
- Change masq script fragment to use iptables. [charlieb 1268]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Changing version to development stream number - 1.9.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Changing version to maintained stream number to 1.8.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.5-01]
- RPM rebuild forced by cvsroot2rpm

* Wed May  8 2002 Mark Knox <markk@e-smith.com>
- [1.7.4-01]
- Subst <base> -> </base> in lexicon [markk 3309]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.3-01]
- Localised "Network Time Server" heading [markk 3311]
- Localised date display [markk 3311]
- Added nav bar entry [gordonr 3155]

* Mon Apr 15 2002 Mark Knox <markk@e-smith.com>
- [1.7.2-01]
- Moved all code into module datetime.pm [markk 3159]
- Converted to FormMagick panel and internationalized [markk 3159]
- Added POD and testsuite [markk 3159]

* Fri Apr 5 2002 Kirrily Robert <skud@e-smith.com>
- [1.7.1-01]
- Testing CVS import

* Fri Apr 5 2002 Kirrily Robert <skud@e-smith.com>
- [1.7.0-01]
- rollRPM: Rolled version number to 1.7.0-01. Includes patches up to 1.6.0-01.

* Tue Dec 11 2001 Jason Miller <jay@e-smith.com>
- [1.6.0-01]
- rollRPM: Rolled version number to 1.6.0-01. Includes patches up to 1.5.0-02.

* Tue Nov 06 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-02]
- Initialise TimeZone db setting from /etc/sysconfig/clock if not set
- Branding changes in web panel.

* Tue Nov 6 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- Rolled version number to 1.5.0-01. Includes patches upto 1.4.0-03.

* Tue Aug 28 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-03]
- Removed deprecated post-restore event directory

* Fri Aug 17 2001 gordonr
- [1.4.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-06.

* Thu Aug 02 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-06]
- More branding changes

* Sun Jul 29 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-05]
- Branding text changes to the datetime web panel 

* Tue Jul 17 2001 Jason Miller <jmiller@e-smith.com>
- [1.3.0-04]
- Patch to datetime panel to fix mismatched section headers

* Tue May 29 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-03]
- fixed actions that had tied %conf when calling serviceControl (4 actions)

* Wed Apr 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-02]
- changing h4 tags to paragraph bold tags.

* Wed Apr 11 2001 Adrian Chung <mac@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-13.

* Fri Feb 23 2001 Paul Nesbit <pkn@e-smith.com>
- [1.2.0-13]
- Fixed conf-timezone to properly handle timezone after restore

* Mon Feb 12 2001 Adrian Chung <adrianc@e-smith.com>
- Roll release number for GPG signing.

* Mon Feb 12 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-12]
- Expand ntp.conf always, even when ntpd is disabled. Otherwise ntpd
  refuses to shut down.

* Fri Feb  9 2001 Adrian Chung <adrianc@e-smith.com>
- Added restart-crond to timezone-update event.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- Rolling release number for GPG signing.

* Wed Feb 07 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-08]
- Add some missing event symlinks

* Sun Feb 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-07]
- Loop through all addresses in case NTPServer refers to multiple IPs

* Fri Feb 02 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-06]
- Build ip masq rule with IP address of NTP server

* Tue Jan 30 2001 Jason Miller <jmiller@e-smith.com>
- [1.2.0-05]
- Updated datetime panel to run the timeserver-update
  event (added rules to make sure that updates to the
  configuration database aren't affected UnsavedChanges flag).

* Tue Jan 30 2001 Jason Miller <jmiller@e-smith.com>
- [1.2.0-04]
- Added a comment in the ipchains rules
- Added symlinks for the conf-masq and restart-masq actions
  to be run as part of timeserver-update event (thereby
  expanding the /etc/rc.d/init.d/masq template). 

* Sat Jan 27 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-03]
- Change ref to %conf => %services in masq template fragment

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-02]
- Fix perl syntax error in masq template fragment
- Save/restore unsavedchanges flag around timezone change.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-28.

* Wed Jan 24 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-28]
- Remove restart-ntp from post-upgrade action
- Remove post-restore event
- Tighten up NTP packet filter rule.
- Remove conf-ntpd from ip-change event
- Remove duplication of timezone migration code - it is in base as well.

* Wed Jan 24 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-27]
- Changed conf-timezone action so that during an upgrade
  it will preserve the existing symlink for /etc/localtime
  and use that value to set the configuration database
  value for TimeZone 

* Wed Jan 24 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-26]
- removed the signal event for datetime-set in the datetime
  web panel 

* Wed Jan 24 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-25]
- combined the timezone-update and datetime-set events
  into a single event (and might combine the action scripts
  as well) 

* Wed Jan 24 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-24]
- added new service control mechanism to not background
  the proxy-stop action to shutdown squid

* Tue Jan 23 2001 Jason Miller <jmiller@e-smith.com>
- moved all date and time settings into a new event/action
  sequence (datetime-set) which then calls the proxy-stop,
  set-date, set-clock, proxy-start and removed the previous
  system calls from the web manager form 
- removed the squid stop/start actions from conf-timezone
  action

* Mon Jan 22 2001 Jason Miller <jmiller@e-smith.com>
- Updated createlinks to have update-timezone and
  update-timeserver events link in the action restart-syslog
  to improve on the strange log times recorded otherwise 

* Mon Jan 22 2001 Jason Miller <jmiller@e-smith.com>
- Added service control to stop the proxy server (squid)
  from running prior to changing the timezone information
  in conf-timezone, then starting it again after the change
  to remove squid hangups on shutdown 

* Mon Jan 22 2001 Gordon Rowell <gordonr@e-smith.com>
- Added NTP fragment to packet filter - Thanks Bernd Leibing

* Tue Jan 16 2001 Jason Miller <jmiller@e-smith.com>
- Removed the %postun section which was deleting ntpd
  configuration values after uninstalling e-smith-ntp
  (which occurs in an upgrade) and the %post section
  which expanded the templates for ntpd without checking
  the status (now done properly in the actions) 

* Tue Jan 16 2001 Jason Miller <jmiller@e-smith.com>
- Fixed the /etc/ntp.conf template expansion to pull
  the NTPServer value from the ntpd service configuration
  settings 

* Tue Jan 16 2001 Jason Miller <jmiller@e-smith.com>
- Changed the order of system time setting:
-	Set timezone first, then clock settings 

* Fri Jan 12 2001 Jason Miller <jmiller@e-smith.com>
- Merged the conf-clock and reset-link into a single
  action script of conf-timezone
- Removed symlinks to post-upgrade and update-timezone
- Added symlink for conf-timezone to update-timezone
- Added symlink for conf-timezone to bootstrap-console-save
 (instead of post-upgrade) 

* Fri Jan 12 2001 Jason Miller <jmiller@e-smith.com>
- Added reset-link and conf-clock to the post-upgrade
  event

* Fri Jan 12 2001 Gordon Rowell <gordonr@e-smith.com>
- Added conf-ntpd-startup

* Thu Jan 11 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-13]
- remove extra signal events based on what time setting
  choice gets made 

* Thu Jan 11 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-12]
- updated datetime panel to take into account the new
  action scripts called by timezone-update event 

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-11]
- use serviceControl()

* Thu Jan 11 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-10]
- fixed /etc/sysconfig/clock template generation 

* Thu Jan 11 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-9]
- added conf-clock to configure /etc/sysconfig/clock
- added reset-link to unlink and re-symlink
  /etc/localtime to the correct timezone

* Sat Jan  6 2001 Jason Miller <jmiller@e-smith.com>
- [1.1.0-7]
- Charlie changed spec file in %post and %postun to
  generate ntpd templates in runlevel 7 and to remove 
  it if e-smith-ntp is uninstalled
- Added configuration parameter for timeZone which
  will be used by default as the timezone value for
  date and time, otherwise it defaults to /etc/localtime

* Fri Jan  5 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-6]
- add new event timezone-update that calls restart httpd
- datetime panel modified to call both time{server,zone}-update

* Fri Jan  5 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-5]
- Disable ntpd by default - without an NTPServer setting there's no
  point in enabling ntpd.
- Remove timeserver web form. Add Jay's new combined datetime and
  timeserver form.

* Fri Dec 15 2000 Adrian Chung <adrianc@e-smith.com>
- Changed NTPserver to NTPServer in 00timeServer fragment
- Modified timeserver panel to record timeserver value to ntpd
  property instead of legacy variable.

* Wed Dec  6 2000 Adrian Chung <adrianc@e-smith.com>
- Removed 'private' property setting in conf-ntpd
- Added link for conf-ntpd to post-install

* Wed Dec  6 2000 Adrian Chung <adrianc@e-smith.com>
- Re-rolled tar ball to get rid of symlinks

* Mon Dec  4 2000 Adrian Chung <adrianc@e-smith.com>
- Initial release

%description
Configuration files and templates for the NTP daemon.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
for i in ip-change post-install post-upgrade timeserver-update \
    timezone-update bootstrap-console-save
do
    mkdir -p root/etc/e-smith/events/$i
done
perl createlinks
/sbin/e-smith/buildtests 30e-smith-datetime

# Manage supervise and multilog.
mkdir -p root/service
ln -s ../var/service/ntpd root/service/ntpd
mkdir -p root/var/service/ntpd/supervise
mkdir -p root/var/service/ntpd/env
touch root/var/service/ntpd/down
mkdir -p root/var/service/ntpd/log/supervise
mkdir -p root/var/log/ntpd

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist \
    --dir '/var/service/ntpd' 'attr(1755,root,root)' \
    --file '/var/service/ntpd/down' 'attr(0644,root,root)' \
    --file '/var/service/ntpd/run' 'attr(0755,root,root)' \
    --dir '/var/service/ntpd/supervise' 'attr(0700,root,root)' \
    --dir '/var/service/ntpd/env' '%attr(0755,root,root)' \
    --file '/var/service/ntpd/env/MEMLIMIT' 'attr(0644,root,root)' \
    --dir '/var/service/ntpd/log' 'attr(1755,root,root)' \
    --file '/var/service/ntpd/log/run' 'attr(0755,root,root)' \
    --dir '/var/log/ntpd' 'attr(2750,smelog,nofiles)' \
    $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre
rm -f /etc/ntp.conf

%preun
%post
%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
