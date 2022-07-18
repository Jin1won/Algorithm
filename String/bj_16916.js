const fs = require("fs");
const { setFlagsFromString } = require("v8");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
const s = input[0];
const p = input[1];

const makeTable = (p) => {
  let table = Array(p.length).fill(0);

  j = 0;
  for (let i = 1; i < table.length; i++) {
    while (j > 0 && p[i] !== p[j]) {
      j = table[j - 1];
    }
    if (p[i] === p[j]) {
      j += 1;
      table[i] = j;
    }
  }

  return table;
};

const kmp = (s, p, table) => {
  let j = 0;

  for (let i = 0; i < s.length; i++) {
    while (j > 0 && s[i] !== p[j]) {
      j = table[j - 1];
    }
    if (s[i] === p[j]) {
      j += 1;
      if (j === p.length) {
        return true;
      }
    }
  }
  return false;
};

if (kmp(s, p, makeTable(p))) {
  console.log(1);
} else {
  console.log(0);
}
