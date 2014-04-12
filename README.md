Infer.NET-sandbox
=================

Code for playing with Infer.NET

Sandbox for playing around with Infer.NET models. I'm using Mono to run Infer.NET
in IronPython on Ubuntu 13.10.

These are the `.bashrc` commands to set up my environment:

    export IRONLANGUAGESDIR=/home/john/src/IronLanguages
    export IRONPYTHONPATH=$IRONLANGUAGESDIR/External.LCA_RESTRICTED/Languages/IronPython/27/Lib/:$IRONPYTHONPATH
    alias ironpy='mono $IRONLANGUAGESDIR/bin/Release/ipy.exe'
