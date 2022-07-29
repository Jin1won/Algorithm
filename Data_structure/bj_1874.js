const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
const n = parseInt(input[0]);
const numbers = [];
const arr = [];
let operators = "";
let cnt = 1;
let flag = true;

for (let i = 0; i < n; i++) {
  numbers.push(Number(input[1 + i]));
}

for (let i = 0; i < n; i++) {
  const number = numbers.shift();

  while (cnt <= number) {
    arr.push(cnt++);
    operators += "+";
  }

  const popNumber = arr.pop();
  if (popNumber !== number) {
    flag = false;
    console.log("NO");
    break;
  }
  operators += "-";
}

if (flag) {
  console.log(operators.split("").join("\n"));
}
