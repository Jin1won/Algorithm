function solution(N, road, K) {
  let answer = 0;
  const dist = new Array(N + 1).fill(Infinity);
  const adj = Array.from({ length: N + 1 }, () => []);
  const priorityQueue = [];

  road.map((route) => {
    adj[route[0]].push({
      to: route[1],
      cost: route[2],
    });
    adj[route[1]].push({
      to: route[0],
      cost: route[2],
    });
  });

  priorityQueue.push({ to: 1, cost: 0 });
  dist[1] = 0; // 출발 노드

  while (priorityQueue.length !== 0) {
    // cost 기준 오름차순
    priorityQueue.sort((a, b) => {
      return a.cost - b.cost;
    });

    const { to, cost } = priorityQueue.shift();
    adj[to].forEach((nextNode) => {
      if (dist[nextNode.to] > dist[to] + nextNode.cost) {
        dist[nextNode.to] = dist[to] + nextNode.cost;
        priorityQueue.push(nextNode);
      }
    });
  }

  answer = dist.filter((num) => num <= K).length;
  return answer;
}
