# System Expert Website (Frappe/ERPNext App)

A minimal website app using Frappe Website (extends `templates/web.html`). Ready for ERPNext v14–v15.

## Install (recommended via git local URL)
```bash
# inside your bench (WSL Ubuntu)
cd ~/frappe-bench
bench get-app file:///mnt/c/Users/<YOUR_USER>/system_expert_site   # if you 'git init' the folder on Windows
bench --site your-site.local install-app system_expert_site
bench build --force && bench restart
```

## Manual copy (no git)
```bash
cd ~/frappe-bench
cp -r /mnt/c/Users/<YOUR_USER>/system_expert_site apps/system_expert_site
./env/bin/pip install -e apps/system_expert_site
bench --site your-site.local install-app system_expert_site
bench build --force && bench restart
```
