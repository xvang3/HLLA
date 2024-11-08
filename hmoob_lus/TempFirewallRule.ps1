# Define the port number and rule name
$port = 8000 # Replace with your port number if different
$ruleName = "Temp Local Server Access on Port $port"

# Add a temporary firewall rule for TCP traffic on the specified port
Write-Output "Creating firewall rule to allow access on port $port..."
New-NetFirewallRule -DisplayName $ruleName -Direction Inbound -Action Allow -Protocol TCP -LocalPort $port -Profile Any

# Start the server in a new process (adjust command to your server's start command)
Write-Output "Starting server..."
# Example command for Django server, replace with your actual server command if different
Start-Process "cmd.exe" -ArgumentList "/c python manage.py runserver 0.0.0.0:$port"

# Wait for user input to stop the server and remove the firewall rule
Read-Host -Prompt "Press Enter to stop the server and remove the firewall rule"

# Stop the server process (adjust the process name to match your server if necessary)
Write-Output "Stopping server and removing firewall rule..."
Stop-Process -Name "python" -Force # Replace "python" with your actual process name if needed

# Remove the firewall rule
Remove-NetFirewallRule -DisplayName $ruleName
Write-Output "Firewall rule removed."
