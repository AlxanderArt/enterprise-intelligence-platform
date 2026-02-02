#!/bin/bash
#
# Refresh Tableau extracts using tabcmd
# Requires: tabcmd installed and configured
#

set -e

# Configuration
SERVER_URL="${TABLEAU_SERVER:-https://your-server.com}"
SITE_ID="${TABLEAU_SITE:-}"
USERNAME="${TABLEAU_USER:-}"
PASSWORD="${TABLEAU_PASSWORD:-}"
WORKBOOK_NAME="Enterprise_Intelligence_Platform"

echo "=============================================="
echo "Tableau Extract Refresh Script"
echo "=============================================="

# Check if tabcmd is installed
if ! command -v tabcmd &> /dev/null; then
    echo "Error: tabcmd is not installed."
    echo "Download from: https://www.tableau.com/products/server/download"
    exit 1
fi

# Login to Tableau Server
echo "Logging in to Tableau Server..."
if [ -n "$SITE_ID" ]; then
    tabcmd login -s "$SERVER_URL" -t "$SITE_ID" -u "$USERNAME" -p "$PASSWORD"
else
    tabcmd login -s "$SERVER_URL" -u "$USERNAME" -p "$PASSWORD"
fi

# Refresh extracts
echo "Refreshing extracts for: $WORKBOOK_NAME"
tabcmd refreshextracts --workbook "$WORKBOOK_NAME"

# Logout
echo "Logging out..."
tabcmd logout

echo "=============================================="
echo "Extract refresh complete!"
echo "=============================================="

# Alternative: Use REST API for refresh
# curl -X POST \
#   "$SERVER_URL/api/3.x/sites/$SITE_ID/workbooks/$WORKBOOK_ID/refresh" \
#   -H "X-Tableau-Auth: $AUTH_TOKEN"
