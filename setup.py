from setuptools import find_packages, setup

from drive_amplifier_ds.version import __version__, licence
from drive_amplifier_ds import __doc__, __author__, __author_email__

setup(
    name='drive_amplifier',
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license=licence,
    description="Tango device class for drive amplifier device.",
    long_description=__doc__,
    url="https://github.com/synchrotron-solaris/dev-solaris-driveamplifier.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["setuptools"],
    entry_points={
        "console_scripts": ["DriveAmplifier = "
                            "drive_amplifier_ds.drive_amplifier:run"]}
    )
