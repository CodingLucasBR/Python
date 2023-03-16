import numpy as np

# MAX_PRODUCT
# Write a function max_product that takes v a vector and n, a positive
# integer, as inputs and computes the largest product of n consecutive
# elements of v. It returns the product and the index of the element of v
# that is the first term of the product. If there are multiple such
# products in v, the function must return the one with the smallest
# starting index. As an example, the following call
# >> [product, ind] = max_product([1 2 2 1 3 1],3);
# will assign 6 to product and 3 to ind since the max 3-term product in
# the input vector is 2*1*3.


def max_product(v, n):
    num = len(v) - n + 1
    ii = 0
    w = 0
    while num >= 1:
        if np.prod(v[ii:n]) > w:
            w = np.prod(v[ii:n])
            index = ii
        num -= 1
        ii += 1
        n += 1
    return w, index


x = np.arange(4, 16)
# x = np.array([15, 34, 2, 45, 7, 7, 2, 3, 13])
mp = max_product(x, 3)
print(mp[0])
print(mp[1])

