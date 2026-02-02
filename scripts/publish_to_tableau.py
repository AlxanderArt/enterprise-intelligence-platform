#!/usr/bin/env python3
"""
Publish workbooks and data sources to Tableau Server/Cloud
Requires: tableauserverclient package
"""

import tableauserverclient as TSC
import os
import argparse

def publish_to_tableau(server_url, token_name, token_value, site_id, project_name, workbook_path):
    """
    Publish a Tableau workbook to Tableau Server or Tableau Cloud

    Args:
        server_url: Tableau Server URL (e.g., https://your-server.com or https://prod-useast-b.online.tableau.com)
        token_name: Personal Access Token name
        token_value: Personal Access Token value
        site_id: Site ID (empty string for default site)
        project_name: Target project name
        workbook_path: Path to .twbx file
    """

    # Authenticate using Personal Access Token
    tableau_auth = TSC.PersonalAccessTokenAuth(token_name, token_value, site_id)
    server = TSC.Server(server_url, use_server_version=True)

    with server.auth.sign_in(tableau_auth):
        print(f"Signed in to {server_url}")

        # Find the project
        all_projects, _ = server.projects.get()
        project = next((p for p in all_projects if p.name == project_name), None)

        if not project:
            print(f"Project '{project_name}' not found. Creating...")
            new_project = TSC.ProjectItem(name=project_name)
            project = server.projects.create(new_project)

        print(f"Publishing to project: {project.name}")

        # Publish workbook
        workbook = TSC.WorkbookItem(project.id)
        workbook = server.workbooks.publish(workbook, workbook_path, mode=TSC.Server.PublishMode.Overwrite)

        print(f"Successfully published: {workbook.name}")
        print(f"Workbook ID: {workbook.id}")
        print(f"URL: {server_url}/#/workbooks/{workbook.id}")

def main():
    parser = argparse.ArgumentParser(description='Publish Tableau workbook to Server/Cloud')
    parser.add_argument('--server', required=True, help='Tableau Server URL')
    parser.add_argument('--token-name', required=True, help='Personal Access Token name')
    parser.add_argument('--token-value', required=True, help='Personal Access Token value')
    parser.add_argument('--site', default='', help='Site ID (default: empty for default site)')
    parser.add_argument('--project', default='Enterprise Intelligence', help='Target project name')
    parser.add_argument('--workbook', required=True, help='Path to .twbx file')

    args = parser.parse_args()

    publish_to_tableau(
        args.server,
        args.token_name,
        args.token_value,
        args.site,
        args.project,
        args.workbook
    )

if __name__ == "__main__":
    print("=" * 60)
    print("Tableau Publishing Script")
    print("=" * 60)
    print("\nUsage:")
    print("  python publish_to_tableau.py \\")
    print("    --server https://your-server.com \\")
    print("    --token-name 'MyToken' \\")
    print("    --token-value 'your-token-value' \\")
    print("    --project 'Enterprise Intelligence' \\")
    print("    --workbook ./tableau/enterprise_dashboard.twbx")
    print("\nFor Tableau Public, use the desktop app to publish directly.")
    print("=" * 60)
