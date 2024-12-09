# ==============================================================================
# SQL Server 
# ==============================================================================

# --------------------------------------
# Applications
# --------------------------------------

# Java JRE 7 needed for Polybase
cinst jre8 --allow-empty-checksums 
if(Test-PendingReboot) {
    Invoke-Reboot
}    

# --------------------------------------
# Firewall
# --------------------------------------
# https://msdn.microsoft.com/en-us/library/cc646023.aspx


# Use either one

# netsh firewall set portopening protocol = TCP port = 1433 name = SQLPort mode = ENABLE scope = SUBNET profile = CURRENT  
netsh advfirewall firewall add rule name = SQLPort dir = in protocol = tcp action = allow localport = 1433 remoteip = localsubnet profile = DOMAIN  
