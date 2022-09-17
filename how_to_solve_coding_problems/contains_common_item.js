// Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
//For Example:
//const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
//should return false.
//-----------
//const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
//should return true.

// 2 parameters - arrays - no size limit
// return true or false

const array1 = [ 1, 'b', 'c', 'c'];
const array2 = ['z', 'z', 'r'];

// Brute approach:
function containsCommonItemFor(arr1, arr2)

// array1 ==> obj { convert array one into an object(hash tables in JS)
// a: true,
// b: true,
// c: true,
// x: true
//}
// Important: Object propierties are turned into strings when created

// array2[index] == obj.properties
// loop through only the second array

function containsCommonItem(arr1, arr2){
    // loop through first array and create an object
    // where propierties == items in the array

    // Improves:
    // can we assume always 2 params?
    // can we assume always 2 arrays pass as param?

    let map = {}
    for (let i = 0; i < arr1.length; i++){
        // check if map.a, map[each_element] exists
        if(!map[arr1[i]]){ // case: doesnt exists
            const item = arr1[i];
            map[item] = true; // adding element and assign it the property of true -> element: true
        }
    }
    console.log(map)
    // loop through second array ad check if item 
    // in second array exists on created object.
    for (let j =0; j <arr2.length; j++){
        if (map[arr2[j]]){
            return true;
        }
    }
    return false;
    // O(a + b) bc is a for after another for and not nested
    // Time complexity is better
}

// Using built-in JS methods to write more readable code for JS language
function containsCommonItem2(array1, array2){
    return array1.some(item => array2.includes(item))
}
// .some : iterates over each item in the array
// include the items in array2

console.log(containsCommonItem(array1, array2))
console.log("Second function: ")
console.log(containsCommonItem2(array1, array2))