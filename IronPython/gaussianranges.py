#-----------------------------------------------------------------------------------
# Infer.NET IronPython example: Truncated Gaussian with different thresholds
#-----------------------------------------------------------------------------------

import infernet
infernet.setup()

from MicrosoftResearch.Infer import Models, Distributions, InferenceEngine, \
        VariationalMessagePassing, ExpectationPropagation
from MicrosoftResearch.Infer.Models import Variable, Range
from MicrosoftResearch.Infer.Maths import Rand
import System

print("\n\n------------------ Infer.NET Learning a Gaussian example ------------------\n");

# The model
numdata = Variable.New[int]()
dataRange = Range(numdata)
dataRange.Name = "i"
x = Variable.Array[float](dataRange)
x.Name = "x"
mean = Variable.GaussianFromMeanAndVariance(0, 100)
mean.Name = "mean"
precision = Variable.GammaFromShapeAndScale(1, 1)
precision.Name = "precision"
x[dataRange] = Variable.GaussianFromMeanAndPrecision(mean, precision).ForEach(dataRange)

# The data
data = System.Array.CreateInstance(float, 100)
for i in xrange(0, data.Length):
    data[i] = Rand.Normal(0, 1)

# Binding the data
numdata.ObservedValue = data.Length
x.ObservedValue = data

# The inference
ie = InferenceEngine(VariationalMessagePassing())
ie.ShowFactorGraph = True
print "mean      = {0}".format(ie.Infer(mean))
print "precision = {0}".format(ie.Infer(precision))
