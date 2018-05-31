

what is machine learning?
2 definitions.
  1. Arthur Samuel = "The field of study that gives computers the ability to learn without being explicitly programmed"
  2. Tom Mitchell = "A computer program is said to learn from experience E with respect to some class of tasks T and performance measured P,
                    if its performance as tasks in T, as measured by P, improves with experience E."

Example: playing checkers
E = the experience of playing many games of checkers
T = the task of playing checkers
P = the probability that the program will win the next game

In general, any ML problem can be assigned to one of the two broad classifications
a. Supervised learning
      example: "right answers" given
      regression: predict continuous valued output (price) = housing price predict
      classifications: discrete valued output (0 or 1)  = breast cancer (malignant, benign  )


      In Supervised learning, we are given a data set and already know what our correct
      output should look like, having the idea that there is a relationship between input and output.

      Example 1:
      Given data about the size of houses on a real estate market, try to predict their price. Price as a function of
      size is a continuous output, so this is a regression problem.

      We could turn this example into a classification problem instead of making our output about whether the house "sells for more or less than the asking price."
      Here we are classifying the houses based on price into two discrete categories.

      Example 2:
      (a) Regression - Given a picture of a person, we have to predict their age on basis of the given picture
      (b) classification - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign.


b. unsupervised learning
    example:  news.google.com --> cluster articles together
              Organize computing clusters, social network analysis, market segmentation, astronomical data analysis

        unsupervised learning allows us to approach problems with little or no idea what our results should look like.
        We can derive structure from data where we don't necessarily know the effect of variables.

        We can derive this structure by clustering the data based on relationships among the variables in the data.

        With unsupervised learning there is no feedback based on the prediction results.

        Example:
        Clustering: Take a collection of 1m different genes, and find a way to automatically group these genes
        into groups that are somehow similar or related by different variables, such as lifespan, location, roles and so on.

        Non-clustering: The "Cocktail Party Algorithm" , allows you to find structure in a chaotic environment.


Model Representation  
  House Prices = Supervised learning, regression (predict real-valued output)
    training set of size in feet squared and price in 1,000s
    Notation:
      m = Number of training examples
      x's = "input" variable/features             = size in feet
      y's = "output" variable /"target" variable  = price in 1,000s
      (x,y) - one training example
      (x^i, y^i) - i^th training example        = i is a index, not power of i
        x^1, y^1 =  2104, 460

    Training Set --> Learning Algorithm --> hypothesis
      input size of house and output the price of the house
      h maps from x's and y's

      linear regression with one variable
      univariate linear regression
Cost Function
    squared error Function - used a lot in regression for cost function.
    Cost function = we can measure the accuracy of our hypothesis function by using a cost function.
    This takes an average difference (actually a fancier version of an average) of all results of the hypothesis with inputs from x's and the actual output y's.

Cost Function - Intuition I
      y = mx  + b
      Points:
        (1,1), (2,2), (3,3)
          J(theta 0.5) = (1/(2m))[(0.5-1)^2 + (0.5-2)^2 + (0.5-3)^2]
                        = (1 / (2*3)) (3*5)
                        = (3*5)/6
                        = 0.58
          J(theta 0)    = (1/(2m)) (1^2 + 2^2 +3^2)
                        = (1/6) * 14
                        = 2.3

Cost Function - Intuition II                        


Gradient Descent
  Assignment
      a := b  --> a := a+1  
  Truth Assertion
      a = b   --> a  = a+1 (wrong)

Gradient Descent Intuition
      As we approach a local minimum, gradient descent will automatically take smaller steps.
      So, no need to decrease theta over time.


Matrix and Vectors
  Maxtrix
  [ 1402 191
    1371  821
    949   1437] = 4x2 Matrix

  [ 1 2 3
    4 5 6] = 2x3 Matrix

  Dimension of Matrix: number of rows X number of columns

  Matrix Elements(entries of matrix)
  A = [ 1402  191
        1371  821
        949   1437
        147   1448]

  Aij = "i, j entry" in the ith row, jth column
  A11 = 1402
  A12 = 191

  Vector: An nx1 Matrix
   y = [460
        232
        315
        178]
    n = 4
    4 Dimensional Vector
    yi = ith Element
    y1 = 460
    y2 = 232

Matrix Addition
  [ 1 0     [ 4 0.5      [  5  0.5
    2 5   +   2 5     =     4 10    
    3 1       0 1           3   2
    ]       ]             ]
    Can only add maxtrix of same size

Scalar (real number) Multiplication:
      [ 1 0       [ 3  0
  3x    2 5   =     6 15
        3 1]        9   3]

Matrix Vector Multiplication
  [ 1 3   [ 1          [1*1 + 3*5       [ 16
    4 0     5   =       4*1 + 0*5     =    4
    2 1   ]             2*1 + 1*5          7
]                     ]                 ]


Housing price trick with Matrix:
  house sizes: 2104, 1416, 1534, 852
  h theta (x) = -40 + 0.25x
  matrix:
  [ 1 2104        [ -40             [ -40*1 + 0.25*2104           [ 486
    1 1416    X     0.25      =       -40*1 + 0.25*1416     =       314
    1 1534        ]                   -40*1 + 0.25*1534             343.5
    1 825                             -40*1 + 0.25*825              166.25
  ]                                 ]                             ]

  prediction = DataMatrix * parameters
