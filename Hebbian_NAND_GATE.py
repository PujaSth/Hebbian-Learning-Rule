#taking the input from user
input_value= [[1, 1], [1, -1], [-1, 1], [-1, -1]]
target_value=[-1, 1, 1, 1]
number_of_input_for_each_pattern = [2, 2, 2, 2]
pattern_number=4
    
#Initialize weight and bias
weight_initial=[]
bias_initial=0
for i in range(number_of_input_for_each_pattern[0]):
    w_old=0
    weight_initial.append(w_old)

#weight update
weight_old=weight_initial
bias_old=bias_initial
for i in range(pattern_number):
    weight_new=[]
    for j in range(number_of_input_for_each_pattern[i]):
        w_new=weight_old[j]+input_value[i][j]*target_value[i];
        weight_new.append(w_new)
    weight_old=weight_new
    bias_old += target_value[i];
    
#display 
print('Input number for each pattern : ',number_of_input_for_each_pattern)
print('Value of input for each pattern: ',input_value)
print('Target value: ',target_value)
print('Initial weight is: ',weight_initial,'and bias is: ',bias_initial)
print('Updated weight: ',weight_old,'\nUpdated bias: ',bias_old)
    