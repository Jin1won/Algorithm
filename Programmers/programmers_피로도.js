function solution(k, dungeons) {
  let answer = 0;
  let visited = Array.from(dungeons.length).fill(false);

  function dfs(cnt, k) {
    for (let i = 0; i < dungeons.length; i++) {
      if (!visited[i] && k >= dungeons[i][0]) {
        visited[i] = true;
        dfs(cnt + 1, k - dungeons[i][1]);
        visited[i] = false;
      }
    }
    answer = answer < cnt ? cnt : answer;
  }

  dfs(0, k);

  return answer;
}
