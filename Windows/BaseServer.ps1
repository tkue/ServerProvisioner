choco feature enable -n=allowGlobalConfirmation
choco feature enable -n=allowEmptyChecksum

Update-ExecutionPolicy Unrestricted
Enable-RemoteDesktop
Disable-InternetExplorerESC
Disable-MicrosoftUpdate
Disable-UAC

Set-ExplorerOptions -showHidenFilesFoldersDrives -showProtectedOSFiles -showFileExtensions
Set-StartScreenOptions -EnableBootToDesktop -EnableDesktopBackgroundOnStart -EnableShowStartOnActiveScreen -EnableSearchEverywhereInAppsView

Install-ChocolateyPinnedTaskBarItem "$env:windir\system32\mstsc.exe"
Install-ChocolateyPinnedTaskBarItem "$env:programfiles\console\console.exe"

# Updates
Install-WindowsUpdate -AcceptEula           # Security updates
if(Test-PendingReboot){Invoke-Reboot}       # Reboot if needed
Install-WindowsUpdate -AcceptEula -Full     # Install all updates

# Just to be sure (have had to do this manually)
if(Test-PendingReboot){Invoke-Reboot}
Install-WindowsUpdate -AcceptEula -Full
if(Test-PendingReboot){Invoke-Reboot}