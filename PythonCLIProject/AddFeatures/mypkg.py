
import json
import os
import time
import argparse

REGISTRY = {
    "numpy": {"version": "1.21.0", "deps": []},
    "pandas": {"version": "1.3.0", "deps": ["numpy"]},
    "scipy": {"version": "1.7.0", "deps": ["numpy"]},
    "matplotlib": {"version": "3.4.2", "deps": ["numpy"]},
    "seaborn": {"version": "0.11.2", "deps": ["matplotlib", "pandas"]},
    "sklearn": {"version": "0.24.2", "deps": ["numpy", "scipy"]}
}

CACHE_FILE = "installed_packages.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(installed):
    with open(CACHE_FILE, "w") as f:
        json.dump(installed, f, indent=2)

def install(package, installed, verbose=False, dry_run=False):
    if package in installed:
        if verbose:
            print(f"✅ {package}=={installed[package]} is already installed.")
        return

    if package not in REGISTRY:
        print(f"❌ Error: Package '{package}' not found in registry.")
        return

    for dep in REGISTRY[package]["deps"]:
        install(dep, installed, verbose, dry_run)

    if verbose:
        print(f"📦 Installing {package}=={REGISTRY[package]['version']}...")

    time.sleep(0.5)
    if not dry_run:
        installed[package] = REGISTRY[package]["version"]

    print(f"✅ {package}=={REGISTRY[package]['version']} installed successfully!")

def uninstall(package, installed, verbose=False):
    if package not in installed:
        print(f"⚠️ {package} is not installed.")
        return

    dependents = [pkg for pkg, meta in REGISTRY.items() if package in meta["deps"] and pkg in installed]
    if dependents:
        print(f"❌ Cannot uninstall {package} — required by: {', '.join(dependents)}")
        return

    if verbose:
        print(f"🗑️ Uninstalling {package}...")

    time.sleep(0.5)
    del installed[package]
    print(f"✅ {package} uninstalled successfully!")

def main():
    parser = argparse.ArgumentParser(description="Simulated Package Manager CLI (like apt or mvn)")
    subparsers = parser.add_subparsers(dest="command")

    install_parser = subparsers.add_parser("install", help="Install a package")
    install_parser.add_argument("package", help="Package name to install")
    install_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    install_parser.add_argument("--dry-run", action="store_true", help="Simulate installation only")

    uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall a package")
    uninstall_parser.add_argument("package", help="Package name to uninstall")
    uninstall_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()
    installed = load_cache()

    if args.command == "install":
        install(args.package, installed, verbose=args.verbose, dry_run=args.dry_run)
        if not args.dry_run:
            save_cache(installed)

    elif args.command == "uninstall":
        uninstall(args.package, installed, verbose=args.verbose)
        save_cache(installed)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


