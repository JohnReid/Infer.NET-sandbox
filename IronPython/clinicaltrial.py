#-----------------------------------------------------------------------------------
# Infer.NET IronPython example: Truncated Gaussian with different thresholds
#-----------------------------------------------------------------------------------

import infernet
infernet.setup()

from MicrosoftResearch.Infer import Models, Distributions, InferenceEngine, \
        VariationalMessagePassing, ExpectationPropagation, Maths
from MicrosoftResearch.Infer.Distributions import VectorGaussian, Distribution, Bernoulli, Beta
from MicrosoftResearch.Infer.Models import Variable, Range
from MicrosoftResearch.Infer.Maths import Rand, Vector, PositiveDefiniteMatrix
import System

print("\n\n------------------ Infer.NET Clinical Trial example ------------------\n");

controlGroup = Variable.Observed[bool](System.Array[bool]((False, False, True, False, False))).Named("controlOutcome")
treatedGroup = Variable.Observed[bool](System.Array[bool]((True, False, True, True, True ))).Named("treatmentOutcome")
i = controlGroup.Range.Named("i")
j = treatedGroup.Range.Named("j")

# Prior on being an effective treatment
isEffective = Variable.Bernoulli(0.5).Named("isEffective");

# If block
with Variable.If(isEffective):
    probIfControl = Variable.Beta(1, 1).Named("probIfControl")
    controlGroup[i] = Variable.Bernoulli(probIfControl).ForEach(i)
    probIfTreated = Variable.Beta(1, 1).Named("probIfTreated")
    treatedGroup[j] = Variable.Bernoulli(probIfTreated).ForEach(j)

# If Not block
with Variable.IfNot(isEffective):
    probAll = Variable.Beta(1, 1).Named("probAll")
    controlGroup[i] = Variable.Bernoulli(probAll).ForEach(i)
    treatedGroup[j] = Variable.Bernoulli(probAll).ForEach(j)

# The inference
ie = InferenceEngine()
ie.ShowFactorGraph = True
print "Probability treatment has an effect            = {0}".format(ie.Infer(isEffective))
print "Probability of good outcome if given treatment = {0}".format(ie.Infer[Beta](probIfTreated).GetMean())
print "Probability of good outcome if control         = {0}".format(ie.Infer[Beta](probIfControl).GetMean())




