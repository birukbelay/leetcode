function chunk(arr: any[], size: number): any[][] {
    let ans =[]
    let temp=[]
    let ctr=0
    for (let i=0; i<arr.length; i++){
        temp.push(arr[i])
        ctr++
        
        if(ctr==size){
            ctr=0
            ans.push(temp)
            temp=[]
        }
    }
    if(ctr>0){
        ans.push(temp)
    }
    return ans
};
