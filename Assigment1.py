import math

# Question 1 
binary_number = "010000000111111010111001"
counter = 11
sum = 0
sum2 = 0
total = 0


for i in range(0,12):
  if(binary_number[i] == '1'):
    sum += pow(2,counter)
  counter -= 1 
#subract 1023 from the sum
sum -= 1023


counter = 1 
for i in range(12,24):
  if(binary_number[i] == '1'):
    sum2 += pow(1/2,counter)
  counter +=1
#add 1 to the sum2 as the formula 
sum2 +=1

total = float(pow(2,sum) * sum2)
print(total)
print("")

#Question 2
chopping = float(math.floor(total))
print(chopping)
print("")

#Question 3
rounding = float(math.ceil(total))
print(float(math.ceil(total)))
print("")

#Question 4 
absolute_error =float(abs(rounding-total))
print(absolute_error)
relative_error   =  float((absolute_error/total))
print("{:.31f}".format(relative_error))
print("")

#Question 5 
tolerance = .0001
k=1
x = 1
formula = ((-1**k) * (x**k)) / (k**3) 
counter = 0
while(abs(formula) >= tolerance ):
  k +=1
  formula = ((-1**k) * (x**k)) / (k**3)
  counter +=1
  
print(counter)
print("")


#Question 6 Bisection Method

def bisection_method(left: float, right: float, given_function: str):
    # pre requisites
    # 1. we must have the two ranges be on opposite ends of the function (such that
    # function(left) and function(right) changes signs )
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return

    tolerance: float = .0001
    diff: float = right - left

    # we can only specify a max iteration counter (this is ideal when we dont have all
    # the time in the world to find an exact solution. after 10 iterations, lets say, we
    # can approximate the root to be ###)
    max_iterations = 50
    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1

        # find function(midpoint)
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)

        if evaluated_midpoint == 0.0:
            break
        
        # find function(left)
        x = left
        evaluated_left_point = eval(given_function)
        
        # this section basically checks if we have crossed the origin point (another way
        # to describe this is if f(midpoint) * f(left_point) changed signs)
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)

        # OPTIONAL: you can see how the root finding for bisection works per iteration
    print(iteration_counter)


if __name__ == "__main__":


    # bisection gives us the first zero of any function to a certain error threshold
    left = -4
    right = 7
    function_string = "x**3 - (4*(x**2)) - 10"
    bisection_method(left, right, function_string)

print("")

#Question 6 Newton_Rapshon method

def custom_derivative(value):
    return (3 * value* value) - (2 * value)


def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    # remember this is an iteration based approach...
    iteration_counter = 0

    # finds f
    x = initial_approximation
    f = eval(sequence)

    # finds f' 
    f_prime = custom_derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)

        # finds f' 
        f_prime = custom_derivative(initial_approximation)

        # division operation
        approximation = f / f_prime

        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1
    print(iteration_counter)


if __name__ == "__main__":
    # newton_raphson method
    initial_approximation: float = 1
    tolerance: float = .0001
    sequence: str = "(x**3) - (x**2) + 4"

    newton_raphson(initial_approximation, tolerance, sequence)














