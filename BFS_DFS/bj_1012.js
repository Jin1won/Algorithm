const input = [];
let inputIndex = 0;

//상, 하, 좌, 우
const distances = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];
//그래프 이중 배열, 가로 길이(열 개수), 세로 길이(행 개수), 배추 개수, 결과 담는 변수
let graph, m, n, k, result;

const strToNumArr = (str) =>
  str.split(" ").map((numString) => Number(numString));

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", function (line) {
    input.push(line.trim());
  })
  .on("close", function () {
    let t = Number(input[inputIndex++]);
    //테스트 케이스 수만큼
    while (t--) {
      [m, n, k] = strToNumArr(input[inputIndex++]);
      //그래프 초기화
      graph = [...Array(n)].map(() => Array(m).fill(0));
      //결과(필요한 벌레 수) 담는 변수 초기화
      result = 0;

      //배추 있는 위치 그래프에 표시
      while (k--) {
        const [x, y] = strToNumArr(input[inputIndex++]);
        graph[y][x] = 1;
      }

      let flag = true;

      while (flag) {
        // let nr, nc;
        //그래프 돌면서 방문하지 않은 배추 위치 알아내기
        for (let i = 0; i < n; i++) {
          for (let j = 0; j < m; j++) {
            if (graph[i][j] === 1) {
              bfs(i, j);
              result++;
            }

            if (i === n - 1 && j === m - 1) {
              flag = false;
            }
          }
          //   const j = graph[i].indexOf(1);
          //   //없으면 계속
          //   if (j === -1) {
          //     continue;
          //   }
          //   //있으면 해당 위치 저장하고 break
          //   (nr = i), (nc = j);
          //   break;
        }

        // //방문하지 않은 배추 없으면 break
        // if (nr === undefined && nc === undefined) break;

        // //필요한 벌레 수+1
        // result++;
        // //인접한 배추 방문
        // bfs(nr, nc);
      }

      console.log(result);
    }
  });

//너비 우선 탐색으로 인접한 배추 방문
const bfs = (rStart, cStart) => {
  //방문할 배추 위치 담는 큐
  const queue = [[rStart, cStart]];
  let r, c, nr, nc;
  //큐가 비기 전까지
  while (queue.length !== 0) {
    //첫 원소 pop
    [r, c] = queue.shift();
    //이미 방문했으면 continue
    if (!graph[r][c]) {
      continue;
    }

    //배추 방문 사실 저장
    graph[r][c] = 0;
    //인접한 정점 중 방문하지 않은 정점 큐에 삽입
    distances.forEach(([dr, dc]) => {
      nr = r + dr;
      nc = c + dc;
      if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
        return;
      }
      if (graph[nr][nc]) {
        queue.push([nr, nc]);
      }
    });
  }
};
