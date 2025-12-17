https://www.geeksforgeeks.org/time-complexities-of-different-data-structures/

Best (omega), worst (O), Avg (Theta)
**Asymptotic Analysis:**
Measuring order of growth based on input size

fun1() --> c1 constant Ex: return n*(n+1)/2
fun2 --> c2 * n +c3 Ex: for i in range(1,n+1):
fun3 --> c4n^2+c5n+c6  Ex: for nested loops

c < logN < sqrt n < n < sq n < 2 ^ n < n ^n 
If the loop variable is multiplied/division by c times then the time is 0(logN to the base c)
If the loop variable is power i**c then time is (logc logN)
For graphs we need to seperate vertices and edges for time complexity 0(m+n)
Recursion: 2T(n/2)+c --> n
2T(n/2) +nc --> nlogn
2T(n)+c --> 2^n
T(n/2) --> logn 
T(n/4)+T(n/2)+nc --> 0(n)
T(n-1)+ T(n-2) +c --> 0(2^n)

Space complixity: if input is list then 0(n)
Auxiliary space : order of growth of extra space (other than input and output)
