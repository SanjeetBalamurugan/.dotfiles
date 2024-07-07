import subprocess


class PackageInstaller:
    packages = []
    packageManager = ""

    def addToPackageStack(self, packageName: str) -> bool:
        self.packages.append(packageName)
        return True

    def installPackages(self) -> bool:
        command = f"sudo {self.packageManager} install " + " ".join(self.packages)
        print("=" * 60)
        print(f"Running Command: {command}\n")
        installCommand = "install"
        if self.packageManager == "pacman":
            installCommand = "-S"
        subprocess.call(["sudo", self.packageManager, installCommand] + self.packages)
        print("=" * 60)
        return False

    def getCorrectPackage(
        self, packageNameApt: str, packageNameDnf: str, packageNamePacman: str
    ) -> str:
        if self.packageManager == "apt":
            return packageNameApt
        elif self.packageManager == "dnf":
            return packageNameDnf
        elif self.packageManager == "pacman":
            return packageNamePacman
        else:
            return ""

    def setPackageManager(self, packageManager: str) -> None:
        self.packageManager = packageManager
