const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim().split(" ");
const [n, r, c] = input.map((e) => +e);

const recursion = (n, r, c) => {
  if (n === 0) return 0;
  let halfSize = Math.pow(2, n - 1);

  if (r < halfSize && c < halfSize) return recursion(n - 1, r, c);
  if (r < halfSize && c >= halfSize)
    return halfSize * halfSize + recursion(n - 1, r, c - halfSize);
  if (r >= halfSize && c < halfSize)
    return 2 * halfSize * halfSize + recursion(n - 1, r - halfSize, c);
  if (r >= halfSize && c >= halfSize)
    return (
      3 * halfSize * halfSize + recursion(n - 1, r - halfSize, c - halfSize)
    );
};

console.log(recursion(n, r, c));
