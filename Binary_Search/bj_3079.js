const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
let a = input[0].split(" ").map(Number);
const n = a[0];
const m = a[1];
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(input[1 + i]));
}
let start = Math.min(...arr);
let end = Math.max(...arr) * m;
let answer = 0;

while (start <= end) {
  let people = 0;
  let mid = parseInt((start + end) / 2);

  for (let i = 0; i < n; i++) {
    people += parseInt(mid / arr[i]);
  }

  if (people >= m) {
    end = mid - 1;
    answer = mid;
  } else {
    start = mid + 1;
  }
}

console.log(answer);
