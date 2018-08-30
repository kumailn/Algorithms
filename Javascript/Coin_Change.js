// amount = total amount, coins = array of coin
function coinChange(amount, coins){
    let storedAmounts = Array(amount + 1).fill(0);
    storedAmounts[0] = 1;
    for(let coin of coins){
        for(let currentAmount of storedAmounts.keys()){
            if(currentAmount >= coin){
                let remainder = currentAmount - coin;
                storedAmounts[currentAmount] += storedAmounts[remainder];
            }
        }
    }
    return storedAmounts.pop();
}

console.log(coinChange(12, [1, 2, 5]));