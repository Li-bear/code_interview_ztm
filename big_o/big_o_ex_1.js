// What is the Big O of the below function?
function funChallenge(input) 
{
    let a = 10; // O(1)
    a = 50 + 3; // O(1)
  
    for (let i = 0; i < input.length; i++) { // O(n) where n is the input
      anotherFunction(); // O(n)
      let stranger = true; //O(n)
      a++; // O(n)
    }
    return a; // O(1) run just once
}

// Big O(3 + 4n)
// Big O (n)