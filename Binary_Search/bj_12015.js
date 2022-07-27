const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
const n = parseInt(input[0]);
const a = input[1].split(" ").map(Number);
const lis = [a[0]];

const binarySearch = (lis, left, right, num) => {
  while (left < right) {
    let mid = Math.floor((left + right) / 2);

    if (lis[mid] < num) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return right;
};

for (let i = 1; i < n; i++) {
  if (lis[lis.length - 1] < a[i]) {
    lis.push(a[i]);
  } else {
    let index = binarySearch(lis, 0, lis.length - 1, a[i]);
    lis[index] = a[i];
  }
}

console.log(lis.length);
