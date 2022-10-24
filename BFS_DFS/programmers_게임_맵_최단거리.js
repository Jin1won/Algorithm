function solution(maps) {
  let n = maps.length;
  let m = maps[0].length;
  const visited = Array.from(Array(n), () => Array(m).fill(false));
  let queue = [];
  queue.push([0, 0, 1]);
  visited[0][0] = true;

  const bfs = () => {
    while (queue.length > 0) {
      const [x, y, cnt] = queue.shift();

      if (x === n - 1 && y === m - 1) {
        return cnt;
      }

      for ([dx, dy] of [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
      ]) {
        let nx = x + dx;
        let ny = y + dy;

        if (
          0 <= nx &&
          nx < n &&
          0 <= ny &&
          ny < m &&
          !visited[nx][ny] &&
          maps[nx][ny] !== 0
        ) {
          visited[nx][ny] = true;
          queue.push([nx, ny, cnt + 1]);
        }
      }
    }
    return -1;
  };

  return bfs();
}
