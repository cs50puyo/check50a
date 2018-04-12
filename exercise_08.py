x_cordenates, y_cordenates = eval(input("Enter a point's x- and \
y-coordinates:"))

if x_cordenates >= 0 and y_cordenates >= 0 and \
(x_cordenates + 2 * y_cordenates <= 200):
    print("The point is in the triangle")
else:
    print("The point is not in the triangle")

# inequalities y = 0, x = 0 ; x + 2y = 200
