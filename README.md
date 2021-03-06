Infer.NET-sandbox
=================

Sandbox for playing around with [Infer.NET](http://research.microsoft.com/en-us/um/cambridge/projects/infernet/) models. I'm using [Mono](http://www.mono-project.com/) to run Infer.NET
in [IronPython](http://ironpython.net/) on Ubuntu 13.10.

I followed most of the instructions [here](http://crowdtheory.wordpress.com/2infer.n12/08/05/getting-infer-net-and-ironpython-to-work-on-ubuntu-12-04/)
to set up this environment. However, I did not need to install Wine, the Microsoft Infer.NET download was not a `msiexec`.

Once everything is installed, these `.bashrc` commands set up my environment:

    export IRONLANGUAGESDIR=/home/john/src/IronLanguages
    export IRONPYTHONPATH=$IRONLANGUAGESDIR/External.LCA_RESTRICTED/Languages/IronPython/27/Lib/:$IRONPYTHONPATH
    alias ironpy='mono $IRONLANGUAGESDIR/bin/Release/ipy.exe'

I have played around with the IronPython example code that comes with the Infer.NET distribution. I think the original code has just been tested under Mono on Windows. It didn't work so well on Ubuntu, some of the distribution classes (amongst others) would not `import` properly. The code in the IronPython directory fixes these problems with the examples.
