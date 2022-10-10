function binary_search(list,target){
    let first = 0
    let last = (list.length -1)
    while(first < last){
        let midpoint = Math.floor((first + last)/2)
        if(list[midpoint] === target){
            return true 
        }else if(target > list[midpoint]){
            first = midpoint+1
        }else{
            last = midpoint-1
        }
    }
    return false
}



const list = [0,1,2,3,4,5,6,7,8,9,10]


const result = binary_search(list,70)

function verify(result){
console.log('target found', result);
}

verify(result)


