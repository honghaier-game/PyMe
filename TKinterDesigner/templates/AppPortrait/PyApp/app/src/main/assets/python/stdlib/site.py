from __future__ import print_function
import sys
import os
if sys.version_info < (3, 0):
    import __builtin__ as builtins
else:
    import builtins
import _sitebuiltins


def makepath(*paths):
    dir = os.path.join(*paths)
    try:
        dir = os.path.abspath(dir)
    except OSError:
        pass
    return dir, os.path.normcase(dir)


def abs_paths():
    """Set all module __file__ and __cached__ attributes to an absolute path"""
    for m in set(sys.modules.values()):
        if (getattr(getattr(m, '__loader__', None), '__module__', None) !=
                '_frozen_importlib'):
            continue   # don't mess with a PEP 302-supplied __file__
        try:
            m.__file__ = os.path.abspath(m.__file__)
        except (AttributeError, OSError):
            pass
        try:
            m.__cached__ = os.path.abspath(m.__cached__)
        except (AttributeError, OSError):
            pass


def addpackage(sitedir, name, known_paths):
    """Process a .pth file within the site-packages directory:
       For each line in the file, either combine it with sitedir to a path
       and add that to known_paths, or execute it if it starts with 'import '.
    """
    fullname = os.path.join(sitedir, name)
    try:
        f = open(fullname, "r")
    except OSError:
        return
    with f:
        for n, line in enumerate(f):
            if line.startswith("#"):
                continue
            try:
                if line.startswith(("import ", "import\t")):
                    exec(line)
                    continue
                line = line.rstrip()
                dir, dircase = makepath(sitedir, line)
                if not dircase in known_paths and os.path.exists(dir):
                    sys.path.append(dir)
                    known_paths.add(dircase)
            except Exception:
                print("Error processing line {:d} of {}:\n".format(n+1, fullname),
                      file=sys.stderr)
                import traceback
                for record in traceback.format_exception(*sys.exc_info()):
                    for line in record.splitlines():
                        print('  '+line, file=sys.stderr)
                print("\nRemainder of file ignored", file=sys.stderr)
                break


def add_zip_package(sitedir, zip_name, known_paths):
    dir, dircase = makepath(sitedir, zip_name)
    if not dircase in known_paths and os.path.exists(dir):
        sys.path.append(dir)
        known_paths.add(dircase)


def addsitedir(sitedir, known_paths):
    sitedir, sitedircase = makepath(sitedir)
    if not sitedircase in known_paths:
        sys.path.append(sitedir)        # Add path component
        known_paths.add(sitedircase)
    try:
        names = os.listdir(sitedir)
    except OSError:
        return
    pth_names = [name for name in names if name.endswith(".pth")]
    zip_names = [name for name in names if name.endswith(".zip")]
    for name in sorted(pth_names):
        addpackage(sitedir, name, known_paths)
    for name in sorted(zip_names):
        add_zip_package(sitedir, name, known_paths)


def setquit():
    """Define new builtins 'quit' and 'exit'.

    These are objects which make the interpreter exit when called.
    The repr of each object contains a hint at how it works.

    """
    if os.sep == ':':
        eof = 'Cmd-Q'
    elif os.sep == '\\':
        eof = 'Ctrl-Z plus Return'
    else:
        eof = 'Ctrl-D (i.e. EOF)'

    builtins.quit = _sitebuiltins.Quitter('quit', eof)
    builtins.exit = _sitebuiltins.Quitter('exit', eof)


def setcopyright():
    """Set 'copyright' and 'credits' in builtins"""
    builtins.copyright = _sitebuiltins._Printer("copyright", sys.copyright)
    builtins.credits = _sitebuiltins._Printer("credits", """\
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.""")
    builtins.license = _sitebuiltins._Printer(
        "license",
        "See https://www.python.org/psf/license/")


def sethelper():
    builtins.help = _sitebuiltins._Helper()


def main():
    abs_paths()
    sitedir = os.path.join(os.path.dirname(sys.executable), "site-packages")
    if os.path.isdir(sitedir):
        known_paths = set()
        addsitedir(sitedir, known_paths)

    setquit()
    setcopyright()
    sethelper()


if not sys.flags.no_site:
    main()
