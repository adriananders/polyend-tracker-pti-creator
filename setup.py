""" Polyend Tracker .pti creator setup """
import distutils.cmd
import distutils.log
import os
import subprocess
import setuptools.command.build_py
import setuptools.command.install
from setuptools import setup

sources = ["./setup.py", "./polyend_tracker_pti_creator", "./tests"]


class PylintCommand(distutils.cmd.Command):
    """A custom command to run Pylint on all Python source files."""

    description = "run Pylint on Python source files"
    user_options = [
        # The format is (long option, short option, description).
        ("pylint-rcfile=", None, "path to Pylint config file"),
    ]

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        self.pylint_rcfile = "standard.rc"

    def finalize_options(self):
        """Post-process options."""
        if self.pylint_rcfile:
            assert os.path.exists(self.pylint_rcfile), (
                    f"Pylint config file {self.pylint_rcfile} does not exist."
            )

    def run(self):
        """Run command."""
        command = ["pylint"]
        if self.pylint_rcfile:
            command.append(f"--rcfile={self.pylint_rcfile}")
        command = command + sources
        self.announce(f"Running command: {str(command)}", level=distutils.log.INFO)
        subprocess.check_call(command)


class BlackCommand(distutils.cmd.Command):
    """A custom command to run Python Black on all Python source files."""

    description = "run Black on Python source files"
    user_options = [
        # The format is (long option, short option, description).
        ("black-config=", None, "path to black config file"),
    ]

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        self.black_config_file = ""

    def finalize_options(self):
        """Post-process options."""
        if self.black_config_file:
            assert os.path.exists(self.black_config_file), (
                    f"black config file {self.black_config_file} does not exist."
            )

    def run(self):
        """Run command."""
        command = ["black"]
        if self.black_config_file:
            command.append(f"--config={self.black_config_file}")
        command = command + sources
        self.announce(f"Running command: {str(command)}", level=distutils.log.INFO)
        subprocess.check_call(command)


class BuildPyCommand(setuptools.command.build_py.build_py):
    """Custom build command."""

    def run(self):
        setuptools.command.build_py.build_py.run(self)


class InstallPyCommand(setuptools.command.install.install):
    """Custom install command."""

    def run(self):
        pip_process = ["pip", "install", "-r"]
        subprocess.check_call(pip_process + ["./requirements.txt"])
        subprocess.check_call(pip_process + ["./test_requirements.txt"])
        setuptools.command.install.install.run(self)


setup(
    name="polyend_tracker_pti_creator",
    version="0.1.0",
    packages=[
        "polyend_tracker_pti_creator",
        "polyend_tracker_pti_creator.utils",
        "polyend_tracker_pti_creator.utils.audio",
        "polyend_tracker_pti_creator.utils.pti",
    ],
    python_requires=">=3",
    entry_points={
        "console_scripts": ["pet-pti-creator=polyend_tracker_pti_creator.creator:main"]
    },
    cmdclass={
        "format": BlackCommand,
        "build_py": BuildPyCommand,
        "install": InstallPyCommand,
        "lint": PylintCommand,
    },
    test_suite="tests",
    url="https://github.com/adriananders/polyend-tracker-pti-creator",
    license="MIT",
    author="Adrian Anders",
    author_email="realaanders@gmail.com",
    description="Polyend Tracker .pti instrument creator",
)
