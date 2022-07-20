const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
const n = parseInt(input[0]);
const tree = [...Array(n + 1)].map(() => []);

for (let i = 0; i < n - 1; i++) {
  const [from, to] = input[1 + i].split(" ").map(Number);
  tree[from].push(to);
  tree[to].push(from);
}

let visited = Array(n + 1).fill(0);

const bfs = () => {
  const queue = [];
  visited[1] = 1;
  queue.push(1);
  while (queue.length) {
    const curNode = queue.pop();
    for (let next of tree[curNode]) {
      if (visited[next]) continue;
      visited[next] = curNode;
      queue.push(next);
    }
  }
};

bfs();

console.log(visited.slice(2).join("\n"));
