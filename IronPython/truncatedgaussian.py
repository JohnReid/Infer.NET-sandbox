#-----------------------------------------------------------------------------------
# Infer.NET IronPython example: Truncated Gaussian with different thresholds
#-----------------------------------------------------------------------------------

import infernet
infernet.setup()

from MicrosoftResearch.Infer import Models, Distributions, InferenceEngine, ExpectationPropagation

print("\n\n------------------ Infer.NET Truncated Gaussian example ------------------\n");
# The model
threshold = Models.Variable.New[float]().Named("threshold")
x = Models.Variable.GaussianFromMeanAndVariance(0, 1).Named("x")
Models.Variable.ConstrainTrue(x > threshold)

# The inference, looping over different thresholds
ie = InferenceEngine()
ie.Algorithm = ExpectationPropagation()
threshold.ObservedValue = -0.1
for i in xrange(0, 11):
    threshold.ObservedValue = threshold.ObservedValue + 0.1
    print "Dist over x given thresh of ", threshold.ObservedValue, "=", ie.Infer(x)

