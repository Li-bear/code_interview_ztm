// Drop Non Dominants

function printAll(numbers){

    console.log('these are the numbers: ');
    numbers.forEach(function (number) {
        console.log(number);
    }); // O(n)

    console.log('and these are their sums');
    numbers.forEach(function(firstNumber){
        numbers.forEach(function(secondNumber){
            console.log(firstNumber + secondNumber);
        }); // O(n^2)
    });
}

// O(n+n^2)
// Drop Non dominants -> O(n^2)