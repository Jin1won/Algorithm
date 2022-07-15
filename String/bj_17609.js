const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
const t = parseInt(input[0]);
const words = [];
for (let i = 0; i < t; i++) {
  words.push(input[1 + i].trim());
}

const checkPseudoPalindrome = (word, left, right) => {
  while (left < right) {
    if (word[left] === word[right]) {
      left += 1;
      right -= 1;
    } else return false;
  }
  return true;
};

const solution = (word) => {
  let left = 0;
  let right = word.length - 1;
  while (left < right) {
    if (word[left] === word[right]) {
      left += 1;
      right -= 1;
    } else {
      if (
        checkPseudoPalindrome(word, left + 1, right) ||
        checkPseudoPalindrome(word, left, right - 1)
      )
        return 1;
      return 2;
    }
  }
  return 0;
};

const result = [];
for (const word of words) result.push(solution(word));

console.log(result.join("\n"));
