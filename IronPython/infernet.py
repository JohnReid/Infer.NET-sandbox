import clr
import os

def _addInferNetClrReferences(basepath):
    # add path to infer.net dlls .................................
    clr.AddReferenceToFileAndPath(os.path.join(basepath, "Infer.Runtime.dll"))
    clr.AddReferenceToFileAndPath(os.path.join(basepath, "Infer.Compiler.dll"))

def setup(infernetpackagedir="/home/john/src/Infer.NET"):
    _addInferNetClrReferences(os.path.join(infernetpackagedir, "Bin"))

