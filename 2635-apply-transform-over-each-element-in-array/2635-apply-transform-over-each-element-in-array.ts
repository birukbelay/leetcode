function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const newArr= new Array(arr.length)
    for (let i=0; i< arr.length; i++){
        newArr[i]= fn(arr[i],i)
    }
    return newArr
};