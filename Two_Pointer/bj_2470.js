const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
const n = parseInt(input[0]);
const arr = input[1].split(" ").map(Number);
arr.sort((a, b) => a - b);

let intervalSum = 0;
let start = 0;
let end = n - 1;
let answer = Infinity;
let answerList = [0, 0];

while (start !== end) {
  intervalSum = arr[start] + arr[end];
  if (Math.abs(intervalSum) < answer) {
    answer = Math.abs(intervalSum);
    answerList[0] = arr[start];
    answerList[1] = arr[end];
  }
  if (intervalSum === 0) {
    break;
  }
  intervalSum < 0 ? start++ : end--;
}

console.log(answerList.join(" "));
