from setuptools import setup, Distribution
from setuptools.command.install import install
from operator import itemgetter
import subprocess
import os
from pathlib import Path


PLUGIN_NAME = "killendpoint"
PACKAGE_NAME = "kismet_kill_endpoint_plugin"
SCRIPT_NAME = "kismet_kill_endpoint_plugin"
MANIFEST_FILE_NAME = "manifest.conf"


def get_install_options():
    distribution = Distribution()
    install_cmd = install(distribution)
    install_cmd.finalize_options()
    return vars(install_cmd)


def get_pkg_variable(name):
    try:
        return subprocess.check_output(
            f"pkg-config --variable={name} kismet", shell=True
        ).decode("utf-8").strip()
    except:
        return None


def link(src, dest):
    dest_path = Path(dest)
    parent = dest_path.parent

    if not parent.exists():
        os.makedirs(parent)

    os.link(src, dest)


class PostInstallCommand(install):
    def run(self):
        install.run(self)

        prefix_path = get_pkg_variable("prefix") or "/usr/local"
        bin_path = f"{prefix_path}/bin"
        plugin_path = get_pkg_variable("plugindir") or "/usr/local/lib/kismet"
        install_options = get_install_options()

        if install_options['install_scripts'] != bin_path:
            link(f"{install_options['install_scripts']}/{SCRIPT_NAME}", f"{bin_path}/{SCRIPT_NAME}")

        if install_options['install_libbase'] != plugin_path:
            link(
                f"{install_options['install_libbase']}/{PACKAGE_NAME}/{MANIFEST_FILE_NAME}",
                f"{plugin_path}/{PLUGIN_NAME}/{MANIFEST_FILE_NAME}",
            )


setup(
    name=PACKAGE_NAME,
    version="1.0.0",
    description="Exposes a REST endpoint to kill the Kismet process",
    author="McShaman",
    author_email="info@mcshaman.com",
    python_requires=">=3.2",
    install_requires=["psutil"],
    packages=[PACKAGE_NAME],
    entry_points={
        "console_scripts": [
            f"{SCRIPT_NAME} = {PACKAGE_NAME}.__main__:main"
        ]
    },
    package_data={"": [MANIFEST_FILE_NAME]},
    cmdclass={"install": PostInstallCommand},
)
