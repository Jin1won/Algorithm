const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
const [m, n, k] = input.shift().split(" ");
let graph = Array.from({ length: m }).map(
  (row) => (row = Array.from({ length: n }).fill(0))
);

for (let i = 0; i < k; i++) {
  let [y1, x1, y2, x2] = input
    .shift()
    .split(" ")
    .map((el) => Number(el));

  for (let x = x1; x < x2; x++) {
    for (let y = y1; y < y2; y++) {
      graph[x][y] = 1;
    }
  }
}

let visited = Array.from({ length: m }).map(
  (row) => (row = Array.from({ length: n }).fill(false))
);

const bfs = (x, y) => {
  visited[x][y] = true;
  const queue = [[x, y]];
  let dx = [0, 0, 1, -1];
  let dy = [-1, 1, 0, 0];
  let cnt = 1;
  while (queue.length) {
    [cx, cy] = queue.shift();
    for (let i = 0; i < 4; i++) {
      let nx = cx + dx[i];
      let ny = cy + dy[i];
      if (nx >= 0 && nx < graph.length && ny >= 0 && ny < graph[0].length) {
        if (!visited[nx][ny]) {
          if (graph[nx][ny] === 0) {
            visited[nx][ny] = true;
            queue.push([nx, ny]);
            cnt += 1;
          }
        }
      }
    }
  }
  return cnt;
};

let area = [];

for (let i = 0; i < m; i++) {
  for (let j = 0; j < n; j++) {
    if (graph[i][j] === 0 && !visited[i][j]) {
      area.push(bfs(i, j));
    }
  }
}

area.sort((a, b) => a - b);
let answer = area.length + "\n" + area.join(" ");
console.log(answer);
