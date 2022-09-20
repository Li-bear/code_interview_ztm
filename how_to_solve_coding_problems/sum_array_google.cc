#include <iostream>
#include <vector>
#include <unordered_set>

bool HasPairWithSum(const std::vector <int> data, int sum){
    // hash set in c++ is an unordered_set
    
    // unordered_set is an associative container that contains a 
    // set of unique objects of type Key
    // Search, insertion, and removal have average constant-time complexity.
    
    // constant-time complexity If an algorithm's time complexity is constant, 
    // it means that it will always run in the same amount of time, no matter the input size
    // O(1)
    
	std::unordered_set <int> comp; // complements
	for (int value: data){
	    // first check and then insert
	    // Check if I have seen it
		if (comp.find(value) != comp.end())
		    // find() return Iterator to an element with key equivalent to key. 
		    // If no such element is found, past-the-end (see end()) iterator is returned. 
		    // If the element is not found .end() is returned
		    // if we store find() value, with & we got addres and with * the value of the address
		    
            //.end() Returns an iterator to the 
            // element following the last element of the unordered_set
			return true;
		comp.insert(sum - value);
	}
	return false;
}

/*  
Collection of numbers, take the maching par that is 
equal to a sum that is given by the user.

[1, 2, 3, 4] sum = 8 -> no
[1, 2, 4, 4] sum = 8 -> yes
*/

int main(){
    std::vector <int> vect { 5, 2, 3, 9};
    std::vector <int> vect2 { 1, 2, 4, 4};
    int sum = 8;

    std::cout << HasPairWithSum(vect, sum) << std::endl;
    std::cout << HasPairWithSum(vect2, sum) << std::endl;
    
    return 0;
}