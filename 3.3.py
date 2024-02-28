#3.3. Bài toán ứng dụng 1: Giới thiệu Roullete Wheel – “Chiếc nón kì diệu”
from __future__ import division
import numpy as np
import random, pdb
import operator
def roulette_selection (weights) :

# sort the weights in ascending order
    sorted_indexed_weights = sorted (enumerate (weights), key=operator. itemgetter (1));indices, sorted_weights = zip (*sorted_indexed_weights); tot_sum=sum (sorted_weights)
    prob = [x/tot_sum for x in sorted_weights]
    cum_prob=np.cumsum (prob)
    random_num=random.random()
    for index_value, cum_prob_value in zip (indices, cum_prob) :
        if random_num < cum_prob_value:
            return index_value
        
xanhdo =[87, 3, 20]# khởi tạo các giá trị 
for i in range(20):
    print (roulette_selection(xanhdo))
xanhdo =[27, 3, 30] # khởi tạo các giá trị: đèn xanh gần bằng đèn đỏ 
for i in range(20):
    print (roulette_selection(xanhdo))