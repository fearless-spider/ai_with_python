# XOR - feedforward neural network(FNN)
#
# x1 * w1 = h1, x2 * w2 = h2
# x1, x2 - inputs
# w1, w2, w3, w4 - weights, what object thinks
# h1, h2 - hidden neurons(results of calculations), not visible during the process
#
# h1=(x1*w1)+(x2*w4) #II.A.weight of hidden neuron h1, sum of opinions
# h2=(x2*w3)+(x1*w2) #II.B.weight of hidden neuron h2, sum of opinions
# deep learning - moving from one to another layer
# b1, b2 - bias
# y1, y2 - second hidden layer
# h1 = y1 * -b1
# h2 = y2 * b2
# set weights
# w1 = 0.5, w2 = 0.5, b1 = 0.5
# w3 = w2, w4 = w1, b2 = b1
# threshold I, layer 2
# if(h1>=1):h1=1;
# if(h1<1):h1=0;
# if(h2>=1):h2=1;
# if(h2<1):h2=0;
# h1 = h1 * -b1
# h2 = h2 * b2
#
# threshold II, final output
# y = h1 + h2
# if (y>=1):y=1
# if (y<1):y=0
#
# change the critical weights, try again until the solution is found
# w2 = w2 + 0.5
# b1 = b1 + 0.5
