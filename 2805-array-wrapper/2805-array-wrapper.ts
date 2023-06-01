class ArrayWrapper {
    nums =[]
	constructor(nums: number[]) {
        this.nums=nums
    }

	valueOf() {
        let sum =0;
        for (let i of this.nums){
            sum = sum+i
        }
        return sum
    }

	toString() {
        let ans = '['+this.nums.join(',')+']'
        return ans
    }
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */