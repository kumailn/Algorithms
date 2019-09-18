//  Question: Given a string, find the first character that is unique
//  Solution: Count the occurance of each letter, find the first letter with 1 occurance from your hashmap
//            because we don't want to loop over our input string twice if it's very long
//  Difficulty: Easy

/**
 * @param {string} s
 * @return {number}
 */

let firstUniqChar = function(s) {
    // Create a hashmap to store the counts of each letter as well as the index
    let letterCounts = {}

    // Store the lowest index we see with a letter count of 1 when we traverse our hashmap
    smallestIndex = s.length 

    // Store each items count as well as the first index it occured at
    for (let i = 0; i < s.length; i++) {
        if (!letterCounts[s[i]]) letterCounts[s[i]] = [1, i];
        else letterCounts[s[i]][0]++;
    }
    
    // Loop through the hashmap updating the smallestIndex each time we see a letter
    // with a count of 1 and a smaller index than the previous 
    let keys = Object.keys(letterCounts);
    for(let letter of keys){
        if (letterCounts[letter][0] == 1) {
            if (letterCounts[letter][1] < smallestIndex) smallestIndex = letterCounts[letter][1];
        }
    }

    // Return either the index of the first char or -1 if there is no unique char
    return smallestIndex == s.length ? -1 : smallestIndex
};