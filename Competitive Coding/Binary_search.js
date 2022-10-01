const binarySearch = (nums, target) => {
    if(nums.length < 2){
        return target === nums[0] ? nums[0] : -1
    }
    
    const leftHalf = nums.slice(0, Math.round(nums.length/2))
    const rightHalf = nums.slice(Math.round(nums.length/2), nums.length)
    
    if(target > leftHalf[leftHalf.length - 1]){
        return binarySearch(rightHalf, target)
    }
    else if(target <= leftHalf[leftHalf.length - 1]){
        return binarySearch(leftHalf, target)
    }

}

////////EXAMPLE
const arr = [1,2,3,4,5,6,7]
const target = 4

binarySearch(arr, target) // returns 4