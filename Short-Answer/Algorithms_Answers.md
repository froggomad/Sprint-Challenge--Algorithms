#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
The outer loop is checking to see if `a` is less than `n` cubed
The inner loop is adding 1 to a + n squared, thereby reducing complexity from O(n^3) O(n)
So the loop will only run n times in total


b) O(n log n)
I'm not sure if my notation is correct, but the complexity appears to be quadratic until analyzing it.
J is being checked to see if it's less than n before the inner loop is run
In the inner loop J is multiplying by 2
This means that j will always be twice i
But the outer is still running for the entirety of n

c) O(n-1)
This is a recursive function that reduces by 1 during each iteration.
the stop condition is bunnies being 0, and bunnies is reduced by 1 during each iteration

## Exercise II

I would use a binary search strategy to reduce the number of broken eggs. This would normally be O(log n) but mine would have to be a little more complex since the egg could break on a higher floor first I guess it would be O(log n + log (log n))... or something 

I'd start at the middle floor and drop the egg, then move up half the total number of floors on each iteration if the egg doesn't break, or down if it breaks. At the point it broke, I'd move half the floors between that floor and the last one I checked to see if it breaks again


egg_drop_test(floors, bottom, top):

    if top < bottom return -1 (the egg didn't break on any floor)

    mid = (bottom + top) // 2

    drop egg at mid

    breaks?

    no = travel up half floors until it breaks

    yes = travel down half floors until it doesn't break, returning the last floor it broke on

