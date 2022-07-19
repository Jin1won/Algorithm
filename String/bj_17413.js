const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim();
const s = input.split("");

let result = [];

const isNum = (c) => {
  if (c.trim() === "") return false;
  return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].includes(Number(c));
};

const isAlphabet = (c) => {
  const code = c.charCodeAt();
  if (65 <= code && code <= 90) return true;
  if (97 <= code && code <= 122) return true;
  return false;
};

while (s.length > 0) {
  const stack = [];

  if (s[0] === "<") {
    while (s[0] !== ">") {
      stack.push(s.shift());
    }
    stack.push(s.shift());
    result.push(...stack);
  } else if (isNum(s[0]) || isAlphabet(s[0])) {
    while (s.length > 0 && s[0] !== "<" && s[0] !== " ") {
      stack.push(s.shift());
    }
    stack.reverse();
    result.push(...stack);
  } else {
    result.push(s.shift());
  }
}

console.log(result.join(""));
