function minSubArrayLen(target: number, nums: number[]): number {
    let totS=0
    let r=0
    let minL=Number.MAX_SAFE_INTEGER
    
    for(let i=0; i<nums.length; i++){
        totS+=nums[i]
        
        while(totS>=target && i>=r){
            minL=Math.min((i-r), minL)
            totS-=nums[r]
            r+=1
        }        
    }
    if (minL===Number.MAX_SAFE_INTEGER) return 0
    return minL +1
    
};