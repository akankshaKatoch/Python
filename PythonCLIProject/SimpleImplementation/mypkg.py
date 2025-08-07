import sys
import time

REGISTRY = {
    "numpy": [],
    "pandas": ["numpy"],
    "scipy": ["numpy"], 
    "matplotlib": ["numpy"],
    "seaborn": ["matplotlib", "pandas"],
    "sklearn": ["numpy", "scipy"]

}

INSTALLED = set()

def install(package):
    if package is INSTALLED:
        print(f" {package} is already installed. ")
        return 
    
    if package not in REGISTRY:
        print(f" Error: Package '{package} not found in registry. " )

    # installation of dependencies. 
    for dep in REGISTRY[package]:
        install(dep)
    
    print(f" Installing {package}...")
    time.sleep(1)
    INSTALLED.add(package)
    print(f"{package} installed successfully!")


def main():
    if len(sys.argv)<3 or sys.argv[1] != "install":
        return 
    
    package = sys.argv[2]
    install(package)

if __name__ == "__main__":
    main()

