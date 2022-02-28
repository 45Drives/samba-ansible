Linux SMB Fileserver - Samba, Winbind, SSSD - Whats the deal

First some definitions:

Samba:
Samba is a free software re-implementation of the SMB networking protocol. Samba provides file services for various Microsoft Windows clients and can integrate with a Microsoft Windows Server domain, either as a Domain Controller (DC) or as a domain member. As of version 4, it supports Active Directory and Microsoft Windows NT domains.

Winbind:
Developed by samba team to be used alongside smb to integrate into domains
Handles the domain interaction, id mapping of SIDs to UID/GIDs.

SSSD:
SSSD is developed independantly from samba team, 
The System Security Services Daemon (SSSD) is software originally developed for the Linux operating system (OS) that provides a set of daemons to manage access to remote directory services and authentication mechanisms. The beginnings of SSSD lie in the open-source software project FreeIPA (Identity, Policy and Audit).he purpose of SSSD is to simplify system administration of authenticated and authorised user access involving multiple distinct hosts. It is intended to provide single sign-on capabilities to networks based on Unix-like OSs that are similar in effect to the capabilities provided by Microsoft Active Directory Domain Services to Microsoft Windows networks


Tradionally Samba+ Winbind has been the accepted solution for domain join's.

Since the development of SSSD, it was possible to join a domain with Samba+SSSD and leave winbind out of it.

This is where the confusion starts

You will find documentation online referening pure samba+sssd setups but they are all out of date.
You can find redhat blogs/articles stating why its best to drop winbind for SSSD.

However more recent docs are back to using Samba+SSSD+Winbind.

So what is the supported method as of today ?
Two method are supported
* "Traditional" Samba+Winbind
* "Modern" Samba+Winbind+SSSD

Why SSSD instead of winbind in the first place ?
* get info from here
https://www.redhat.com/en/blog/overview-direct-integration-options

Why do we need to interject a third daemon service into an already complex setup ?
* Well you dont, if you want to keep using samba+winbind. But if you need to use SSSD then all three must be used
The reasoning is due to samba code changes in verisons >=4.8.0

As per the samba relaese for v4.8.0

"Domain member setups require winbindd - Setups with "security = domain" or
"security = ads" require a
running 'winbindd' now. The fallback that smbd directly contacts domain
controllers is gone."

So as long as samba has security set to "domain" or "ads", which it needs to function properly in a domain integrtaion, winbind must be used.

Do I really need to use all three can I stick to a samba+winbind setup ?

yes you can stick to pure winbind, 

SSSD+Winbind
- Best used when mixed Linux and Windows Client Machines
    - simple join of domains for linux clients w. SSSD
    - windows machines join normally to AD
    - NTLM logins are NOT needed, only kerberos tickets allowed to access storage
    - While file server itself must be joined via winbind and SSSD, linux clients accessing fileserevr only needs to be joined with SSSD.
Pure Winbind
- Best used when only windows client machines accessing storage
    - NTLM Supported
    - 


references:
https://access.redhat.com/articles/4355391
https://lists.fedorahosted.org/archives/list/sssd-users@lists.fedorahosted.org/thread/ACEUWJTGJUWUUD32EBN2I7PXIVZD3PTM/
https://www.redhat.com/en/blog/overview-direct-integration-options
https://www.redhat.com/en/blog/sssd-vs-winbind