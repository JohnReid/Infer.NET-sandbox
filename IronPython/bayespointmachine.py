#-----------------------------------------------------------------------------------
# Infer.NET IronPython example: Truncated Gaussian with different thresholds
#-----------------------------------------------------------------------------------

import infernet
infernet.setup()

from MicrosoftResearch.Infer import Models, Distributions, InferenceEngine, \
        VariationalMessagePassing, ExpectationPropagation, Maths
from MicrosoftResearch.Infer.Distributions import VectorGaussian, Distribution, Bernoulli
from MicrosoftResearch.Infer.Models import Variable, Range
from MicrosoftResearch.Infer.Maths import Rand, Vector, PositiveDefiniteMatrix
import System

print("\n\n------------------ Infer.NET Bayes Point Machine example ------------------\n");
# The model
len = Variable.New[int]().Named("N")
j = Range(len).Named("j")
x = Variable.Array[Vector](j).Named("x")
y = Variable.Array[bool](j).Named("y")
w0 = VectorGaussian(Vector.Zero(3), PositiveDefiniteMatrix.Identity(3))
w = Variable.Random[Vector](w0).Named("w")
noise = 0.1
y[j] = Variable.GaussianFromMeanAndVariance(
        Variable.InnerProduct(w, x[j]).Named("innerProduct"), noise) > 0

# The data
incomes = System.Array[float]((63, 16, 28, 55, 22, 20 ))
ages = System.Array[float]((38, 23, 40, 27, 18, 40 ))
willBuy = System.Array[bool]((True, False, True, True, False, False))
dataLen = willBuy.Length
xdata = System.Array.CreateInstance(Vector, dataLen)
for i in range(0, dataLen):
    xdata[i] = Vector.FromArray(System.Array[float]((incomes[i], ages[i], 1.0)))

# Binding the data
x.ObservedValue = xdata
y.ObservedValue = willBuy
len.ObservedValue = dataLen

# Inferring the weights
ie = InferenceEngine()
ie.ShowFactorGraph = True
wPosterior = ie.Infer[VectorGaussian](w)
print "Dist over w=\n", wPosterior

# Prediction
incomesTest = System.Array[float]((58, 18, 22))
agesTest = System.Array[float]((36, 24, 37))
testDataLen = incomesTest.Length
xtestData = System.Array.CreateInstance(Vector, testDataLen)
for i in range(0, testDataLen):
    xtestData[i] = Vector.FromArray(System.Array[float]((incomesTest[i], agesTest[i], 1.0)))

jtest = Range(testDataLen).Named("j")
xtest = Variable.Observed[Vector](xtestData, jtest).Named("xtest")
wtest = Variable.Random[Vector](wPosterior).Named("wtest")
ytest = Variable.Array[bool](jtest).Named("ytest")
ytest[jtest] = Variable.GaussianFromMeanAndVariance(
                    Variable.InnerProduct(wtest, xtest[jtest]).Named("innerproduct"), noise) > 0
ypred = Distribution.ToArray[System.Array[Bernoulli]](ie.Infer(ytest))
print "Output = ", ypred[0], ",", ypred[1], ",", ypred[2]
