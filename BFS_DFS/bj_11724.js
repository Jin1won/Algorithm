const fs = require("fs");
const { config } = require("process");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
const [n, m] = input[0].split(" ").map(Number);
const edges = [];

for (let i = 1; i <= n; i++) {
  edges[i] = [];
}

for (let i = 0; i < m; i++) {
  let [u, v] = input[i + 1].split(" ").map(Number);
  edges[u].push(v);
  edges[v].push(u);
}

let visited = new Array(n + 1).fill(false);
let result = 0;

function dfs(node) {
  visited[node] = true;

  for (let i = 0; i < edges[node].length; i++) {
    if (!visited[edges[node][i]]) {
      dfs(edges[node][i]);
    }
  }
}

for (let i = 1; i <= n; i++) {
  if (!visited[i]) {
    dfs(i);
    result++;
  }
}

console.log(result);
