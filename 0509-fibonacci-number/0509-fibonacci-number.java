class Solution {
    public int fib(int n) {
        if(n==0 || n==1)
            return n;
        else
            return this.fib(n-1) + this.fib(n-2);
    }
}


