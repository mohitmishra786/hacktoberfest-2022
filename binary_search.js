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

function recursive_binary(list,target){
    if(list.length === 1 && list[0] !== target){
        return false
    }
    let midpoint = Math.floor((list.length)/2)
    if(list[midpoint]=== target){
        return true
    }else if(target > list[midpoint]){
        return recursive_binary(list.slice((midpoint)),target)

    }else if(target < list[midpoint]){
        return recursive_binary(list.slice(0,(midpoint)),target)
    }
}


const list = [0,1,2,3,4,5,6,7,8,9,10]


const result = binary_search(list,11)
const result1 = binary_search(list,70)

function verify(result){
console.log('target found', result);
}

verify(result)
verify(result1)



