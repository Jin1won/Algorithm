function solution(id_list, report, k) {
  const answer = new Array(id_list.length);
  answer.fill(0);
  const list_length = id_list.length;
  let id_reported = Array.from(Array(list_length), () => new Set());

  report.forEach((r) => {
    id_reported[id_list.indexOf(r.split(" ")[1])].add(r.split(" ")[0]);
  });

  for (const key in id_reported) {
    if (id_reported[key].size >= k) {
      id_reported[key].forEach((user) => {
        answer[id_list.indexOf(user)] += 1;
      });
    }
  }

  return answer;
}
