# Chocolately options
choco feature enable -n=allowGlobalConfirmation
# choco feature enable -n=allowEmptyChecksum

# Updates
Install-WindowsUpdate -AcceptEula
if(Test-PendingReboot){Invoke-Reboot}
Install-WindowsUpdate -AcceptEula -Full

# Just to be sure (have had to do this manually)
if(Test-PendingReboot){Invoke-Reboot}
Install-WindowsUpdate -AcceptEula -Full

# Windows Config
Update-ExecutionPolicy Unrestricted
Enable-RemoteDesktop
Disable-InternetExplorerESC
Disable-MicrosoftUpdate
Disable-UAC
Set-ExplorerOptions -showHidenFilesFoldersDrives -showProtectedOSFiles -showFileExtensions
Set-StartScreenOptions -EnableBootToDesktop -EnableDesktopBackgroundOnStart -EnableShowStartOnActiveScreen -EnableShowAppsViewOnStartScreen -EnableSearchEverywhereInAppsView -EnableListDesktopAppsFirst

# Frameworks
cinst PowerShell -source windowsfeatures
cinst DotNet4.0 -source windowsfeatures
cinst DotNet4.5 -source windowsfeatures
cinst DotNet5.0 -source windowsfeatures

# Basic Apps
cinst 7zip.install

cinst git.install

cinst nugetpackagemanager
cinst nuget.commandline

cinst sublimetext3
cinst sublimetext3.packagecontrol
cinst openinsublimetext # Adds a menu command that lets you open any solution, project, folder and file in Sublime Text.
cinst sublimetext3.powershellalias # add powershell subl command

cinst python3
cinst python2
cinst pip
cinst pywin32
cinst ironpython
cinst python.pypy


# Unlocker
# http://update.iobit.com/dl/unlocker-setup.exe
Install-ChocolateyPackage 'unlocker-setup' 'exe' '/passive /norestart' 'http://update.iobit.com/dl/unlocker-setup.exe'


Install-ChocolateyPinnedTaskBarItem "$env:programfiles\console\console.exe"
Install-ChocolateyPinnedTaskBarItem "$env:programfiles\Sublime Text 3\sublime_text.exe"


if(Test-PendingReboot){Invoke-Reboot}
