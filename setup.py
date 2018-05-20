from subprocess import call

call(["sudo","apt-get", "install", "python-pip"])
call(["sudo","pip2", "install", "python-xlib"])


from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['xlib_keyboard_driver'],
    package_dir={'': 'src'}
)

setup(**setup_args)

