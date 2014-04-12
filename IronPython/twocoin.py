import infernet
infernet.setup()

from MicrosoftResearch.Infer import Models, Distributions, InferenceEngine

#-----------------------------------------------------------------------------------
# Infer.NET IronPython example: Two Coins
#-----------------------------------------------------------------------------------

# two coins example
print("\n\n------------------ Infer.NET Two Coins example ------------------\n");

# The model
b = Distributions.Bernoulli(0.5)
firstCoin = Models.Variable.Bernoulli(0.5)
secondCoin = Models.Variable.Bernoulli(0.5)
bothHeads = firstCoin & secondCoin

# The inference
ie = InferenceEngine()
print "Probability both coins are heads:", ie.Infer(bothHeads)
bothHeads.ObservedValue = False
print "Probability distribution over firstCoin:", ie.Infer(firstCoin)

