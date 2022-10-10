const strings = ['a', 'b', 'c', 'd'];

// 4 items
// In a 32 bits system we are using 4*4 = 16 bytes of storage

// O(1)
console.log(strings[2]);

// push O(1)
strings.push('e');

// pop O(1) bc computer knows where the last item is stored
// we are not looping
strings.pop();
strings.pop();

// unshift (javascript) O(n)
strings.unshift('x');

// splice O(n)
strings.splice(2, 0, '1'); // 0 bc we dont want to delete nothing
strings.splice(2, 2);

console.log(strings);